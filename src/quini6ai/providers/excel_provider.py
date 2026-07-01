from pathlib import Path
import pandas as pd


class ExcelProvider:

    def __init__(self, archivo="data/Q2.xlsx", hoja="Stats"):
        self.archivo = Path(archivo)
        self.hoja = hoja

    def cargar(self):

        if not self.archivo.exists():
            raise FileNotFoundError(
                f"No existe el archivo {self.archivo}"
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

        return df