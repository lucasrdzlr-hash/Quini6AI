from quini6ai.plugins.base_plugin import BasePlugin


class AtrasoPlugin(BasePlugin):

    @property
    def nombre(self):
        return "atraso"

    def ejecutar(self, df, configuracion):

        df = df.copy()

        dias_minimos = configuracion.get(
            "dias_minimos",
            0
        )

        if "atraso" not in df.columns:
            return df

        df["atraso_score"] = (
            df["atraso"] >= dias_minimos
        ).astype(int)

        return df