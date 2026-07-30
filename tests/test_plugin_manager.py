from games.quini6.provider import Quini6Provider

from quini6ai.plugins.plugin_registry import PluginRegistry


provider = Quini6Provider()

df = provider.cargar()

manager = PluginRegistry.crear()

df = manager.ejecutar(
    df,
    {}
)

print(df.info())

print(df.head())