#ZEUS- I START FROM THRE, WHERE EVERYONE GIVE-UP

from .object import Object


class List(list):
    __slots__ = []

    def __str__(self):
        # noinspection PyCallByClass
        return Object.__str__(self)

    def __repr__(self):
        return f"zeuspy.types.List([{','.join(Object.__repr__(i) for i in self)}])"
