from pathlib import Path
import pandas as pd


class Quini6Provider:

    def __init__(self):

        self.archivo = Path("data") / "Q2.xlsx"
        self.hoja = "Stats"

    def cargar(self):

        if not self.archivo.exists():
            raise FileNotFoundError(
                f"No existe {self.archivo}"
            )

        df = pd.read_excel(
            self.archivo,
            sheet_name=self.hoja
        )

        df.columns = (
            df.columns
            .str.strip()
            .str.lower()
        )

        columnas = [
            "numero",
            "ap20",
            "au20",
            "sc20",
            "ap50",
            "au50",
            "sc50",
            "ap100",
            "au100",
            "sc100",
            "hist_ap",
            "ult_salida",
            "atraso",
            "grupo",
            "categoria"
        ]

        return df[columnas]