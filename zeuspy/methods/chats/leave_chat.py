#ZEUS- I START FROM THRE, WHERE EVERYONE GIVE-UP

from typing import Union

import zeuspy
from zeuspy import raw


class LeaveChat:
    async def leave_chat(
        self: "zeuspy.Client",
        chat_id: Union[int, str],
        delete: bool = False
    ):
        """Leave a group chat or channel.

        Parameters:
            chat_id (``int`` | ``str``):
                Unique identifier for the target chat or username of the target channel/supergroup
                (in the format @username).

            delete (``bool``, *optional*):
                Deletes the group chat dialog after leaving (for simple group chats, not supergroups).
                Defaults to False.

        Example:
            .. code-block:: python

                # Leave chat or channel
                await app.leave_chat(chat_id)

                # Leave basic chat and also delete the dialog
                await app.leave_chat(chat_id, delete=True)
        """
        peer = await self.resolve_peer(chat_id)

        if isinstance(peer, raw.types.InputPeerChannel):
            return await self.invoke(
                raw.functions.channels.LeaveChannel(
                    channel=await self.resolve_peer(chat_id)
                )
            )
        elif isinstance(peer, raw.types.InputPeerChat):
            r = await self.invoke(
                raw.functions.messages.DeleteChatUser(
                    chat_id=peer.chat_id,
                    user_id=raw.types.InputUserSelf()
                )
            )

            if delete:
                await self.invoke(
                    raw.functions.messages.DeleteHistory(
                        peer=peer,
                        max_id=0
                    )
                )

            return r
