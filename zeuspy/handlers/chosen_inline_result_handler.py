#ZEUS- I START FROM THRE, WHERE EVERYONE GIVE-UP

from typing import Callable

from .handler import Handler


class ChosenInlineResultHandler(Handler):
    """The ChosenInlineResultHandler handler class. Used to handle chosen inline results coming from inline queries.
    It is intended to be used with :meth:`~zeuspy.Client.add_handler`

    For a nicer way to register this handler, have a look at the
    :meth:`~zeuspy.Client.on_chosen_inline_result` decorator.

    Parameters:
        callback (``Callable``):
            Pass a function that will be called when a new chosen inline result arrives.
            It takes *(client, chosen_inline_result)* as positional arguments (look at the section below for a
            detailed description).

        filters (:obj:`Filters`):
            Pass one or more filters to allow only a subset of chosen inline results to be passed
            in your callback function.

    Other parameters:
        client (:obj:`~zeuspy.Client`):
            The Client itself, useful when you want to call other API methods inside the message handler.

        chosen_inline_result (:obj:`~zeuspy.types.ChosenInlineResult`):
            The received chosen inline result.
    """

    def __init__(self, callback: Callable, filters=None):
        super().__init__(callback, filters)
