from pathlib import Path
import sys

sys.path.insert(
    0,
    str(Path(__file__).parent.parent / "src")
)

from quini6ai.scrapers.historial_scraper import HistorialScraper

scraper = HistorialScraper()

df = scraper.obtener()

print(df.info())
print()
print(df.head())