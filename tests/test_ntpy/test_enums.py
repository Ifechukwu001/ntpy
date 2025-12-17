"""Tests for ntpy enums."""

import logging

from ntpy.enums import Tags, Priority


def test_tags_stringify() -> None:
    """Test for Tags stringify method."""
    assert f"{Tags.COMPUTER},{Tags.CD_PLATE},{Tags.FACEPALM}" == Tags.stringify(
        [Tags.COMPUTER, Tags.CD_PLATE, Tags.FACEPALM]
    )


def test_log_priority() -> None:
    """Test for Priority log_priority method."""
    assert Priority.MAX == Priority.log_priority(logging.CRITICAL)
    assert Priority.HIGH == Priority.log_priority(logging.ERROR)
    assert Priority.DEFAULT == Priority.log_priority(logging.WARNING)
    assert Priority.LOW == Priority.log_priority(logging.INFO)
    assert Priority.MIN == Priority.log_priority(logging.DEBUG)
    assert Priority.MIN == Priority.log_priority(logging.NOTSET)
