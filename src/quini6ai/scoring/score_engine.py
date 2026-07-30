class ScoreEngine:

    def __init__(self, df, score_config):

        self.df = df.copy()
        self.score_config = score_config

    def calcular(self):

        self.df["score_final"] = 0.0

        for columna, config in self.score_config.items():

            peso = config.get("peso", 0)

            if columna not in self.df.columns:

                print(
                    f"Aviso: '{columna}' no existe."
                )

                continue

            self.df["score_final"] += (

                self.df[columna] * peso

            )

        return self.df.sort_values(
            "score_final",
            ascending=False
        )