from __future__ import annotations

from typing import Protocol

NUMS_TO_LETTERS = {
    0: "а",
    1: "б",
    2: "в",
    3: "г",
    4: "д",
    5: "е",
    6: "ж",
    7: "з",
    8: "и",
    9: "к",
}


class Coordinates(Protocol):
    x: int
    y: int | str

    @property
    def coordinates(self):
        return f"{self.y}{self.x}"

    def __eq__(self, other: Coordinates) -> bool:
        return self.coordinates == other.coordinates

    def __str__(self) -> str:
        return self.coordinates

    def __repr__(self) -> str:
        return f"(x={self.x}, y={self.y})"


class LetterCoordinates(Coordinates):
    def __init__(self, x: int, y: int | str) -> None:
        self.x = x + 1
        if isinstance(y, int):
            self.y = NUMS_TO_LETTERS[y]
        else:
            self.y = y


class NumCoordinates(Coordinates):
    def __init__(self, x: int, y: int | str) -> None:
        self.x = x + 1
        self.y = y + 1
