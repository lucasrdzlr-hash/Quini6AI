import pandas as pd


class ScoreEngine:

    def __init__(self, df: pd.DataFrame, pesos: dict):
        self.df = df.copy()
        self.pesos = pesos

    def calcular(self):

        self.df["score_final"] = (
            self.df["f_sc20"]   * self.pesos["sc20"] +
            self.df["f_sc50"]   * self.pesos["sc50"] +
            self.df["f_sc100"]  * self.pesos["sc100"] +
            self.df["f_hist"]   * self.pesos["hist"] +
            self.df["f_atraso"] * self.pesos["atraso"]
        )

        return (
            self.df
            .sort_values(
                "score_final",
                ascending=False
            )
            .reset_index(drop=True)
        )