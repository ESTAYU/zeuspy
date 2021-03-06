#ZEUS- I START FROM THRE, WHERE EVERYONE GIVE-UP

from typing import Union

import zeuspy
from zeuspy import raw, types


class GetChatAdminsWithInviteLinks:
    async def get_chat_admins_with_invite_links(
        self: "zeuspy.Client",
        chat_id: Union[int, str],
    ):
        """Get the list of the administrators that have exported invite links in a chat.

        You must be the owner of a chat for this to work.

        Args:
            chat_id (``int`` | ``str``):
                Unique identifier for the target chat or username of the target channel/supergroup
                (in the format @username).

        Returns:
            List of :obj:`~zeuspy.types.ChatAdminWithInviteLink`: On success, the list of admins that have exported
            invite links is returned.
        """
        r = await self.invoke(
            raw.functions.messages.GetAdminsWithInvites(
                peer=await self.resolve_peer(chat_id)
            )
        )

        users = {i.id: i for i in r.users}

        return types.List(
            types.ChatAdminWithInviteLinks._parse(self, admin, users)
            for admin in r.admins
        )
