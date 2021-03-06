#ZEUS- I START FROM THRE, WHERE EVERYONE GIVE-UP

from .block_user import BlockUser
from .delete_profile_photos import DeleteProfilePhotos
from .get_chat_photos import GetChatPhotos
from .get_chat_photos_count import GetChatPhotosCount
from .get_common_chats import GetCommonChats
from .get_me import GetMe
from .get_users import GetUsers
from .set_profile_photo import SetProfilePhoto
from .set_username import SetUsername
from .unblock_user import UnblockUser
from .update_profile import UpdateProfile


class Users(
    BlockUser,
    GetCommonChats,
    GetChatPhotos,
    SetProfilePhoto,
    DeleteProfilePhotos,
    GetUsers,
    GetMe,
    SetUsername,
    GetChatPhotosCount,
    UnblockUser,
    UpdateProfile,
):
    pass
