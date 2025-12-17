"""Test for in-memory backend."""

import time
from collections.abc import Generator

import pytest

from ntpy.backends.inmemory import InMemoryBackend


@pytest.fixture(autouse=True)
def reset_inmemory_storage() -> Generator[None]:
    """Reset the in-memory storage before each test."""
    InMemoryBackend._STORAGE = None  # type: ignore
    yield
    InMemoryBackend._STORAGE = None  # type: ignore


def test_inmemory_consistent_hash() -> None:
    """Test that the in-memory backend generates consistent hashes."""
    backend = InMemoryBackend(validity=10)
    backend_2 = InMemoryBackend(validity=10)

    data = "sample data"
    hash1 = backend.hash(data)
    hash2 = backend_2.hash(data)

    assert hash1 == hash2


def test_inmemory_store_and_check() -> None:
    """Test storing and checking data in the in-memory backend."""
    backend = InMemoryBackend(validity=10)

    data = "sample data 4"
    data_hash = backend.hash(data)

    backend.store(data)
    assert backend.has_hash(data_hash)

    assert not backend.has_hash("nonexistenthash")


def test_inmemory_expiry() -> None:
    """Test that data expires correctly in the in-memory backend."""
    backend = InMemoryBackend(validity=1)  # 1 second validity

    data = "sample data r"
    data_hash = backend.hash(data)

    backend.store(data)
    assert backend.has_hash(data_hash)

    time.sleep(1)  # Wait for data to expire
    assert not backend.has_hash(data_hash)


def test_uninitialized_storage() -> None:
    """Test that accessing uninitialized storage raises an error."""
    backend = InMemoryBackend(validity=10)
    InMemoryBackend._STORAGE = None  # type: ignore

    with pytest.raises(RuntimeError, match="Storage was not initialized"):
        backend.store("data")

    with pytest.raises(RuntimeError, match="Storage was not initialized"):
        backend.has_hash("somehash")
