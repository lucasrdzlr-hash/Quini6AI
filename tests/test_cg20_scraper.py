from pathlib import Path
import sys

sys.path.insert(
    0,
    str(Path(__file__).parent.parent / "src")
)

from quini6ai.scrapers.cg20_scraper import CG20Scraper

scraper = CG20Scraper()

df = scraper.obtener()

print(df.info())
print()
print(df.head())
print()
print(df.tail())