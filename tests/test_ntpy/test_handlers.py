"""Test for ntpy logging handlers."""

import logging
from unittest.mock import patch

import pytest

from ntpy.enums import Priority
from ntpy.handlers import RedisNtpyHandler, InMemoryNtpyHandler


@pytest.fixture
def logger() -> logging.Logger:
    """Get a test logger."""
    logger = logging.getLogger("test_logger")
    logger.setLevel(logging.DEBUG)
    return logger


def test_inmemory_ntpy_handler_log_emit(logger: logging.Logger) -> None:
    """Test InMemoryNtpyHandler log emit."""
    patch_publish = patch("ntpy.handlers.publish")
    handler = InMemoryNtpyHandler(topic="test/topic", title="Test Title", validity=60)

    logger.addHandler(handler)

    record = logging.LogRecord(
        name="test_logger",
        level=logging.INFO,
        pathname=__file__,
        lineno=10,
        msg="This is a test log message.",
        args=(),
        exc_info=None,
    )

    with patch_publish as mock_publish:
        handler.emit(record)

        mock_publish.assert_called_once()
        _, called_kwargs = mock_publish.call_args

        assert called_kwargs["topic"] == "test/topic"
        assert called_kwargs["data"] == "This is a test log message."
        assert called_kwargs["title"] == "Test Title"
        assert called_kwargs["extras"]["Priority"] == Priority.LOW

        handler.emit(record)
        mock_publish.assert_called_once()

    logger.removeHandler(handler)


def test_redis_ntpy_handler_log_emit(logger: logging.Logger) -> None:
    """Test RedisNtpyHandler log emit."""
    patch_publish = patch("ntpy.handlers.publish")
    handler = RedisNtpyHandler(
        topic="test/topic",
        redis_url="redis://localhost:6379",
        title="Test Title",
        validity=60,
    )

    logger.addHandler(handler)

    record = logging.LogRecord(
        name="test_logger",
        level=logging.INFO,
        pathname=__file__,
        lineno=10,
        msg="This is a test log message.",
        args=(),
        exc_info=None,
    )

    with patch_publish as mock_publish:
        handler.emit(record)

        mock_publish.assert_called_once()
        _, called_kwargs = mock_publish.call_args

        assert called_kwargs["topic"] == "test/topic"
        assert called_kwargs["data"] == "This is a test log message."
        assert called_kwargs["title"] == "Test Title"
        assert called_kwargs["extras"]["Priority"] == Priority.LOW

        handler.emit(record)
        mock_publish.assert_called_once()

    logger.removeHandler(handler)
