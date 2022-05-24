#ZEUS- I START FROM THRE, WHERE EVERYONE GIVE-UP

from enum import Enum


class AutoName(Enum):
    def _generate_next_value_(self, *args):
        return self.lower()

    def __repr__(self):
        return f"zeuspy.enums.{self}"
