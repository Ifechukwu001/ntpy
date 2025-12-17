"""Conftest file for pytest configuration and fixtures."""

import time
from typing import Any, ClassVar

import httpx
import redis
import pytest


class _MockResponse:
    def raise_for_status(self) -> None:
        return None


class _MockClient:
    def post(self, url: str, content: str, headers: dict[str, str]) -> _MockResponse:
        return _MockResponse()

    def close(self) -> None: ...

    def __enter__(self) -> "_MockClient":
        return self

    def __exit__(self, *args: Any) -> None:  # noqa: ANN401
        ...


class _AMockClient:
    async def post(
        self, url: str, content: str, headers: dict[str, str]
    ) -> _MockResponse:
        return _MockResponse()

    async def aclose(self) -> None: ...

    async def __aenter__(self) -> "_AMockClient":
        return self

    async def __aexit__(self, *args: Any) -> None:  # noqa: ANN401
        ...


class _MockFailResponse:
    def raise_for_status(self) -> None:
        raise httpx.HTTPError("Mock failure")


class _MockFailClient:
    def post(
        self, url: str, content: str, headers: dict[str, str]
    ) -> _MockFailResponse:
        return _MockFailResponse()

    def close(self) -> None: ...

    def __enter__(self) -> "_MockFailClient":
        return self

    def __exit__(self, *args: Any) -> None:  # noqa: ANN401
        ...


class _AMockFailClient:
    async def post(
        self, url: str, content: str, headers: dict[str, str]
    ) -> _MockFailResponse:
        return _MockFailResponse()

    async def aclose(self) -> None: ...

    async def __aenter__(self) -> "_AMockFailClient":
        return self

    async def __aexit__(self, *args: Any) -> None:  # noqa: ANN401
        ...


@pytest.fixture(autouse=True)
def httpx_client() -> None:
    """Fixture to mock httpx Client for all tests."""
    pytest.MonkeyPatch().setattr("httpx.Client", lambda: _MockClient())
    pytest.MonkeyPatch().setattr("httpx.AsyncClient", lambda: _AMockClient())


@pytest.fixture
def httpx_failure_client() -> None:
    """Fixture to mock httpx Client failure for all tests."""
    pytest.MonkeyPatch().setattr("httpx.Client", lambda: _MockFailClient())
    pytest.MonkeyPatch().setattr("httpx.AsyncClient", lambda: _AMockFailClient())


class RedisLikeBackend:
    """A mock Redis-like backend for testing purposes."""

    _storage: ClassVar[dict[str, float]] = {}

    def ping(self) -> None:
        """Simulate a ping to the Redis server."""
        ...

    def set(self, key: str, value: float, ex: int) -> None:
        """Set a key with an expiration time."""
        self._storage[key] = value + ex

    def get(self, key: str) -> float | None:
        """Get a key exists and has not expired."""
        expiry = self._storage.get(key)
        if expiry is None:
            return None

        if time.monotonic() > expiry:
            del self._storage[key]
            return None

        return expiry


@pytest.fixture(autouse=True)
def mock_redis_storage(monkeypatch: pytest.MonkeyPatch) -> None:
    """Mock the redis storage."""

    def from_url(url: str) -> RedisLikeBackend:
        return RedisLikeBackend()

    monkeypatch.setattr(redis.Redis, "from_url", from_url)
