#ZEUS- I START FROM THRE, WHERE EVERYONE GIVE-UP

from zeuspy import raw, enums
from ..object import Object


class SentCode(Object):
    """Contains info on a sent confirmation code.

    Parameters:
        type (:obj:`~zeuspy.enums.SentCodeType`):
            Type of the current sent code.

        phone_code_hash (``str``):
            Confirmation code identifier useful for the next authorization steps (either
            :meth:`~zeuspy.Client.sign_in` or :meth:`~zeuspy.Client.sign_up`).

        next_type (:obj:`~zeuspy.enums.NextCodeType`, *optional*):
            Type of the next code to be sent with :meth:`~zeuspy.Client.resend_code`.

        timeout (``int``, *optional*):
            Delay in seconds before calling :meth:`~zeuspy.Client.resend_code`.
    """

    def __init__(
        self, *,
        type: "enums.SentCodeType",
        phone_code_hash: str,
        next_type: "enums.NextCodeType" = None,
        timeout: int = None
    ):
        super().__init__()

        self.type = type
        self.phone_code_hash = phone_code_hash
        self.next_type = next_type
        self.timeout = timeout

    @staticmethod
    def _parse(sent_code: raw.types.auth.SentCode) -> "SentCode":
        return SentCode(
            type=enums.SentCodeType(type(sent_code.type)),
            phone_code_hash=sent_code.phone_code_hash,
            next_type=enums.NextCodeType(type(sent_code.next_type)) if sent_code.next_type else None,
            timeout=sent_code.timeout
        )
