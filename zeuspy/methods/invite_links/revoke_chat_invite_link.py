#ZEUS- I START FROM THRE, WHERE EVERYONE GIVE-UP

from typing import Union

import zeuspy
from zeuspy import raw
from zeuspy import types


class RevokeChatInviteLink:
    async def revoke_chat_invite_link(
        self: "zeuspy.Client",
        chat_id: Union[int, str],
        invite_link: str,
    ) -> "types.ChatInviteLink":
        """Revoke a previously created invite link.

        If the primary link is revoked, a new link is automatically generated.

        You must be an administrator in the chat for this to work and must have the appropriate admin rights.

        Parameters:
            chat_id (``int`` | ``str``):
                Unique identifier for the target chat or username of the target channel/supergroup
                (in the format @username).

            invite_link (``str``):
               The invite link to revoke.

        Returns:
            :obj:`~zeuspy.types.ChatInviteLink`: On success, the invite link object is returned.
        """

        r = await self.invoke(
            raw.functions.messages.EditExportedChatInvite(
                peer=await self.resolve_peer(chat_id),
                link=invite_link,
                revoked=True
            )
        )

        users = {i.id: i for i in r.users}

        chat_invite = (
            r.new_invite
            if isinstance(r, raw.types.messages.ExportedChatInviteReplaced)
            else r.invite
        )

        return types.ChatInviteLink._parse(self, chat_invite, users)
