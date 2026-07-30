class FeatureEngine:

    def __init__(self, df):

        self.df = df.copy()

    def calcular(self):

        # -------------------------
        # Características propias
        # del número.
        # -------------------------

        self.df["paridad"] = (

            self.df["numero"] % 2

        )

        self.df["decena"] = (

            self.df["numero"] // 10

        )

        return self.df