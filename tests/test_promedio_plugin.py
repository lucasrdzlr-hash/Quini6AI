from pathlib import Path
import sys

sys.path.insert(
    0,
    str(Path(__file__).parent.parent / "src")
)

from quini6ai.providers.web_provider import WebProvider
from quini6ai.plugins.promedio_plugin import PromedioPlugin
from quini6ai.core.strategy_loader import StrategyLoader


provider = WebProvider()

df = provider.cargar()

loader = StrategyLoader()

estrategia = loader.cargar("balanceada")

plugin = PromedioPlugin()

df = plugin.ejecutar(
    df,
    estrategia["plugins"]["promedio"],
)

print(df.info())

print(df.head())