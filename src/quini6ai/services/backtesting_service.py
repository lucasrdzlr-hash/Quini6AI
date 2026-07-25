from quini6ai.services.base_service import BaseService


class BacktestingService(BaseService):

    @property
    def nombre(self):
        return "Backtesting"

    def ejecutar(self):
        print("\nMódulo en desarrollo.\n")
        input("Presione ENTER para continuar...")