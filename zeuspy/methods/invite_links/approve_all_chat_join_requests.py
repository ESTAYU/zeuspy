#ZEUS- I START FROM THRE, WHERE EVERYONE GIVE-UP

from typing import Union

import zeuspy
from zeuspy import raw


class ApproveAllChatJoinRequests:
    async def approve_all_chat_join_requests(
        self: "zeuspy.Client",
        chat_id: Union[int, str],
        invite_link: str = None
    ) -> bool:
        """Approve all pending join requests in a chat.

        Parameters:
            chat_id (``int`` | ``str``):
                Unique identifier for the target chat or username of the target channel/supergroup
                (in the format @username).

            invite_link (``str``, *optional*):
                Pass an invite link to approve only its join requests.
                By default, all join requests are approved.

        Returns:
            ``bool``: True on success.
        """
        await self.invoke(
            raw.functions.messages.HideAllChatJoinRequests(
                peer=await self.resolve_peer(chat_id),
                approved=True,
                link=invite_link
            )
        )

        return True
