from pathlib import Path
from typing import Literal

from coordinates import Coordinates, LetterCoordinates


class NavalBattle:
    def __init__(self, path: str | Path, coordinates_system: Coordinates) -> None:
        self.battlefield = self._load_field(path)
        self.__Cords = coordinates_system
        self.flotilla = self._define_ships_positions(self.battlefield)

    def _load_field(self, path: str | Path) -> list[list[int]]:
        field = []
        with open(path, "tr") as f:
            for line in f:
                formatted_line = list(map(int, line.strip()))
                field.append(formatted_line)

        return field

    def _define_ships_positions(self, battlefield):
        # TODO find more optimized way
        CRITICAL_COORDS = (0, 9)  # TODO Enums maybe
        ship = None
        flotilla = []
        # traverse horizontally
        for row in range(10):
            for col in range(10):
                if battlefield[row][col] == 1:
                    # Checking for vertical ship
                    if row != CRITICAL_COORDS[0]:
                        if battlefield[row - 1][col] == 1:
                            continue
                    if row != CRITICAL_COORDS[1]:
                        if battlefield[row + 1][col] == 1:
                            continue
                    battlefield[row][col] = 0
                    if ship is None:
                        ship = [self.__Cords(row, col)]
                    else:
                        ship.append(self.__Cords(row, col))
                    if col != CRITICAL_COORDS[1]:
                        if battlefield[row][col + 1] == 0:
                            flotilla.append(ship)
                            ship = None
                    else:
                        flotilla.append(ship)
                        ship = None
        # traverse vertically
        ship = None

        for col in range(10):
            for row in range(10):
                if battlefield[row][col] == 1:
                    if ship is None:
                        ship = [self.__Cords(row, col)]
                    else:
                        ship.append(self.__Cords(row, col))
                    if row != CRITICAL_COORDS[1]:
                        if battlefield[row + 1][col] == 0:
                            flotilla.append(ship)
                            ship = None
                    else:
                        flotilla.append(ship)
                        ship = None
        return flotilla

    def strike(
        self, x_position: int, y_position: int
    ) -> Literal["hurt", "eliminate", "miss"]:
        ...


a = NavalBattle(r"school_10thgrade\NavalBattle\battlefield.txt", LetterCoordinates)
print(a.flotilla)
