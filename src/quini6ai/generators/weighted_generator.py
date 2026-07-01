import numpy as np


class WeightedGenerator:

    def __init__(self, ranking):
        self.ranking = ranking.copy()

        self.probabilidades = (
            self.ranking["score_final"] /
            self.ranking["score_final"].sum()
        )

    def generar(self):

        numeros = np.random.choice(
            self.ranking["numero"],
            size=6,
            replace=False,
            p=self.probabilidades
        )

        return sorted(numeros.tolist())