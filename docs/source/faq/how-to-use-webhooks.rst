How to use webhooks?
====================

There is no webhook in zeuspy, simply because there is no HTTP involved. However, a similar technique is
being used to make receiving updates efficient.

zeuspy uses persistent connections via TCP sockets to interact with the server and instead of actively asking for
updates every time (polling), zeuspy will sit down and wait for the server to send updates by itself the very moment
they are available (server push).
