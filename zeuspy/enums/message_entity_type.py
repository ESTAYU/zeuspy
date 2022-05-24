#ZEUS- I START FROM THRE, WHERE EVERYONE GIVE-UP

from zeuspy import raw
from .auto_name import AutoName


class MessageEntityType(AutoName):
    """Message entity type enumeration used in :obj:`~zeuspy.types.MessageEntity`."""

    MENTION = raw.types.MessageEntityMention
    "``@username``"

    HASHTAG = raw.types.MessageEntityHashtag
    "``#hashtag``"

    CASHTAG = raw.types.MessageEntityCashtag
    "``$USD``"

    BOT_COMMAND = raw.types.MessageEntityBotCommand
    "``/start@zeuspybot``"

    URL = raw.types.MessageEntityUrl
    "``https://zeuspy.org`` (see ``url``)"

    EMAIL = raw.types.MessageEntityEmail
    "``do-not-reply@zeuspy.org``"

    PHONE_NUMBER = raw.types.MessageEntityPhone
    "``+1-123-456-7890``"

    BOLD = raw.types.MessageEntityBold
    "Bold text"

    ITALIC = raw.types.MessageEntityItalic
    "Italic text"

    UNDERLINE = raw.types.MessageEntityUnderline
    "Underlined text"

    STRIKETHROUGH = raw.types.MessageEntityStrike
    "Strikethrough text"

    SPOILER = raw.types.MessageEntitySpoiler
    "Spoiler text"

    CODE = raw.types.MessageEntityCode
    "Monowidth string"

    PRE = raw.types.MessageEntityPre
    "Monowidth block (see ``language``)"

    BLOCKQUOTE = raw.types.MessageEntityBlockquote
    "Blockquote text"

    TEXT_LINK = raw.types.MessageEntityTextUrl
    "For clickable text URLs"

    TEXT_MENTION = raw.types.MessageEntityMentionName
    "for users without usernames (see ``user``)"

    BANK_CARD = raw.types.MessageEntityBankCard
    "Bank card text"

    UNKNOWN = raw.types.MessageEntityUnknown
    "Unknown message entity type"
