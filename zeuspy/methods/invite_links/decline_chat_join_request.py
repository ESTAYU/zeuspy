#ZEUS- I START FROM THRE, WHERE EVERYONE GIVE-UP

from typing import Union

import zeuspy
from zeuspy import raw


class DeclineChatJoinRequest:
    async def decline_chat_join_request(
        self: "zeuspy.Client",
        chat_id: Union[int, str],
        user_id: int,
    ) -> bool:
        """Decline a chat join request.

        The bot must be an administrator in the chat for this to work and must have the *can_invite_users* administrator
        right.

        Parameters:
            chat_id (``int`` | ``str``):
                Unique identifier for the target chat or username of the target channel/supergroup
                (in the format @username).

            user_id (``int``):
                Unique identifier of the target user.

        Returns:
            ``bool``: True on success.
        """
        await self.invoke(
            raw.functions.messages.HideChatJoinRequest(
                peer=await self.resolve_peer(chat_id),
                user_id=await self.resolve_peer(user_id),
                approved=False
            )
        )

        return True
