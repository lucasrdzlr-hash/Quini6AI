from quini6ai.plugins.base_plugin import BasePlugin


class TendenciaPlugin(BasePlugin):

    @property
    def nombre(self):
        return "tendencia"

    def ejecutar(self, df, configuracion):

        df = df.copy()

        df["tendencia20_100"] = (
            df["sc20"] - df["sc100"]
        )

        df["tendencia50_100"] = (
            df["sc50"] - df["sc100"]
        )

        return df