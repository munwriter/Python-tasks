from dataclasses import dataclass
from typing import TypeVar

T = TypeVar("T", bound="Node")


@dataclass
class Node:
    char: str
    freq: int

    def __gt__(self, other: T) -> bool:
        if self.freq == other.freq:
            if self.char < other.char:
                return True
            else:
                return False
        elif self.freq > other.freq:
            return True
        else:
            return False
