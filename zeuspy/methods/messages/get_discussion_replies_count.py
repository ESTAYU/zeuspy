#ZEUS- I START FROM THRE, WHERE EVERYONE GIVE-UP

from typing import Union

import zeuspy
from zeuspy import raw


class GetDiscussionRepliesCount:
    async def get_discussion_replies_count(
        self: "zeuspy.Client",
        chat_id: Union[int, str],
        message_id: int,
    ) -> int:
        """Get the total count of replies in a discussion thread.

        Parameters:
            chat_id (``int`` | ``str``):
                Unique identifier (int) or username (str) of the target chat.

            message_id (``int``):
                Message id.

        Example:
            .. code-block:: python

                count = await app.get_discussion_replies_count(chat_id, message_id)
        """

        r = await self.invoke(
            raw.functions.messages.GetReplies(
                peer=await self.resolve_peer(chat_id),
                msg_id=message_id,
                offset_id=0,
                offset_date=0,
                add_offset=0,
                limit=1,
                max_id=0,
                min_id=0,
                hash=0
            )
        )

        return r.count
