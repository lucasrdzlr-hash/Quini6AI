import random

from quini6ai.models.jugada import Jugada


class WeightedGenerator:

    def __init__(self, ranking):

        self.ranking = ranking

    def generar(self, cantidad):

        pesos = self.ranking["score_final"].tolist()

        numeros = self.ranking["numero"].tolist()

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