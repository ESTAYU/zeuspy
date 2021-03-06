#ZEUS- I START FROM THRE, WHERE EVERYONE GIVE-UP

from typing import List, Union

import zeuspy
from zeuspy import raw
from zeuspy import utils
from zeuspy.file_id import FileType


class DeleteProfilePhotos:
    async def delete_profile_photos(
        self: "zeuspy.Client",
        photo_ids: Union[str, List[str]]
    ) -> bool:
        """Delete your own profile photos.

        Parameters:
            photo_ids (``str`` | List of ``str``):
                A single :obj:`~zeuspy.types.Photo` id as string or multiple ids as list of strings for deleting
                more than one photos at once.

        Returns:
            ``bool``: True on success.

        Example:
            .. code-block:: python

                # Get the photos to be deleted
                photos = await app.get_profile_photos("me")

                # Delete one photo
                await app.delete_profile_photos(photos[0].file_id)

                # Delete the rest of the photos
                await app.delete_profile_photos([p.file_id for p in photos[1:]])
        """
        photo_ids = photo_ids if isinstance(photo_ids, list) else [photo_ids]
        input_photos = [utils.get_input_media_from_file_id(i, FileType.PHOTO).id for i in photo_ids]

        return bool(await self.invoke(
            raw.functions.photos.DeletePhotos(
                id=input_photos
            )
        ))
