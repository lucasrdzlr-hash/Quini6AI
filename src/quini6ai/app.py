from games.quini6.provider import Quini6Provider
from quini6ai.core.feature_engine import FeatureEngine


class App:

    def run(self):

        print("Quini6AI")

        provider = Quini6Provider()

        df = provider.cargar()

        df = FeatureEngine(df).calcular()

        print()

        print(df[
            [
                "numero",
                "f_sc20",
                "f_sc50",
                "f_sc100",
                "f_hist",
                "f_atraso"
            ]
        ].head())