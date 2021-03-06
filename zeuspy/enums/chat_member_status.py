#ZEUS- I START FROM THRE, WHERE EVERYONE GIVE-UP

from enum import auto

from .auto_name import AutoName


class ChatMemberStatus(AutoName):
    """Chat member status enumeration used in :obj:`~zeuspy.types.ChatMember`."""

    OWNER = auto()
    "Chat owner"

    ADMINISTRATOR = auto()
    "Chat administrator"

    MEMBER = auto()
    "Chat member"

    RESTRICTED = auto()
    "Restricted chat member"

    LEFT = auto()
    "Left chat member"

    BANNED = auto()
    "Banned chat member"
