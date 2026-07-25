from quini6ai.services.base_service import BaseService


class ConfiguracionService(BaseService):

    @property
    def nombre(self):
        return "Configuración"

    def ejecutar(self):
        print("\nMódulo en desarrollo.\n")
        input("Presione ENTER para continuar...")