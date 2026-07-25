from quini6ai.services.base_service import BaseService


class PluginsService(BaseService):

    @property
    def nombre(self):
        return "Plugins"

    def ejecutar(self):
        print("\nMódulo en desarrollo.\n")
        input("Presione ENTER para continuar...")