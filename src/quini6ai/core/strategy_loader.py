from pathlib import Path
import yaml


class StrategyLoader:

    def cargar(self, nombre):

        archivo = (
            Path("config")
            / "estrategias"
            / f"{nombre}.yaml"
        )

        with open(
            archivo,
            "r",
            encoding="utf-8"
        ) as f:

            return yaml.safe_load(f)