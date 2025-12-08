"""In-memory backend implementation."""

import time
import hashlib

import cachetools

from ._base import BaseBackend


class InMemoryBackend(BaseBackend):
    """In-memory backend for storing data."""

    _STORAGE: cachetools.TTLCache[str, float] | None = None

    def __init__(self, validity: int) -> None:
        """Initialize the in-memory storage."""
        self.validity = validity

        if InMemoryBackend._STORAGE is None:
            InMemoryBackend._STORAGE = cachetools.TTLCache(maxsize=100000, ttl=validity)

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
        if self._STORAGE is None:
            raise RuntimeError("Storage was not initialized")

        self._STORAGE[hash_value] = time.monotonic()

        return hash_value

    def has_hash(self, hash_value: str) -> bool:
        """Check if the given hash exists.

        Args:
            hash_value (str): The hash to check.

        Returns:
            bool: True if the hash exists, False otherwise.
        """
        if self._STORAGE is None:
            raise RuntimeError("Storage was not initialized")

        return self._STORAGE.get(hash_value) is not None
