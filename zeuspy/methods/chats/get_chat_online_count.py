#ZEUS- I START FROM THRE, WHERE EVERYONE GIVE-UP

from typing import Union

import zeuspy
from zeuspy import raw


class GetChatOnlineCount:
    async def get_chat_online_count(
        self: "zeuspy.Client",
        chat_id: Union[int, str]
    ) -> int:
        """Get the number of members that are currently online in a chat.

        Parameters:
            chat_id (``int`` | ``str``):
                Unique identifier (int) or username (str) of the target chat.

        Returns:
            ``int``: On success, the chat members online count is returned.

        Example:
            .. code-block:: python

                online = await app.get_chat_online_count(chat_id)
                print(online)
        """
        return (await self.invoke(
            raw.functions.messages.GetOnlines(
                peer=await self.resolve_peer(chat_id)
            )
        )).onlines
