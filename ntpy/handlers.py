"""ntpy logging handlers module."""

import logging

from .enums import Priority
from .typing import Extras
from .request import publish
from .backends import BaseBackend, RedisBackend, InMemoryBackend

_MINUTE = 60


class _BaseNtpyHandler(logging.Handler):
    """Base Ntpy logging handler.

    Attribute:
        backend (BaseBackend): The backend storage for log deduplication.
        topic (str): The ntfy topic to publish logs to.
        title (str): The title for the published logs.
    """

    backend: BaseBackend
    topic: str
    title: str

    def emit(self, record: logging.LogRecord) -> None:
        """Emit a log record.

        Args:
            record (logging.LogRecord): The log record to emit.
        """
        log_entry = self.format(record)
        hash_value = self.backend.hash(log_entry)

        if not self.backend.has_hash(hash_value):
            self.backend.store(log_entry)

            extras: Extras = {"Priority": Priority.log_priority(record.levelno)}

            publish(topic=self.topic, data=log_entry, title=self.title, extras=extras)


class InMemoryNtpyHandler(_BaseNtpyHandler):
    """In-Memory Ntpy logging handler."""

    def __init__(
        self,
        topic: str,
        title: str = "",
        validity: int = 30 * _MINUTE,
        level: int = 0,
    ) -> None:
        """Initialize the in-memory logging handler.

        Args:
            topic (str): The ntfy topic to publish logs to.
            title (str, optional): The title for the published logs. Defaults to "".
            validity (int, optional): The validity duration for deduplication in seconds. Defaults to 30 * MINUTE.
            level (int, optional): The logging level. Defaults to 0.
        """
        super().__init__(level)
        self.topic = topic
        self.title = title
        self.backend: BaseBackend = InMemoryBackend(validity=validity)


class RedisNtpyHandler(_BaseNtpyHandler):
    """Redis Ntpy logging handler."""

    def __init__(
        self,
        topic: str,
        redis_url: str,
        title: str = "",
        validity: int = 30 * _MINUTE,
        level: int = 0,
    ) -> None:
        """Initialize the redis logging handler.

        Args:
            topic (str): The ntfy topic to publish logs to.
            redis_url (str): The Redis connection URL.
            title (str, optional): The title for the published logs. Defaults to "".
            validity (int, optional): The validity duration for deduplication in seconds. Defaults to 30 * MINUTE.
            level (int, optional): The logging level. Defaults to 0.
        """
        super().__init__(level)
        self.topic = topic
        self.title = title
        self.backend: BaseBackend = RedisBackend(validity=validity, redis_url=redis_url)
