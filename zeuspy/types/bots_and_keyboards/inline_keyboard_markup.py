#ZEUS- I START FROM THRE, WHERE EVERYONE GIVE-UP

from typing import List

import zeuspy
from zeuspy import raw
from zeuspy import types
from ..object import Object


class InlineKeyboardMarkup(Object):
    """An inline keyboard that appears right next to the message it belongs to.

    Parameters:
        inline_keyboard (List of List of :obj:`~zeuspy.types.InlineKeyboardButton`):
            List of button rows, each represented by a List of InlineKeyboardButton objects.
    """

    def __init__(self, inline_keyboard: List[List["types.InlineKeyboardButton"]]):
        super().__init__()

        self.inline_keyboard = inline_keyboard

    @staticmethod
    def read(o):
        inline_keyboard = []

        for i in o.rows:
            row = []

            for j in i.buttons:
                row.append(types.InlineKeyboardButton.read(j))

            inline_keyboard.append(row)

        return InlineKeyboardMarkup(
            inline_keyboard=inline_keyboard
        )

    async def write(self, client: "zeuspy.Client"):
        rows = []

        for r in self.inline_keyboard:
            buttons = []

            for b in r:
                buttons.append(await b.write(client))

            rows.append(raw.types.KeyboardButtonRow(buttons=buttons))

        return raw.types.ReplyInlineMarkup(rows=rows)

        # There seems to be a Python issues with nested async comprehensions.
        # See: https://bugs.python.org/issue33346
        #
        # return raw.types.ReplyInlineMarkup(
        #     rows=[raw.types.KeyboardButtonRow(
        #         buttons=[await j.write(client) for j in i]
        #     ) for i in self.inline_keyboard]
        # )
