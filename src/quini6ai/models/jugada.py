from dataclasses import dataclass


@dataclass
class Jugada:

    numeros: list[int]

    score: float = 0.0