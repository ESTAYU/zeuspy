#ZEUS- I START FROM THRE, WHERE EVERYONE GIVE-UP

class Client:
    def __init__(self):
        self.username = "username"

    async def get_me(self):
        return User(self.username)


class User:
    def __init__(self, username: str = None):
        self.username = username


class Message:
    def __init__(self, text: str = None, caption: str = None):
        self.text = text
        self.caption = caption
        self.command = None
