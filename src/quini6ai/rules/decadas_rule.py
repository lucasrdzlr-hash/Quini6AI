from quini6ai.rules.base_rule import BaseRule


class DecadasRule(BaseRule):

    @property
    def nombre(self):
        return "decadas"

    def validar(self, jugada, parametros):

        decadas = {
            numero // 10
            for numero in jugada.numeros
        }

        return (
            parametros["minimo"]
            <= len(decadas)
            <= parametros["maximo"]
        )