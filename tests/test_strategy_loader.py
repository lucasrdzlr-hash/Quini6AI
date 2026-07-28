from pathlib import Path
import sys

sys.path.insert(
    0,
    str(Path(__file__).parent.parent / "src")
)

from quini6ai.core.strategy_loader import StrategyLoader

loader = StrategyLoader()

estrategia = loader.cargar("balanceada")

print(estrategia)