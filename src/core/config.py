import json
from pathlib import Path


def cargar_estrategia(nombre):

    archivo = Path("config") / f"{nombre}.json"

    with open(archivo, encoding="utf8") as f:
        return json.load(f)