from quini6ai.plugins.plugin_manager import PluginManager

from quini6ai.plugins.promedio_plugin import PromedioPlugin
from quini6ai.plugins.tendencia_plugin import TendenciaPlugin


class PluginRegistry:

    @staticmethod
    def crear():

        manager = PluginManager()

        manager.registrar(
            PromedioPlugin()
        )

        manager.registrar(
            TendenciaPlugin()
        )

        return manager