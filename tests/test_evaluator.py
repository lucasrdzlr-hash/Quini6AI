import sys
from pathlib import Path

sys.path.append(str(Path(__file__).resolve().parents[1]))

from src.models.jugada import Jugada
from src.evaluators.evaluator import Evaluator

jugada = Jugada(
    numeros=[5, 8, 13, 20, 34, 43]
)

jugada = Evaluator.evaluar(jugada)

print(jugada)