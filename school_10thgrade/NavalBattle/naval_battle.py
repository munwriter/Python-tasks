from pathlib import Path
from typing import Literal

from coordinates import Coordinates, LetterCoordinates


class NavalBattle:
    def __init__(self, path: str | Path, coordinates_system: Coordinates) -> None:
        self.flotilla: list[Coordinates] = []
        self.battlefield = self._load_field(path)
        self.__Cords = coordinates_system

    def _load_field(self, path: str | Path) -> list[list[int]]:
        field = []
        with open(path, "tr") as f:
            for line in f:
                formatted_line = list(map(int, line.strip()))
                field.append(formatted_line)

        return field

    def _define_ships_positions(self):
        # TODO find more optimized way
        CRITICAL_COORDS = (0, 9)  # TODO Enums maybe
        ship = None
        saved_cords = set()
        # traverse horizontally
        for row in range(10):
            for col in range(10):
                if self.battlefield[row][col] == 1:
                    # Checking for vertical ship
                    if row != CRITICAL_COORDS[0]:
                        if self.battlefield[row - 1][col] == 1:
                            continue
                    if row != CRITICAL_COORDS[1]:
                        if self.battlefield[row + 1][col] == 1:
                            continue
                    if ship is None:
                        ship = [self.__Cords(row, col)]
                        saved_cords.add(self.__Cords(row, col).coordinates)
                    else:
                        ship.append(self.__Cords(row, col))
                        saved_cords.add(self.__Cords(row, col).coordinates)
                    if col != CRITICAL_COORDS[1]:
                        if self.battlefield[row][col + 1] == 0:
                            self.flotilla.append(ship)
                            ship = None
                    else:
                        self.flotilla.append(ship)
                        ship = None
        # traverse vertically
        ship = None

        for col in range(10):
            for row in range(10):
                if self.battlefield[row][col] == 1:
                    # Checking for horizontal ship
                    if col != CRITICAL_COORDS[0]:
                        if self.battlefield[row][col - 1] == 1:
                            continue
                    if col != CRITICAL_COORDS[1]:
                        if self.battlefield[row][col + 1] == 1:
                            continue
                    if (
                        ship is None
                        and self.__Cords(row, col).coordinates not in saved_cords
                    ):
                        ship = [self.__Cords(row, col)]
                    elif self.__Cords(row, col).coordinates not in saved_cords:
                        ship.append(self.__Cords(row, col))
                    if row != CRITICAL_COORDS[1]:
                        if self.battlefield[row + 1][col] == 0:
                            self.flotilla.append(ship)
                            ship = None
                    else:
                        self.flotilla.append(ship)
                        ship = None

    def strike(
        self, x_position: int, y_position: int
    ) -> Literal["hurt", "eliminate", "miss"]:
        ...


a = NavalBattle(r"school_10thgrade\NavalBattle\battlefield.txt", LetterCoordinates)
print(a._define_ships_positions(), a.flotilla)
