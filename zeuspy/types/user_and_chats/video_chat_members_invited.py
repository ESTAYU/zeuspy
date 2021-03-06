#ZEUS- I START FROM THRE, WHERE EVERYONE GIVE-UP

from typing import List, Dict

from zeuspy import raw, types
from ..object import Object


class VideoChatMembersInvited(Object):
    """A service message about new members invited to a voice chat.


    Parameters:
        users (List of :obj:`~zeuspy.types.User`):
            New members that were invited to the voice chat.
    """

    def __init__(
        self, *,
        users: List["types.User"]
    ):
        super().__init__()

        self.users = users

    @staticmethod
    def _parse(
        client,
        action: "raw.types.MessageActionInviteToGroupCall",
        users: Dict[int, "raw.types.User"]
    ) -> "VideoChatMembersInvited":
        users = [types.User._parse(client, users[i]) for i in action.users]

        return VideoChatMembersInvited(users=users)
