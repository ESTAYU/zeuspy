#ZEUS- I START FROM THRE, WHERE EVERYONE GIVE-UP

import zeuspy
from zeuspy import raw
from .bot_command_scope import BotCommandScope


class BotCommandScopeAllPrivateChats(BotCommandScope):
    """Represents the scope of bot commands, covering all private chats.
    """

    def __init__(self):
        super().__init__("all_private_chats")

    async def write(self, client: "zeuspy.Client") -> "raw.base.BotCommandScope":
        return raw.types.BotCommandScopeUsers()
