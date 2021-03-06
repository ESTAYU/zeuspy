#ZEUS- I START FROM THRE, WHERE EVERYONE GIVE-UP

from zeuspy import raw
from .auto_name import AutoName


class ChatMembersFilter(AutoName):
    """Chat members filter enumeration used in :meth:`~zeuspy.Client.get_chat_members`"""

    SEARCH = raw.types.ChannelParticipantsSearch
    "Search for members"

    BANNED = raw.types.ChannelParticipantsKicked
    "Banned members"

    RESTRICTED = raw.types.ChannelParticipantsBanned
    "Restricted members"

    BOTS = raw.types.ChannelParticipantsBots
    "Bots"

    RECENT = raw.types.ChannelParticipantsRecent
    "Recently active members"

    ADMINISTRATORS = raw.types.ChannelParticipantsAdmins
    "Administrators"
