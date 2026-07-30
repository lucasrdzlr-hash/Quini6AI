from quini6ai.plugins.normalizacion_plugin import NormalizacionPlugin
from quini6ai.plugins.plugin_manager import PluginManager
from quini6ai.plugins.promedio_plugin import PromedioPlugin
from quini6ai.plugins.tendencia_plugin import TendenciaPlugin
from quini6ai.plugins.atraso_plugin import AtrasoPlugin

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

        manager.registrar(
            NormalizacionPlugin()
        )
        manager.registrar(
            AtrasoPlugin()
        )
        return manager