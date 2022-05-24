#ZEUS- I START FROM THRE, WHERE EVERYONE GIVE-UP

import logging

import zeuspy
from zeuspy import raw
from zeuspy.raw.core import TLObject
from zeuspy.session import Session

log = logging.getLogger(__name__)


class Invoke:
    async def invoke(
        self: "zeuspy.Client",
        query: TLObject,
        retries: int = Session.MAX_RETRIES,
        timeout: float = Session.WAIT_TIMEOUT,
        sleep_threshold: float = None
    ):
        """Invoke raw Telegram functions.

        This method makes it possible to manually call every single Telegram API method in a low-level manner.
        Available functions are listed in the :obj:`functions <zeuspy.api.functions>` package and may accept compound
        data types from :obj:`types <zeuspy.api.types>` as well as bare types such as ``int``, ``str``, etc...

        .. note::

            This is a utility method intended to be used **only** when working with raw
            :obj:`functions <zeuspy.api.functions>` (i.e: a Telegram API method you wish to use which is not
            available yet in the Client class as an easy-to-use method).

        Parameters:
            query (``RawFunction``):
                The API Schema function filled with proper arguments.

            retries (``int``):
                Number of retries.

            timeout (``float``):
                Timeout in seconds.

            sleep_threshold (``float``):
                Sleep threshold in seconds.

        Returns:
            ``RawType``: The raw type response generated by the query.

        Raises:
            RPCError: In case of a Telegram RPC error.
        """
        if not self.is_connected:
            raise ConnectionError("Client has not been started yet")

        if self.no_updates:
            query = raw.functions.InvokeWithoutUpdates(query=query)

        if self.takeout_id:
            query = raw.functions.InvokeWithTakeout(takeout_id=self.takeout_id, query=query)

        r = await self.session.invoke(
            query, retries, timeout,
            (sleep_threshold
             if sleep_threshold is not None
             else self.sleep_threshold)
        )

        await self.fetch_peers(getattr(r, "users", []))
        await self.fetch_peers(getattr(r, "chats", []))

        return r