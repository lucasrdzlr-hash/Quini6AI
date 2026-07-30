from quini6ai.plugins.base_plugin import BasePlugin


class NormalizacionPlugin(BasePlugin):

    @property
    def nombre(self):
        return "normalizacion"

    def ejecutar(self, df, configuracion):

        df = df.copy()

        if "atraso" in df.columns:

            maximo = df["atraso"].max()

            if maximo > 0:

                df["atraso_norm"] = (
                    df["atraso"] / maximo
                )

            else:

                df["atraso_norm"] = 0

        if "hist_ap" in df.columns:

            maximo = df["hist_ap"].max()

            if maximo > 0:

                df["hist_ap_norm"] = (
                    df["hist_ap"] / maximo
                )

            else:

                df["hist_ap_norm"] = 0

        return df