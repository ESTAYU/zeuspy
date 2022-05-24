#ZEUS- I START FROM THRE, WHERE EVERYONE GIVE-UP

import zeuspy
from zeuspy import raw
from zeuspy import types


class GetMe:
    async def get_me(
        self: "zeuspy.Client"
    ) -> "types.User":
        """Get your own user identity.

        Returns:
            :obj:`~zeuspy.types.User`: Information about the own logged in user/bot.

        Example:
            .. code-block:: python

                me = await app.get_me()
                print(me)
        """
        r = await self.invoke(
            raw.functions.users.GetFullUser(
                id=raw.types.InputUserSelf()
            )
        )

        users = {u.id: u for u in r.users}

        return types.User._parse(self, users[r.full_user.id])
