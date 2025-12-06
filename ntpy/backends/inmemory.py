"""In-memory backend implementation."""

from datetime import datetime, timedelta

from ._base import BaseBackend


class InMemoryBackend(BaseBackend):
    """In-memory backend for storing data."""

    def __init__(self, validity: int) -> None:
        """Initialize the in-memory storage."""
        self.validity = validity
        self.storage: dict[str, datetime] = {}

    def hash(self, data: str) -> str:
        """Generate a simple hash for the given data.

        Args:
            data (str): The data to hash.

        Returns:
            str: The generated hash.
        """
        return str(hash(data))

    def store(self, data: str) -> str:
        """Store the given data and return its hash.

        Args:
            data (str): The data to store.

        Returns:
            str: The hash of the stored data.
        """
        hash_value = self.hash(data)
        self.storage[hash_value] = datetime.now()
        return hash_value

    def has_hash(self, hash_value: str) -> bool:
        """Check if the given hash exists.

        Args:
            hash_value (str): The hash to check.

        Returns:
            bool: True if the hash exists, False otherwise.
        """
        in_store = hash_value in self.storage and datetime.now() < (
            self.storage[hash_value] + timedelta(seconds=self.validity)
        )

        if not in_store and hash_value in self.storage:
            del self.storage[hash_value]

        return in_store
