class BaseScraper:

    def obtener(self):
        raise NotImplementedError(
            "Los scrapers deben implementar obtener()."
        )