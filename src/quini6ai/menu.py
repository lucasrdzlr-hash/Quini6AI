from quini6ai.version import VERSION

from quini6ai.services.generar_service import GenerarService
from quini6ai.services.sorteos_service import SorteosService
from quini6ai.services.historial_service import HistorialService
from quini6ai.services.estadisticas_service import EstadisticasService
from quini6ai.services.backtesting_service import BacktestingService
from quini6ai.services.estrategias_service import EstrategiasService
from quini6ai.services.plugins_service import PluginsService
from quini6ai.services.configuracion_service import ConfiguracionService
from quini6ai.services.informacion_service import InformacionService


class Menu:

    def __init__(self):

        self.opciones = {

            "1": GenerarService(),

            "2": SorteosService(),

            "3": HistorialService(),

            "4": EstadisticasService(),

            "5": BacktestingService(),

            "6": EstrategiasService(),

            "7": PluginsService(),

            "8": ConfiguracionService(),

            "9": InformacionService()

        }

    def mostrar(self):

        while True:

            self._mostrar_encabezado()

            self._mostrar_menu()

            opcion = input(
                "\nSeleccione una opción: "
            ).strip()

            if opcion == "0":

                print("\nHasta luego.\n")
                break

            servicio = self.opciones.get(opcion)

            if servicio is None:

                print("\nOpción inválida.")

                input(
                    "\nPresione ENTER para continuar..."
                )

                continue

            try:

                print()

                servicio.ejecutar()

            except Exception as e:

                print("\n===================================")
                print("ERROR")
                print("===================================")

                print(e)

                input(
                    "\nPresione ENTER para continuar..."
                )

    def _mostrar_encabezado(self):

        print("\n=========================================")
        print(f"           Quini6AI {VERSION}")
        print("=========================================")

    def _mostrar_menu(self):

        print()

        for opcion, servicio in self.opciones.items():

            print(f"{opcion} - {servicio.nombre}")

        print("0 - Salir")