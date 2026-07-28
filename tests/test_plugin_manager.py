from pathlib import Path
import sys

sys.path.insert(
    0,
    str(Path(__file__).parent.parent / "src")
)

from quini6ai.plugins.plugin_manager import PluginManager
from quini6ai.plugins.promedio_plugin import PromedioPlugin
from quini6ai.core.strategy_loader import StrategyLoader

loader = StrategyLoader()

estrategia = loader.cargar("balanceada")

manager = PluginManager()

manager.registrar(
    PromedioPlugin()
)

manager.ejecutar(
    None,
    estrategia,
)