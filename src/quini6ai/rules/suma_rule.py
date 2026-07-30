from quini6ai.rules.base_rule import BaseRule


class SumaRule(BaseRule):

    @property
    def nombre(self):
        return "suma"

    def validar(self, jugada, parametros):

        total = sum(jugada.numeros)

        minimo = parametros.get("minimo", 60)
        maximo = parametros.get("maximo", 180)

        return minimo <= total <= maximo