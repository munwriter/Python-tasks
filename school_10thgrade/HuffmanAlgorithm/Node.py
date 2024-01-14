from typing import TypeVar

T = TypeVar("T", bound="Node")


class Node:
    def __init__(self, char: str, freq: int) -> None:
        self.char = char
        self.freq = freq

    def __lt__(self, other: T) -> bool:
        return self.freq < other.freq or (
            self.freq == other.freq and not self.char < other.char
        )

    def __gt__(self, other: T) -> bool:
        return self.freq > other.freq or (
            self.freq == other.freq and self.char < other.char
        )

    def __str__(self) -> str:
        return f"{self.char}: {self.freq}"

    def __repr__(self) -> str:
        return f"Node(char={self.char}, freq={self.freq})"
