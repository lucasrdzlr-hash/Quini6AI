from quini6ai.services.base_service import BaseService

from quini6ai.database.repositories.ejecuciones_repository import (
    EjecucionesRepository,
)


class HistorialService(BaseService):

    @property
    def nombre(self):
        return "Historial"

    def ejecutar(self):

        repo = EjecucionesRepository()

        ejecuciones = repo.listar()

        repo.cerrar()

        print("\n===================================")
        print("HISTORIAL DE EJECUCIONES")
        print("===================================\n")

        if not ejecuciones:

            print("No hay ejecuciones registradas.\n")

            input("Presione ENTER para continuar...")

            return

        print(
            f"{'Fecha':19} "
            f"{'Versión':10} "
            f"{'Estrategia':15} "
            f"{'Jugadas':8} "
            f"{'Score'}"
        )

        print("-" * 70)

        for fecha, version, estrategia, cantidad, score in ejecuciones:

            print(
                f"{fecha:19} "
                f"{version:10} "
                f"{estrategia:15} "
                f"{cantidad:<8} "
                f"{score:.4f}"
            )

        input("\nPresione ENTER para continuar...")