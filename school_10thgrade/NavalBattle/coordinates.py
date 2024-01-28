from typing import Protocol

NUMS_TO_LETTERS = {
    0: "a",
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
    x: int | str
    y: int

    @property
    def coordinates(self):
        return f"{self.x}{self.y}"


class LetterCoordinates(Coordinates):
    def __init__(self, x: int, y: int) -> None:
        self.x = NUMS_TO_LETTERS[x]
        self.y = y + 1

    def __str__(self) -> str:
        return self.coordinates
    
    def __repr__(self) -> str:
        return f"(x={self.x}, y={self.y})"