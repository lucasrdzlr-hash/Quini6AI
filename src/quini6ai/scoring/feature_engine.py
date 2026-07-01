import pandas as pd


class FeatureEngine:

    def __init__(self, df):
        self.df = df.copy()

    def calcular(self):

        # Tendencia reciente
        self.df["tendencia20_100"] = self.df["sc20"] - self.df["sc100"]
        self.df["tendencia50_100"] = self.df["sc50"] - self.df["sc100"]

        # Paridad
        self.df["paridad"] = self.df["numero"] % 2

        # Decena
        self.df["decena"] = self.df["numero"] // 10

        # Normalizaciones
        self.df["atraso_norm"] = (
            self.df["atraso"] / self.df["atraso"].max()
        )

        self.df["hist_ap_norm"] = (
            self.df["hist_ap"] / self.df["hist_ap"].max()
        )

        return self.df