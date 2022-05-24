#ZEUS- I START FROM THRE, WHERE EVERYONE GIVE-UP

import asyncio
from typing import List

import zeuspy
from .idle import idle


async def compose(
    clients: List["zeuspy.Client"],
    sequential: bool = False
):
    """Run multiple clients at once.

    This method can be used to run multiple clients at once and can be found directly in the ``zeuspy`` package.

    If you want to run a single client, you can use Client's bound method :meth:`~zeuspy.Client.run`.

    Parameters:
        clients (List of :obj:`~zeuspy.Client`):
            A list of client objects to run.

        sequential (``bool``, *optional*):
            Pass True to run clients sequentially.
            Defaults to False (run clients concurrently)

    Example:
        .. code-block:: python

            import asyncio
            from zeuspy import Client, compose


            async def main():
                app1 = Client("account1")
                app2 = Client("account2")
                app3 = Client("account3")

                ...

                await compose([app1, app2, app3])


            asyncio.run(main())

    """
    if sequential:
        for c in clients:
            await c.start()
    else:
        await asyncio.gather(*[c.start() for c in clients])

    await idle()

    if sequential:
        for c in clients:
            await c.stop()
    else:
        await asyncio.gather(*[c.stop() for c in clients])
