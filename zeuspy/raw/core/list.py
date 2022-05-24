#ZEUS- I START FROM THRE, WHERE EVERYONE GIVE-UP

from typing import List as TList, Any

from .tl_object import TLObject


class List(TList[Any], TLObject):
    def __repr__(self) -> str:
        return f"zeuspy.raw.core.List([{','.join(TLObject.__repr__(i) for i in self)}])"
