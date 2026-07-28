from io import StringIO

import pandas as pd

from quini6ai.scrapers.base_scraper import BaseScraper


class CG50Scraper(BaseScraper):

    URL = (
        "https://www.combinacionganadora.com/ar/"
        "quini6/estadisticas/?nsorteos=50"
    )

    def obtener(self):

        html = self.descargar_html(self.URL)

        tablas = pd.read_html(StringIO(html))

        apariciones = pd.concat(
            [tablas[2], tablas[3]],
            ignore_index=True,
        )

        ausencias = pd.concat(
            [tablas[7], tablas[8]],
            ignore_index=True,
        )

        apariciones = apariciones.rename(
            columns={
                "Número": "numero",
                "Apariciones": "ap50",
            }
        )

        ausencias = ausencias.rename(
            columns={
                "Número": "numero",
                "Ausencias": "au50",
            }
        )

        df = apariciones.merge(
            ausencias,
            on="numero",
        )

        df = df[
            [
                "numero",
                "ap50",
                "au50",
            ]
        ]

        df = df.sort_values(
            "numero"
        ).reset_index(drop=True)

        return df