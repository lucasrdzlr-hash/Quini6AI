from src.models.jugada import Jugada


class Evaluator:

    @staticmethod
    def evaluar(jugada: Jugada):

        numeros = sorted(jugada.numeros)

        jugada.suma = sum(numeros)

        jugada.pares = sum(1 for n in numeros if n % 2 == 0)

        jugada.impares = 6 - jugada.pares

        jugada.bajos = sum(1 for n in numeros if n <= 22)

        jugada.altos = 6 - jugada.bajos

        consecutivos = 0

        for i in range(len(numeros)-1):

            if numeros[i+1] == numeros[i] + 1:
                consecutivos += 1

        jugada.consecutivos = consecutivos

        return jugada