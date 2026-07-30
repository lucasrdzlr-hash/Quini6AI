from quini6ai.rules.base_rule import BaseRule


class ParesRule(BaseRule):

    @property
    def nombre(self):
        return "pares"

    def validar(self, jugada, parametros):

        pares = sum(
            1
            for n in jugada.numeros
            if n % 2 == 0
        )

        minimo = parametros.get("minimo", 2)
        maximo = parametros.get("maximo", 4)

        return minimo <= pares <= maximo