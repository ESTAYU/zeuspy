#ZEUS- I START FROM THRE, WHERE EVERYONE GIVE-UP

from typing import Callable

import zeuspy


class OnDisconnect:
    def on_disconnect(self=None) -> Callable:
        """Decorator for handling disconnections.

        This does the same thing as :meth:`~zeuspy.Client.add_handler` using the
        :obj:`~zeuspy.handlers.DisconnectHandler`.
        """

        def decorator(func: Callable) -> Callable:
            if isinstance(self, zeuspy.Client):
                self.add_handler(zeuspy.handlers.DisconnectHandler(func))

            return func

        return decorator
