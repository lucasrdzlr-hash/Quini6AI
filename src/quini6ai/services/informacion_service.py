from quini6ai.services.base_service import BaseService

from quini6ai.version import VERSION


class InformacionService(BaseService):

    @property
    def nombre(self):
        return "Información del sistema"

    def ejecutar(self):

        print("\n===================================")
        print("Quini6AI")
        print("===================================")
        print(f"Versión: {VERSION}")

        input("\nPresione ENTER para continuar...")