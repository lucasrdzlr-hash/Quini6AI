import pandas as pd


class FeatureEngine:

    def __init__(self, df: pd.DataFrame):
        self.df = df.copy()

    def calcular(self):

        self.df["f_sc20"] = self.df["sc20"]
        self.df["f_sc50"] = self.df["sc50"]
        self.df["f_sc100"] = self.df["sc100"]

        self.df["f_hist"] = (
            self.df["hist_ap"] /
            self.df["hist_ap"].max()
        )

        self.df["f_atraso"] = (
            self.df["atraso"] /
            self.df["atraso"].max()
        )

        return self.df