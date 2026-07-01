from pathlib import Path
import sys

sys.path.insert(
    0,
    str(Path(__file__).parent)
)

sys.path.insert(
    0,
    str(Path(__file__).parent / "src")
)

from quini6ai.app import App


if __name__ == "__main__":
    App().run()