"""ntpy logging handlers module."""

import logging
from importlib import import_module

from ntpy.request import publish
from ntpy.backends import DEFAULT_BACKEND, BaseBackend

MINUTE = 60


class NtpyHandler(logging.Handler):
    """Ntpy logging handler."""

    def __init__(
        self,
        topic: str,
        title: str = "",
        backend: str = DEFAULT_BACKEND,
        validity: int = 30 * MINUTE,
        level: int = 0,
    ) -> None:
        """Initialize the Ntpy logging handler."""
        super().__init__(level)
        self.topic = topic
        self.title = title

        try:
            module_path, class_name = backend.rsplit(".", 1)
            module = import_module(module_path)
            backend_class = getattr(module, class_name)
            self.backend: BaseBackend = backend_class(validity=validity)
        except (ImportError, AttributeError) as e:
            raise ImportError(f"Could not import backend '{backend}': {e}")

    def emit(self, record: logging.LogRecord) -> None:
        """Emit a log record.

        Args:
            record (logging.LogRecord): The log record to emit.
        """
        log_entry = self.format(record)
        hash_value = self.backend.hash(log_entry)

        if not self.backend.has_hash(hash_value):
            self.backend.store(log_entry)
            publish(topic=self.topic, data=log_entry, title=self.title)
