#ZEUS- I START FROM THRE, WHERE EVERYONE GIVE-UP

import zeuspy
from ..object import Object


class PollOption(Object):
    """Contains information about one answer option in a poll.

    Parameters:
        text (``str``):
            Option text, 1-100 characters.

        voter_count (``int``):
            Number of users that voted for this option.
            Equals to 0 until you vote.

        data (``bytes``):
            The data this poll option is holding.
    """

    def __init__(
        self,
        *,
        client: "zeuspy.Client" = None,
        text: str,
        voter_count: int,
        data: bytes
    ):
        super().__init__(client)

        self.text = text
        self.voter_count = voter_count
        self.data = data
