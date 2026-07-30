from quini6ai.generators.generator_manager import GeneratorManager
from quini6ai.generators.weighted_generator import WeightedGenerator
from quini6ai.generators.genetic_generator import GeneticGenerator

class GeneratorRegistry:

    @staticmethod
    def crear():

        manager = GeneratorManager()

        manager.registrar(
            WeightedGenerator()
        )

        manager.registrar(
            GeneticGenerator()
        )

        return manager