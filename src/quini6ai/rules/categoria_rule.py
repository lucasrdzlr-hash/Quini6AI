from quini6ai.rules.base_rule import BaseRule


class CategoriaRule(BaseRule):

    @property
    def nombre(self):
        return "categoria"

    def validar(self, jugada, parametros):

        # Se implementará en la versión 1.0
        return True