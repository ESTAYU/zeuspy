#ZEUS- I START FROM THRE, WHERE EVERYONE GIVE-UP

import logging
from typing import List

import zeuspy
from zeuspy import raw
from zeuspy import types

log = logging.getLogger(__name__)


class GetContacts:
    async def get_contacts(
        self: "zeuspy.Client"
    ) -> List["types.User"]:
        """Get contacts from your Telegram address book.

        Returns:
            List of :obj:`~zeuspy.types.User`: On success, a list of users is returned.

        Example:
            .. code-block:: python

                contacts = await app.get_contacts()
                print(contacts)
        """
        contacts = await self.invoke(raw.functions.contacts.GetContacts(hash=0))
        return types.List(types.User._parse(self, user) for user in contacts.users)
