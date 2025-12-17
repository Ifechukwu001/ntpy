"""Test for redis backend."""

import time

from ntpy.backends.redis import RedisBackend


def test_redis_consistent_hash() -> None:
    """Test that the redis backend generates consistent hashes."""
    backend = RedisBackend(validity=10, redis_url="redis://localhost:6379/0")
    backend_2 = RedisBackend(validity=10, redis_url="redis://localhost:6379/0")

    data = "sample data"
    hash1 = backend.hash(data)
    hash2 = backend_2.hash(data)

    assert hash1 == hash2


def test_redis_store_and_check() -> None:
    """Test storing and checking data in the redis backend."""
    backend = RedisBackend(validity=10, redis_url="redis://localhost:6379/0")

    data = "sample data 4"
    data_hash = backend.hash(data)

    backend.store(data)
    assert backend.has_hash(data_hash)

    assert not backend.has_hash("nonexistenthash")


def test_redis_expiry() -> None:
    """Test that data expires correctly in the redis backend."""
    backend = RedisBackend(
        validity=1, redis_url="redis://localhost:6379/0"
    )  # 1 second validity

    data = "sample data r"
    data_hash = backend.hash(data)

    backend.store(data)
    assert backend.has_hash(data_hash)

    time.sleep(1)  # Wait for data to expire
    assert not backend.has_hash(data_hash)
