#ZEUS- I START FROM THRE, WHERE EVERYONE GIVE-UP

from enum import auto

from .auto_name import AutoName


class PollType(AutoName):
    """Poll type enumeration used in :obj:`~zeuspy.types.Poll`."""

    QUIZ = auto()
    "Quiz poll"

    REGULAR = auto()
    "Regular poll"
