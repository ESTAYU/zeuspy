#ZEUS- I START FROM THRE, WHERE EVERYONE GIVE-UP

from typing import Union, Optional

import zeuspy
from zeuspy import raw


class SetChatUsername:
    async def set_chat_username(
        self: "zeuspy.Client",
        chat_id: Union[int, str],
        username: Optional[str]
    ) -> bool:
        """Set a channel or a supergroup username.

        To set your own username (for users only, not bots) you can use :meth:`~zeuspy.Client.set_username`.

        Parameters:
            chat_id (``int`` | ``str``)
                Unique identifier (int) or username (str) of the target chat.

            username (``str`` | ``None``):
                Username to set. Pass "" (empty string) or None to remove the username.

        Returns:
            ``bool``: True on success.

        Raises:
            ValueError: In case a chat id belongs to a user or chat.

        Example:
            .. code-block:: python

                await app.set_chat_username(chat_id, "new_username")
        """

        peer = await self.resolve_peer(chat_id)

        if isinstance(peer, raw.types.InputPeerChannel):
            return bool(
                await self.invoke(
                    raw.functions.channels.UpdateUsername(
                        channel=peer,
                        username=username or ""
                    )
                )
            )
        else:
            raise ValueError(f'The chat_id "{chat_id}" belongs to a user or chat')
