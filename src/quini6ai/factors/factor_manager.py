from quini6ai.factors.promedio_factor import PromedioFactor


class FactorManager:

    def __init__(self):

        self.factores = [
            PromedioFactor()
        ]

    def calcular(self, jugada, ranking):

        resultados = {}

        for factor in self.factores:

            resultados[factor.nombre] = factor.calcular(
                jugada,
                ranking
            )

        return resultados