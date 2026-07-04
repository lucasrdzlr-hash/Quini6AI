class Evaluator:

    def evaluar(self, jugada):

        numeros = jugada.numeros

        pares = sum(1 for n in numeros if n % 2 == 0)

        bajos = sum(1 for n in numeros if n <= 22)

        suma = sum(numeros)

        motivos = []

        if pares < 2 or pares > 4:
            motivos.append("pares")

        if bajos < 2 or bajos > 4:
            motivos.append("bajos")

        if suma < 60 or suma > 180:
            motivos.append("suma")

        jugada.valida = len(motivos) == 0
        jugada.motivos = motivos

        return jugada