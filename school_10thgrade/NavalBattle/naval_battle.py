from pathlib import Path
from typing import Literal




class NavalBattle:
    def __init__(self, path: str | Path) -> None:
        self.battlefield = self._load_field(path)

    def _load_field(self, path: str | Path) -> list[list[int]]:
        field = []
        with open(path, "tr") as f:
            for line in f:
                formatted_line = list(map(int, line.strip()))
                field.append(formatted_line)

        return field

    def strike(self, x_position: int, y_position: int) -> Literal["hurt", "eliminate", "miss"]:
        ...
        

a = NavalBattle(r"school_10thgrade\NavalBattle\battlefield.txt")
print(a._load_field(r"school_10thgrade\NavalBattle\battlefield.txt"))
