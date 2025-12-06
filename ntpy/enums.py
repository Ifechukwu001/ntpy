"""ntpy enums."""

from enum import StrEnum


class Tags(StrEnum):
    """An enum representing possible tags for ntfy notifications."""

    THUMBS_UP = "+1"
    THUMBS_DOWN = "-1"
    PARTYING_FACE = "partying_face"
    TADA = "tada"
    HEAVY_CHECK_MARK = "heavy_check_mark"
    LOUDSPEAKER = "loudspeaker"
    WARNING = "warning"
    ROTATING_LIGHT = "rotating_light"
    TRIANGULAR_FLAG_ON_POST = "triangular_flag_on_post"
    SKULL = "skull"
    FACEPALM = "facepalm"
    NO_ENTRY = "no_entry"
    NO_ENTRY_SIGN = "no_entry_sign"
    CD_PLATE = "cd"
    COMPUTER = "computer"

    @classmethod
    def stringify(cls, tags: list["Tags"]) -> str:
        """Converts a list of Tags enum members to a comma-separated string.

        Args:
            tags (list[Tags]): A list of Tags enum members.

        Returns:
            str: A comma-separated string of tag values.
        """
        return ",".join(tag.value for tag in tags)


class Priority(StrEnum):
    """An enum representing possible priority levels for ntfy notifications."""

    MIN = "1"
    LOW = "2"
    DEFAULT = "3"
    HIGH = "4"
    MAX = "5"
