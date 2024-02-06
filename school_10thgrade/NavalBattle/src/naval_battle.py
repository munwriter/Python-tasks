from pathlib import Path
from typing import Literal

from coordinates import Coordinates, LetterCoordinates, NumCoordinates


class NavalBattle:
    def __init__(self, path: str | Path, coordinates_system: Coordinates) -> None:
        self.battlefield = self._load_field(path)
        self.__Cords = coordinates_system
        self.flotilla = self._define_ships_positions(self.battlefield)

    def _load_field(self, path: str | Path) -> list[list[int]]:
        field = []
        with open(path, "tr") as f:
            for _ in range(10):
                formatted_line = list(map(int, f.readline().strip()))
                field.append(formatted_line)
        return field

    def _define_ships_positions(self, battlefield) -> list[list[Coordinates]]:
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
        self, x_position: int, y_position: int | str
    ) -> Literal["hurt", "eliminate", "miss", "мимо", "убил", "ранил"]:
        for ship in self.flotilla:
            for coordinate in ship:
                if coordinate.coordinates == f"{y_position}{x_position}":
                    ship.remove(self.__Cords(x_position - 1, y_position))
                    if ship:
                        return "ранил"
                    else:
                        return "убил"
        return "мимо"


def parse_strike_coords(path: str | Path) -> list[list]:
    strike_coordinates = []
    with open(path, "rt", encoding="utf-8") as f:
        lines = f.readlines()[10:]
        for line in lines:
            line = line.strip()
            strike_coordinates.append([int(line[1:]), line[0].lower()])

    return strike_coordinates


if __name__ == "__main__":
    battle = NavalBattle(
        r"school_10thgrade\NavalBattle\src\battlefield.txt", LetterCoordinates
    )
    print(battle.flotilla)
    strike_coordinates = parse_strike_coords(
        r"school_10thgrade\NavalBattle\src\battlefield.txt"
    )
    info = []
    for coordinate in strike_coordinates:

        info.append(f"{battle.strike(*coordinate)}\n")
    info[-1] = info[-1].strip()
    with open("output.txt", "wt", encoding="utf-8") as f:
        f.writelines(info)
