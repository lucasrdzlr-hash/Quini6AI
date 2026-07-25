from pathlib import Path
import sys

sys.path.insert(
    0,
    str(Path(__file__).parent.parent / "src")
)

from quini6ai.models.sorteo import Sorteo

from quini6ai.database.repositories.sorteos_repository import (
    SorteosRepository
)

repo = SorteosRepository()

sorteo = Sorteo(
    numero=10000,
    fecha="2026-07-21",
    tradicional="01-02-03-04-05-06",
    segunda="07-08-09-10-11-12",
    revancha="13-14-15-16-17-18",
    siempre_sale="19-20-21-22-23-24"
)

repo.guardar(sorteo)

print(repo.ultimo())

repo.cerrar()