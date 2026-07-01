from games.quini6.provider import Quini6Provider

from quini6ai.core.feature_engine import FeatureEngine
from quini6ai.core.score_engine import ScoreEngine
from quini6ai.core.config import cargar_estrategia


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

        print()

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