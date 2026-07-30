from quini6ai.rules.base_rule import BaseRule


class BajosRule(BaseRule):

    @property
    def nombre(self):
        return "bajos"

    def validar(self, jugada, parametros):

        bajos = sum(
            1
            for n in jugada.numeros
            if n <= 22
        )

        minimo = parametros.get("minimo", 2)
        maximo = parametros.get("maximo", 4)

        return minimo <= bajos <= maximo