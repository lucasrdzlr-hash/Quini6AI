class ScoreEngine:

    def __init__(self, df, pesos):
        self.df = df.copy()
        self.pesos = pesos

    def calcular(self):

        self.df["score_final"] = (

            self.df["sc100"] * self.pesos["sc100"]

            + self.df["sc50"] * self.pesos["sc50"]

            + self.df["sc20"] * self.pesos["sc20"]

            + self.df["atraso_norm"] * self.pesos["atraso"]

            + self.df["hist_ap_norm"] * self.pesos["hist_ap"]

            + self.df["tendencia20_100"] * self.pesos["tendencia"]

        )

        return self.df.sort_values(
            "score_final",
            ascending=False
        )