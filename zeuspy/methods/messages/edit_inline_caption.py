#ZEUS- I START FROM THRE, WHERE EVERYONE GIVE-UP

from typing import Optional

import zeuspy
from zeuspy import types, enums


class EditInlineCaption:
    async def edit_inline_caption(
        self: "zeuspy.Client",
        inline_message_id: str,
        caption: str,
        parse_mode: Optional["enums.ParseMode"] = None,
        reply_markup: "types.InlineKeyboardMarkup" = None
    ) -> bool:
        """Edit the caption of inline media messages.

        Parameters:
            inline_message_id (``str``):
                Identifier of the inline message.

            caption (``str``):
                New caption of the media message.

            parse_mode (:obj:`~zeuspy.enums.ParseMode`, *optional*):
                By default, texts are parsed using both Markdown and HTML styles.
                You can combine both syntaxes together.

            reply_markup (:obj:`~zeuspy.types.InlineKeyboardMarkup`, *optional*):
                An InlineKeyboardMarkup object.

        Returns:
            ``bool``: On success, True is returned.

        Example:
            .. code-block:: python

                # Bots only
                await app.edit_inline_caption(inline_message_id, "new media caption")
        """
        return await self.edit_inline_text(
            inline_message_id=inline_message_id,
            text=caption,
            parse_mode=parse_mode,
            reply_markup=reply_markup
        )
