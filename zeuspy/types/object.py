#ZEUS- I START FROM THRE, WHERE EVERYONE GIVE-UP

import typing
from datetime import datetime
from enum import Enum
from json import dumps

import zeuspy


class Object:
    def __init__(self, client: "zeuspy.Client" = None):
        self._client = client

    def bind(self, client: "zeuspy.Client"):
        """Bind a Client instance to this and to all nested zeuspy objects.

        Parameters:
            client (:obj:`~zeuspy.types.Client`):
                The Client instance to bind this object with. Useful to re-enable bound methods after serializing and
                deserializing zeuspy objects with ``repr`` and ``eval``.
        """
        self._client = client

        for i in self.__dict__:
            o = getattr(self, i)

            if isinstance(o, Object):
                o.bind(client)

    @staticmethod
    def default(obj: "Object"):
        if isinstance(obj, bytes):
            return repr(obj)

        # https://t.me/zeuspychat/167281
        # Instead of re.Match, which breaks for python <=3.6
        if isinstance(obj, typing.Match):
            return repr(obj)

        if isinstance(obj, Enum):
            return str(obj)

        if isinstance(obj, datetime):
            return str(obj)

        return {
            "_": obj.__class__.__name__,
            **{
                attr: (
                    "*" * 9 if attr == "phone_number" else
                    getattr(obj, attr)
                )
                for attr in filter(lambda x: not x.startswith("_"), obj.__dict__)
                if getattr(obj, attr) is not None
            }
        }

    def __str__(self) -> str:
        return dumps(self, indent=4, default=Object.default, ensure_ascii=False)

    def __repr__(self) -> str:
        return "zeuspy.types.{}({})".format(
            self.__class__.__name__,
            ", ".join(
                f"{attr}={repr(getattr(self, attr))}"
                for attr in filter(lambda x: not x.startswith("_"), self.__dict__)
                if getattr(self, attr) is not None
            )
        )

    def __eq__(self, other: "Object") -> bool:
        for attr in self.__dict__:
            try:
                if attr.startswith("_"):
                    continue

                if getattr(self, attr) != getattr(other, attr):
                    return False
            except AttributeError:
                return False

        return True

    def __getstate__(self):
        new_dict = self.__dict__.copy()
        new_dict.pop("_client", None)
        return new_dict
