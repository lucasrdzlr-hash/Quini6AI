from quini6ai.services.base_service import BaseService
from quini6ai.models.sorteo import Sorteo
from quini6ai.database.repositories.sorteos_repository import (
    SorteosRepository,
)


class SorteosService(BaseService):

    @property
    def nombre(self):
        return "Registrar sorteo"

    def ejecutar(self):

        while True:

            print("\n===================================")
            print("GESTIÓN DE SORTEOS")
            print("===================================\n")

            print("1 - Registrar sorteo")
            print("2 - Ver último sorteo")
            print("3 - Listar sorteos")
            print("0 - Volver")

            opcion = input("\nSeleccione una opción: ").strip()

            if opcion == "0":
                break

            elif opcion == "1":
                self._registrar()

            elif opcion == "2":
                self._ultimo()

            elif opcion == "3":
                self._listar()

            else:
                print("\nOpción inválida.")

    # -------------------------------------------------

    def _registrar(self):

        print("\n===================================")
        print("REGISTRO DE SORTEO")
        print("===================================\n")

        try:

            numero = int(
                input("Número de sorteo: ")
            )

            fecha = input(
                "Fecha (YYYY-MM-DD): "
            ).strip()

            tradicional = input(
                "Tradicional: "
            ).strip()

            segunda = input(
                "La Segunda: "
            ).strip()

            revancha = input(
                "Revancha: "
            ).strip()

            siempre_sale = input(
                "Siempre Sale: "
            ).strip()

            sorteo = Sorteo(
                numero=numero,
                fecha=fecha,
                tradicional=tradicional,
                segunda=segunda,
                revancha=revancha,
                siempre_sale=siempre_sale,
            )

            repo = SorteosRepository()

            repo.guardar(sorteo)

            repo.cerrar()

            print("\nSorteo registrado correctamente.")

        except Exception as e:

            print("\n===================================")
            print("ERROR")
            print("===================================")

            print(e)

    # -------------------------------------------------

    def _ultimo(self):

        repo = SorteosRepository()

        sorteo = repo.ultimo()

        repo.cerrar()

        if sorteo is None:

            print("\nNo hay sorteos registrados.")

            return

        self._mostrar_sorteo(sorteo)

    # -------------------------------------------------

    def _listar(self):

        repo = SorteosRepository()

        sorteos = repo.listar()

        repo.cerrar()

        if not sorteos:

            print("\nNo hay sorteos registrados.")

            return

        print("\n===================================")
        print("LISTADO DE SORTEOS")
        print("===================================\n")

        for fila in sorteos:

            print(
                f"Sorteo {fila[1]} - Fecha {fila[2]}"
            )

    # -------------------------------------------------

    def _mostrar_sorteo(self, sorteo):

        print("\n===================================")
        print("ÚLTIMO SORTEO")
        print("===================================\n")

        print(f"Número: {sorteo.numero}")
        print(f"Fecha: {sorteo.fecha}")
        print()

        print(f"Tradicional   : {sorteo.tradicional}")
        print(f"La Segunda    : {sorteo.segunda}")
        print(f"Revancha      : {sorteo.revancha}")
        print(f"Siempre Sale  : {sorteo.siempre_sale}")