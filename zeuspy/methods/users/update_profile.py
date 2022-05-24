#ZEUS- I START FROM THRE, WHERE EVERYONE GIVE-UP

import zeuspy
from zeuspy import raw


class UpdateProfile:
    async def update_profile(
        self: "zeuspy.Client",
        first_name: str = None,
        last_name: str = None,
        bio: str = None
    ) -> bool:
        """Update your profile details such as first name, last name and bio.

        You can omit the parameters you don't want to change.

        Parameters:
            first_name (``str``, *optional*):
                The new first name.

            last_name (``str``, *optional*):
                The new last name.
                Pass "" (empty string) to remove it.

            bio (``str``, *optional*):
                The new bio, also known as "about". Max 70 characters.
                Pass "" (empty string) to remove it.

        Returns:
            ``bool``: True on success.

        Example:
            .. code-block:: python

                # Update your first name only
                await app.update_profile(first_name="zeuspy")

                # Update first name and bio
                await app.update_profile(first_name="zeuspy", bio="https://docs.zeuspy.org/")

                # Remove the last name
                await app.update_profile(last_name="")
        """

        return bool(
            await self.invoke(
                raw.functions.account.UpdateProfile(
                    first_name=first_name,
                    last_name=last_name,
                    about=bio
                )
            )
        )
