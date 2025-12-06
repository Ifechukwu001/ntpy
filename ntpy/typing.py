"""ntpy typings."""

from typing import TypedDict, NotRequired


class Extras(TypedDict):
    """An Extras dict representing optional extra metadata fields for ntfy headers .

    Attributes:
        Tags (NotRequired[str]): Optional string containing tags or categories associated with the item.
        Priority (NotRequired[str]): Optional string indicating the priority level of the item.
        Email (NotRequired[str]): Optional string containing an email address.
        Icon (NotRequired[str]): Optional string representing an icon identifier or path.
    """

    Tags: NotRequired[str]
    Priority: NotRequired[str]
    Email: NotRequired[str]
    Icon: NotRequired[str]
