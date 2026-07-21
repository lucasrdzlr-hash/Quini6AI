from pathlib import Path
import sys

sys.path.insert(
    0,
    str(Path(__file__).parent.parent / "src")
)
from quini6ai.database.repositories.ejecuciones_repository import (
    EjecucionesRepository
)

repo = EjecucionesRepository()

for fila in repo.listar():

    print(fila)

repo.cerrar()