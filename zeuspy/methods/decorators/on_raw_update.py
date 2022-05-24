#ZEUS- I START FROM THRE, WHERE EVERYONE GIVE-UP

from typing import Callable

import zeuspy


class OnRawUpdate:
    def on_raw_update(
        self=None,
        group: int = 0
    ) -> Callable:
        """Decorator for handling raw updates.

        This does the same thing as :meth:`~zeuspy.Client.add_handler` using the
        :obj:`~zeuspy.handlers.RawUpdateHandler`.

        Parameters:
            group (``int``, *optional*):
                The group identifier, defaults to 0.
        """

        def decorator(func: Callable) -> Callable:
            if isinstance(self, zeuspy.Client):
                self.add_handler(zeuspy.handlers.RawUpdateHandler(func), group)
            else:
                if not hasattr(func, "handlers"):
                    func.handlers = []

                func.handlers.append(
                    (
                        zeuspy.handlers.RawUpdateHandler(func),
                        group if self is None else group
                    )
                )

            return func

        return decorator
