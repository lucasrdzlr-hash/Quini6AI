from dataclasses import dataclass


@dataclass
class Jugada:

    numeros: list[int]

    score: float = 0.0

    suma: int = 0

    pares: int = 0

    impares: int = 0

    bajos: int = 0

    altos: int = 0

    consecutivos: int = 0