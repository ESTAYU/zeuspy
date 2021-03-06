#ZEUS- I START FROM THRE, WHERE EVERYONE GIVE-UP

import zeuspy
from ..object import Object


class Reaction(Object):
    """Contains information about a reaction.

    Parameters:
        emoji (``str``):
            Reaction emoji.

        count (``int``):
            Reaction count.

        chosen (``bool``):
            Whether this is the chosen reaction.
    """

    def __init__(
        self,
        *,
        client: "zeuspy.Client" = None,
        emoji: str,
        count: int,
        chosen: bool
    ):
        super().__init__(client)

        self.emoji = emoji
        self.count = count
        self.chosen = chosen
