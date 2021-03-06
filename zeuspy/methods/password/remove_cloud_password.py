#ZEUS- I START FROM THRE, WHERE EVERYONE GIVE-UP

import zeuspy
from zeuspy import raw
from zeuspy.utils import compute_password_check


class RemoveCloudPassword:
    async def remove_cloud_password(
        self: "zeuspy.Client",
        password: str
    ) -> bool:
        """Turn off the Two-Step Verification security feature (Cloud Password) on your account.

        Parameters:
            password (``str``):
                Your current password.

        Returns:
            ``bool``: True on success.

        Raises:
            ValueError: In case there is no cloud password to remove.

        Example:
            .. code-block:: python

                await app.remove_cloud_password("password")
        """
        r = await self.invoke(raw.functions.account.GetPassword())

        if not r.has_password:
            raise ValueError("There is no cloud password to remove")

        await self.invoke(
            raw.functions.account.UpdatePasswordSettings(
                password=compute_password_check(r, password),
                new_settings=raw.types.account.PasswordInputSettings(
                    new_algo=raw.types.PasswordKdfAlgoUnknown(),
                    new_password_hash=b"",
                    hint=""
                )
            )
        )

        return True
