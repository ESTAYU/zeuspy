Decorators
==========

Decorators are able to register callback functions for handling updates in a much easier and cleaner way compared to
:doc:`Handlers <handlers>`; they do so by instantiating the correct handler and calling
:meth:`~zeuspy.Client.add_handler` automatically. All you need to do is adding the decorators on top of your
functions.

.. code-block:: python

    from zeuspy import Client

    app = Client("my_account")


    @app.on_message()
    def log(client, message):
        print(message)


    app.run()

.. contents:: Contents
    :backlinks: none
    :depth: 1
    :local:

-----

.. currentmodule:: zeuspy

Index
-----

.. hlist::
    :columns: 3

    - :meth:`~Client.on_message`
    - :meth:`~Client.on_edited_message`
    - :meth:`~Client.on_callback_query`
    - :meth:`~Client.on_inline_query`
    - :meth:`~Client.on_chosen_inline_result`
    - :meth:`~Client.on_chat_member_updated`
    - :meth:`~Client.on_chat_join_request`
    - :meth:`~Client.on_deleted_messages`
    - :meth:`~Client.on_user_status`
    - :meth:`~Client.on_poll`
    - :meth:`~Client.on_disconnect`
    - :meth:`~Client.on_raw_update`

-----

Details
-------

.. Decorators
.. autodecorator:: zeuspy.Client.on_message()
.. autodecorator:: zeuspy.Client.on_edited_message()
.. autodecorator:: zeuspy.Client.on_callback_query()
.. autodecorator:: zeuspy.Client.on_inline_query()
.. autodecorator:: zeuspy.Client.on_chosen_inline_result()
.. autodecorator:: zeuspy.Client.on_chat_member_updated()
.. autodecorator:: zeuspy.Client.on_chat_join_request()
.. autodecorator:: zeuspy.Client.on_deleted_messages()
.. autodecorator:: zeuspy.Client.on_user_status()
.. autodecorator:: zeuspy.Client.on_poll()
.. autodecorator:: zeuspy.Client.on_disconnect()
.. autodecorator:: zeuspy.Client.on_raw_update()
