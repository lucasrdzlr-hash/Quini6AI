from dataclasses import dataclass

@dataclass
class Numero:

    numero: int

    ap20: float
    au20: float
    sc20: float

    ap50: float
    au50: float
    sc50: float

    ap100: float
    au100: float
    sc100: float

    hist_ap: float

    ult_salida: str

    atraso: float

    grupo: str

    categoria: str

    peso: float = 0