import random

from quini6ai.generators.base_generator import BaseGenerator
from quini6ai.models.jugada import Jugada


class WeightedGenerator(BaseGenerator):

    @property
    def nombre(self):
        return "weighted"

    def generar(
        self,
        ranking,
        cantidad
    ):

        pesos = ranking["score_final"].tolist()

        numeros = ranking["numero"].tolist()

        jugadas = []

        while len(jugadas) < cantidad:

            seleccion = random.choices(
                numeros,
                weights=pesos,
                k=6
            )

            seleccion = sorted(set(seleccion))

            if len(seleccion) != 6:
                continue

            jugadas.append(
                Jugada(seleccion)
            )

        return jugadas