import pandas as pd


class ScoreEngine:

    def __init__(self, df, config):
        self.df = df
        self.cfg = config

    def calcular(self):

        self.df["PUNTAJE"] = (
            self.df["SCORE100"] * self.cfg["peso_score100"]
            + self.df["SCORE50"] * self.cfg["peso_score50"]
            + self.df["SCORE20"] * self.cfg["peso_score20"]
            + self.df["ATRASO"] * self.cfg["peso_atraso"]
        )

        return self.df.sort_values(
            "PUNTAJE",
            ascending=False
        )