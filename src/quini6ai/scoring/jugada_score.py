class JugadaScore:

    def calcular(self, jugada, ranking):

        tabla = ranking.set_index("numero")

        score = 0.0

        for numero in jugada.numeros:

            score += tabla.loc[numero, "score_final"]

        jugada.score = score / len(jugada.numeros)

        return jugada