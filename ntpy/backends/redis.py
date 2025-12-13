"""Redis backend implementation."""

import time
import hashlib

import redis

from ._base import BaseBackend


class RedisBackend(BaseBackend):
    """Redis backend for storing data."""

    def __init__(self, validity: int, redis_url: str) -> None:
        """Initialize the redis storage."""
        self.validity = validity
        self.client: redis.Redis = redis.Redis.from_url(redis_url)  # type: ignore

        self.client.ping()  # type: ignore

    def hash(self, data: str) -> str:
        """Generate a simple hash for the given data.

        Args:
            data (str): The data to hash.

        Returns:
            str: The generated hash.
        """
        return hashlib.sha256(data.encode()).hexdigest()

    def store(self, data: str) -> str:
        """Store the given data and return its hash.

        Args:
            data (str): The data to store.

        Returns:
            str: The hash of the stored data.
        """
        hash_value = self.hash(data)
        self.client.set(hash_value, time.monotonic(), ex=self.validity)

        return hash_value

    def has_hash(self, hash_value: str) -> bool:
        """Check if the given hash exists.

        Args:
            hash_value (str): The hash to check.

        Returns:
            bool: True if the hash exists, False otherwise.
        """
        return self.client.get(hash_value) is not None
