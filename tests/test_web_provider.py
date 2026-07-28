from pathlib import Path
import sys

sys.path.insert(
    0,
    str(Path(__file__).parent.parent / "src")
)

from quini6ai.providers.web_provider import WebProvider

provider = WebProvider()

df = provider.cargar()

print(df.info())

print()

print(df.head())

print()

print(df.tail())