from quini6ai.factors.base_factor import BaseFactor


class PromedioFactor(BaseFactor):

    nombre = "promedio"

    def calcular(self, jugada, ranking):

        df = ranking.set_index("numero")

        scores = []

        for numero in jugada.numeros:

            scores.append(
                df.loc[numero, "score_final"]
            )

        return sum(scores) / len(scores)