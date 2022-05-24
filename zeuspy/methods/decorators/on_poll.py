#ZEUS- I START FROM THRE, WHERE EVERYONE GIVE-UP

from typing import Callable

import zeuspy
from zeuspy.filters import Filter


class OnPoll:
    def on_poll(
        self=None,
        filters=None,
        group: int = 0
    ) -> Callable:
        """Decorator for handling poll updates.

        This does the same thing as :meth:`~zeuspy.Client.add_handler` using the
        :obj:`~zeuspy.handlers.PollHandler`.

        Parameters:
            filters (:obj:`~zeuspy.filters`, *optional*):
                Pass one or more filters to allow only a subset of polls to be passed
                in your function.

            group (``int``, *optional*):
                The group identifier, defaults to 0.
        """

        def decorator(func: Callable) -> Callable:
            if isinstance(self, zeuspy.Client):
                self.add_handler(zeuspy.handlers.PollHandler(func, filters), group)
            elif isinstance(self, Filter) or self is None:
                if not hasattr(func, "handlers"):
                    func.handlers = []

                func.handlers.append(
                    (
                        zeuspy.handlers.PollHandler(func, self),
                        group if filters is None else filters
                    )
                )

            return func

        return decorator
