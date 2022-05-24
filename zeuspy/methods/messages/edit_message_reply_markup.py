#ZEUS- I START FROM THRE, WHERE EVERYONE GIVE-UP

from typing import Union

import zeuspy
from zeuspy import raw
from zeuspy import types


class EditMessageReplyMarkup:
    async def edit_message_reply_markup(
        self: "zeuspy.Client",
        chat_id: Union[int, str],
        message_id: int,
        reply_markup: "types.InlineKeyboardMarkup" = None,
    ) -> "types.Message":
        """Edit only the reply markup of messages sent by the bot.

        Parameters:
            chat_id (``int`` | ``str``):
                Unique identifier (int) or username (str) of the target chat.
                For your personal cloud (Saved Messages) you can simply use "me" or "self".
                For a contact that exists in your Telegram address book you can use his phone number (str).

            message_id (``int``):
                Message identifier in the chat specified in chat_id.

            reply_markup (:obj:`~zeuspy.types.InlineKeyboardMarkup`, *optional*):
                An InlineKeyboardMarkup object.

        Returns:
            :obj:`~zeuspy.types.Message`: On success, the edited message is returned.

        Example:
            .. code-block:: python

                from zeuspy.types import InlineKeyboardMarkup, InlineKeyboardButton

                # Bots only
                await app.edit_message_reply_markup(
                    chat_id, message_id,
                    InlineKeyboardMarkup([[
                        InlineKeyboardButton("New button", callback_data="new_data")]]))
        """
        r = await self.invoke(
            raw.functions.messages.EditMessage(
                peer=await self.resolve_peer(chat_id),
                id=message_id,
                reply_markup=await reply_markup.write(self) if reply_markup else None,
            )
        )

        for i in r.updates:
            if isinstance(i, (raw.types.UpdateEditMessage, raw.types.UpdateEditChannelMessage)):
                return await types.Message._parse(
                    self, i.message,
                    {i.id: i for i in r.users},
                    {i.id: i for i in r.chats}
                )
