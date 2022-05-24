#ZEUS- I START FROM THRE, WHERE EVERYONE GIVE-UP

from .change_cloud_password import ChangeCloudPassword
from .enable_cloud_password import EnableCloudPassword
from .remove_cloud_password import RemoveCloudPassword


class Password(
    RemoveCloudPassword,
    ChangeCloudPassword,
    EnableCloudPassword
):
    pass
