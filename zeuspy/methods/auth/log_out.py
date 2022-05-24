#ZEUS- I START FROM THRE, WHERE EVERYONE GIVE-UP

import logging

import zeuspy
from zeuspy import raw

log = logging.getLogger(__name__)


class LogOut:
    async def log_out(
        self: "zeuspy.Client",
    ):
        """Log out from Telegram and delete the *\\*.session* file.

        When you log out, the current client is stopped and the storage session deleted.
        No more API calls can be made until you start the client and re-authorize again.

        Returns:
            ``bool``: On success, True is returned.

        Example:
            .. code-block:: python

                # Log out.
                app.log_out()
        """
        await self.invoke(raw.functions.auth.LogOut())
        await self.stop()
        await self.storage.delete()

        return True
