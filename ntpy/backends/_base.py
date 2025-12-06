from abc import ABC, abstractmethod


class BaseBackend(ABC):
    """Abstract base class for backends."""

    @abstractmethod
    def hash(self, data: str) -> str:
        """Generate a hash for the given data.

        Args:
            data (str): The data to hash.

        Returns:
            str: The generated hash.
        """

    @abstractmethod
    def store(self, data: str) -> str:
        """Store the given data and return its hash.

        Args:
            data (str): The data to store.

        Returns:
            str: The hash of the stored data.
        """

    @abstractmethod
    def has_hash(self, hash_value: str) -> bool:
        """Check if the given hash exists.

        Args:
            hash_value (str): The hash to check.

        Returns:
            bool: True if the hash exists, False otherwise.
        """
