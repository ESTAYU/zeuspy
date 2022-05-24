#ZEUS- I START FROM THRE, WHERE EVERYONE GIVE-UP

from typing import Union

import zeuspy
from zeuspy import raw
from zeuspy import types


class SetChatMenuButton:
    async def set_chat_menu_button(
        self: "zeuspy.Client",
        chat_id: Union[int, str] = None,
        menu_button: "types.MenuButton" = None
    ) -> bool:
        """Change the bot's menu button in a private chat, or the default menu button.

        Parameters:
            chat_id (``int`` | ``str``, *optional*):
                Unique identifier (int) or username (str) of the target chat.
                If not specified, default bot's menu button will be changed.

            menu_button (:obj:`~zeuspy.types.MenuButton`, *optional*):
                The new bot's menu button.
                Defaults to :obj:`~zeuspy.types.MenuButtonDefault`.
        """

        await self.invoke(
            raw.functions.bots.SetBotMenuButton(
                user_id=await self.resolve_peer(chat_id or "me"),
                button=(
                    (await menu_button.write(self)) if menu_button
                    else (await types.MenuButtonDefault().write(self))
                )
            )
        )

        return True
