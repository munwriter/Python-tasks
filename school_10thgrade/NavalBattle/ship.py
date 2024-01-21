from dataclasses import dataclass


@dataclass
class Coordinates:
    x: int
    y: int


@dataclass
class Ship:
    coordinates: dict[Coordinates, Coordinates]