from quini6ai.services.base_service import BaseService


class EstadisticasService(BaseService):

    @property
    def nombre(self):
        return "Estadísticas"

    def ejecutar(self):
        print("\nMódulo en desarrollo.\n")
        input("Presione ENTER para continuar...")