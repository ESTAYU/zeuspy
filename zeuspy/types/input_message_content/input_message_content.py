#ZEUS- I START FROM THRE, WHERE EVERYONE GIVE-UP

import zeuspy

from ..object import Object

"""- :obj:`~zeuspy.types.InputLocationMessageContent`
    - :obj:`~zeuspy.types.InputVenueMessageContent`
    - :obj:`~zeuspy.types.InputContactMessageContent`"""


class InputMessageContent(Object):
    """Content of a message to be sent as a result of an inline query.

    zeuspy currently supports the following types:

    - :obj:`~zeuspy.types.InputTextMessageContent`
    """

    def __init__(self):
        super().__init__()

    async def write(self, client: "zeuspy.Client", reply_markup):
        raise NotImplementedError
