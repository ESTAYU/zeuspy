#ZEUS- I START FROM THRE, WHERE EVERYONE GIVE-UP

from uuid import uuid4

import zeuspy
from zeuspy import types
from ..object import Object


class InlineQueryResult(Object):
    """One result of an inline query.

    - :obj:`~zeuspy.types.InlineQueryResultCachedAudio`
    - :obj:`~zeuspy.types.InlineQueryResultCachedDocument`
    - :obj:`~zeuspy.types.InlineQueryResultCachedAnimation`
    - :obj:`~zeuspy.types.InlineQueryResultCachedPhoto`
    - :obj:`~zeuspy.types.InlineQueryResultCachedSticker`
    - :obj:`~zeuspy.types.InlineQueryResultCachedVideo`
    - :obj:`~zeuspy.types.InlineQueryResultCachedVoice`
    - :obj:`~zeuspy.types.InlineQueryResultArticle`
    - :obj:`~zeuspy.types.InlineQueryResultAudio`
    - :obj:`~zeuspy.types.InlineQueryResultContact`
    - :obj:`~zeuspy.types.InlineQueryResultDocument`
    - :obj:`~zeuspy.types.InlineQueryResultAnimation`
    - :obj:`~zeuspy.types.InlineQueryResultLocation`
    - :obj:`~zeuspy.types.InlineQueryResultPhoto`
    - :obj:`~zeuspy.types.InlineQueryResultVenue`
    - :obj:`~zeuspy.types.InlineQueryResultVideo`
    - :obj:`~zeuspy.types.InlineQueryResultVoice`
    """

    def __init__(
        self,
        type: str,
        id: str,
        input_message_content: "types.InputMessageContent",
        reply_markup: "types.InlineKeyboardMarkup"
    ):
        super().__init__()

        self.type = type
        self.id = str(uuid4()) if id is None else str(id)
        self.input_message_content = input_message_content
        self.reply_markup = reply_markup

    async def write(self, client: "zeuspy.Client"):
        pass
