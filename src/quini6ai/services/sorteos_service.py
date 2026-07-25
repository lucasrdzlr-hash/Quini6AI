from datetime import datetime

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

        print("\n===================================")
        print("REGISTRO DE SORTEOS")
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