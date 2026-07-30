from quini6ai.generators.base_generator import BaseGenerator
from quini6ai.generators.weighted_generator import WeightedGenerator


class GeneticGenerator(BaseGenerator):

    @property
    def nombre(self):
        return "genetic"

    def generar(
        self,
        ranking,
        cantidad
    ):

        print("Usando GeneticGenerator (modo compatibilidad)")

        return WeightedGenerator().generar(
            ranking,
            cantidad
        )