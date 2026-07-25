from quini6ai.services.base_service import BaseService


class HistorialService(BaseService):

    @property
    def nombre(self):
        return "Historial"

    def ejecutar(self):
        print("\nMódulo en desarrollo.\n")
        input("Presione ENTER para continuar...")