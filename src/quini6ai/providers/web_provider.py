import pandas as pd

from quini6ai.providers.base_provider import BaseProvider

from quini6ai.scrapers.historial_scraper import HistorialScraper
from quini6ai.scrapers.cg20_scraper import CG20Scraper
from quini6ai.scrapers.cg50_scraper import CG50Scraper
from quini6ai.scrapers.cg100_scraper import CG100Scraper


class WebProvider(BaseProvider):

    def cargar(self):

        historial = HistorialScraper().obtener()

        cg20 = CG20Scraper().obtener()

        cg50 = CG50Scraper().obtener()

        cg100 = CG100Scraper().obtener()

        df = (
            historial
            .merge(cg20, on="numero")
            .merge(cg50, on="numero")
            .merge(cg100, on="numero")
        )

        return df.sort_values(
            "numero"
        ).reset_index(drop=True)