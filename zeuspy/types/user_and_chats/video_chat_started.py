#ZEUS- I START FROM THRE, WHERE EVERYONE GIVE-UP

from ..object import Object


class VideoChatStarted(Object):
    """A service message about a voice chat started in the chat.

    Currently holds no information.
    """

    def __init__(self):
        super().__init__()
