#ZEUS- I START FROM THRE, WHERE EVERYONE GIVE-UP

from enum import auto

from .auto_name import AutoName


class MessageMediaType(AutoName):
    """Message media type enumeration used in :obj:`~zeuspy.types.Message`."""

    AUDIO = auto()
    "Audio media"

    DOCUMENT = auto()
    "Document media"

    PHOTO = auto()
    "Photo media"

    STICKER = auto()
    "Sticker media"

    VIDEO = auto()
    "Video media"

    ANIMATION = auto()
    "Animation media"

    VOICE = auto()
    "Voice media"

    VIDEO_NOTE = auto()
    "Video note media"

    CONTACT = auto()
    "Contact media"

    LOCATION = auto()
    "Location media"

    VENUE = auto()
    "Venue media"

    POLL = auto()
    "Poll media"

    WEB_PAGE = auto()
    "Web page media"

    DICE = auto()
    "Dice media"

    GAME = auto()
    "Game media"
