"""ntpy request module."""

import httpx

from .typing import Extras


async def apublish(topic: str, data: str, title: str = "", extras: Extras = {}) -> bool:
    """Asynchronously publishes notifications.

    Args:
        topic (str): The topic to publish the data.
        data (str): The data content to be published.
        title (str, optional): The title for the published data. Defaults to "".
        extras (Extras, optional): Additional metadata for the notification. Defaults to {}.

    Returns:
        bool: True if the data was successfully published, False otherwise.
    """
    headers: dict[str, str] = {key: str(value) for key, value in extras.items()}
    if title:
        headers["Title"] = title

    try:
        async with httpx.AsyncClient() as client:
            await client.post(f"https://ntfy.sh/{topic}", content=data, headers=headers)
    except httpx.HTTPError:
        return False

    return True


def publish(topic: str, data: str, title: str = "", extras: Extras = {}) -> bool:
    """Publishes notifications.

    Args:
        topic (str): The topic to publish the data.
        data (str): The data content to be published.
        title (str, optional): The title for the published data. Defaults to "".
        extras (Extras, optional): Additional metadata for the notification. Defaults to {}.

    Returns:
        bool: True if the data was successfully published, False otherwise.
    """
    headers: dict[str, str] = {key: str(value) for key, value in extras.items()}
    if title:
        headers["Title"] = title

    try:
        with httpx.Client() as client:
            client.post(f"https://ntfy.sh/{topic}", content=data, headers=headers)
    except httpx.HTTPError:
        return False

    return True
