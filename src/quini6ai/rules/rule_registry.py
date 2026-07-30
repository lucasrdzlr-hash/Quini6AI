from quini6ai.rules.rule_manager import RuleManager

from quini6ai.rules.pares_rule import ParesRule
from quini6ai.rules.bajos_rule import BajosRule
from quini6ai.rules.suma_rule import SumaRule
from quini6ai.rules.decadas_rule import DecadasRule
from quini6ai.rules.categoria_rule import CategoriaRule


class RuleRegistry:

    @staticmethod
    def crear():

        manager = RuleManager()

        manager.registrar(ParesRule())
        manager.registrar(BajosRule())
        manager.registrar(SumaRule())
        manager.registrar(DecadasRule())
        manager.registrar(CategoriaRule())

        return manager