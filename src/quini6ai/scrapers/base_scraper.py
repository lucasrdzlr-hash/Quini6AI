import requests


class BaseScraper:

    HEADERS = {
        "User-Agent": (
            "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
            "AppleWebKit/537.36 (KHTML, like Gecko) "
            "Chrome/138.0 Safari/537.36"
        )
    }

    def descargar_html(self, url):

        response = requests.get(
            url,
            headers=self.HEADERS,
            timeout=30,
        )

        response.raise_for_status()

        return response.text

    def obtener(self):
        raise NotImplementedError(
            "Los scrapers deben implementar obtener()."
        )