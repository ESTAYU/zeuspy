#ZEUS- I START FROM THRE, WHERE EVERYONE GIVE-UP

import zeuspy
from zeuspy.handlers import DisconnectHandler
from zeuspy.handlers.handler import Handler


class AddHandler:
    def add_handler(
        self: "zeuspy.Client",
        handler: "Handler",
        group: int = 0
    ):
        """Register an update handler.

        You can register multiple handlers, but at most one handler within a group will be used for a single update.
        To handle the same update more than once, register your handler using a different group id (lower group id
        == higher priority). This mechanism is explained in greater details at
        :doc:`More on Updates <../../topics/more-on-updates>`.

        Parameters:
            handler (``Handler``):
                The handler to be registered.

            group (``int``, *optional*):
                The group identifier, defaults to 0.

        Returns:
            ``tuple``: A tuple consisting of *(handler, group)*.

        Example:
            .. code-block:: python

                from zeuspy import Client
                from zeuspy.handlers import MessageHandler

                async def hello(client, message):
                    print(message)

                app = Client("my_account")

                app.add_handler(MessageHandler(hello))

                app.run()
        """
        if isinstance(handler, DisconnectHandler):
            self.disconnect_handler = handler.callback
        else:
            self.dispatcher.add_handler(handler, group)

        return handler, group
