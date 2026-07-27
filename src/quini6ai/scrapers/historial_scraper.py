import pandas as pd

from quini6ai.scrapers.base_scraper import BaseScraper


class HistorialScraper(BaseScraper):

    URL = (
        "https://www.quini-6-resultados.com.ar/"
        "quini6/quini6estadisticas.aspx"
    )

    def obtener(self):

        tabla = pd.read_html(self.URL)[0]

        tabla.columns = [
            "numero",
            "hist_ap",
            "ult_salida",
        ]

        tabla["ult_salida"] = pd.to_datetime(
            tabla["ult_salida"],
            dayfirst=True,
        )

        return tabla