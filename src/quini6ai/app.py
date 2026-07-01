from games.quini6.provider import Quini6Provider

from quini6ai.core.feature_engine import FeatureEngine
from quini6ai.core.score_engine import ScoreEngine
from quini6ai.core.config import cargar_estrategia
from quini6ai.generators.weighted_generator import WeightedGenerator


class App:

    def run(self):

        provider = Quini6Provider()

        df = provider.cargar()

        df = FeatureEngine(df).calcular()

        pesos = cargar_estrategia("balanceada")

        ranking = ScoreEngine(
            df,
            pesos
        ).calcular()

        print("\n=== TOP 20 NÚMEROS ===")
        print(
            ranking[
                [
                    "numero",
                    "score_final",
                    "grupo",
                    "categoria"
                ]
            ].head(20)
        )

        print("\n=== JUGADAS GENERADAS ===")

        generator = WeightedGenerator(ranking)

        jugadas = generator.generar(20)

        for i, jugada in enumerate(jugadas, start=1):
            print(f"{i:02d} - {jugada.numeros}")