from dataclasses import dataclass, field


@dataclass
class Jugada:

    numeros: list[int]

    score: float = 0.0

    valida: bool = False

    motivos: list[str] = field(default_factory=list)