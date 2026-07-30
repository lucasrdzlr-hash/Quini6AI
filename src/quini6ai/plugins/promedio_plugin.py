from quini6ai.plugins.base_plugin import BasePlugin


class PromedioPlugin(BasePlugin):

    @property
    def nombre(self):
        return "promedio"

    def ejecutar(self, df, configuracion):

        df = df.copy()

        df["sc20"] = (
            df["ap20"] * configuracion["ap20"] / 20
            +
            df["au20"] * configuracion["au20"] / 20
        )

        df["sc50"] = (
            df["ap50"] * configuracion["ap50"] / 50
            +
            df["au50"] * configuracion["au50"] / 50
        )

        df["sc100"] = (
            df["ap100"] * configuracion["ap100"] / 100
            +
            df["au100"] * configuracion["au100"] / 100
        )

        return df