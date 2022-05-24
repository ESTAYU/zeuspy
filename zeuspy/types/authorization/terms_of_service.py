#ZEUS- I START FROM THRE, WHERE EVERYONE GIVE-UP

from typing import List

from zeuspy import raw
from zeuspy import types
from ..object import Object


class TermsOfService(Object):
    """Telegram's Terms of Service returned by :meth:`~zeuspy.Client.sign_in`.

    Parameters:
        id (``str``):
            Terms of Service identifier.

        text (``str``):
            Terms of Service text.

        entities (List of :obj:`~zeuspy.types.MessageEntity`):
            Special entities like URLs that appear in the text.
    """

    def __init__(self, *, id: str, text: str, entities: List["types.MessageEntity"]):
        super().__init__()

        self.id = id
        self.text = text
        self.entities = entities

    @staticmethod
    def _parse(terms_of_service: "raw.types.help.TermsOfService") -> "TermsOfService":
        return TermsOfService(
            id=terms_of_service.id.data,
            text=terms_of_service.text,
            entities=[
                types.MessageEntity._parse(None, entity, {})
                for entity in terms_of_service.entities
            ]
        )
