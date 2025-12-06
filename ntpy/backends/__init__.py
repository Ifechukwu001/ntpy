"""ntpy backends package."""

from ._base import BaseBackend

DEFAULT_BACKEND = "ntpy.backends.inmemory.InMemoryBackend"


__all__ = ["DEFAULT_BACKEND", "BaseBackend"]
