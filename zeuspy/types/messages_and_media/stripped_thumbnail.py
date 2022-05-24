#ZEUS- I START FROM THRE, WHERE EVERYONE GIVE-UP

import zeuspy
from zeuspy import raw
from ..object import Object


class StrippedThumbnail(Object):
    """A stripped thumbnail

    Parameters:
        data (``bytes``):
            Thumbnail data
    """

    def __init__(
        self,
        *,
        client: "zeuspy.Client" = None,
        data: bytes
    ):
        super().__init__(client)

        self.data = data

    @staticmethod
    def _parse(client, stripped_thumbnail: "raw.types.PhotoStrippedSize") -> "StrippedThumbnail":
        return StrippedThumbnail(
            data=stripped_thumbnail.bytes,
            client=client
        )
