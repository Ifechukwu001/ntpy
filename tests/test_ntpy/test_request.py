"""Tests for ntpy request."""

import pytest

from ntpy.request import publish, apublish


def test_publish_success() -> None:
    """Test successful publish."""
    result = publish("test_topic", "test_data", "test_title")
    assert result is True


@pytest.mark.anyio
async def test_apublish_success() -> None:
    """Test successful asynchronous publish."""
    result = await apublish("test_topic", "test_data", "test_title")
    assert result is True


def test_publish_failure(httpx_failure_client: None) -> None:
    """Test failed publish."""
    result = publish("test_topic", "test_data", "test_title")
    assert result is False


@pytest.mark.anyio
async def test_apublish_failure(httpx_failure_client: None) -> None:
    """Test failed asynchronous publish."""
    result = await apublish("test_topic", "test_data", "test_title")
    assert result is False
