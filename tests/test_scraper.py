from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parents[1]

sys.path.insert(0, str(ROOT / "src"))
from quini6ai.scrapers.base_scraper import BaseScraper


URL = (
    "https://www.combinacionganadora.com/"
    "ar/quini6/estadisticas/?nsorteos=20"
)


html = BaseScraper().descargar(URL)

print(html[:500])