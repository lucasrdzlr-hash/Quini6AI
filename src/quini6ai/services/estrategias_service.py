from quini6ai.services.base_service import BaseService


class EstrategiasService(BaseService):

    @property
    def nombre(self):
        return "Estrategias"

    def ejecutar(self):
        print("\nMódulo en desarrollo.\n")
        input("Presione ENTER para continuar...")