#ZEUS- I START FROM THRE, WHERE EVERYONE GIVE-UP

from typing import Union

import zeuspy
from zeuspy import raw


class UnblockUser:
    async def unblock_user(
        self: "zeuspy.Client",
        user_id: Union[int, str]
    ) -> bool:
        """Unblock a user.

        Parameters:
            user_id (``int`` | ``str``)::
                Unique identifier (int) or username (str) of the target user.
                For you yourself you can simply use "me" or "self".
                For a contact that exists in your Telegram address book you can use his phone number (str).

        Returns:
            ``bool``: True on success

        Example:
            .. code-block:: python

                await app.unblock_user(user_id)
        """
        return bool(
            await self.invoke(
                raw.functions.contacts.Unblock(
                    id=await self.resolve_peer(user_id)
                )
            )
        )
