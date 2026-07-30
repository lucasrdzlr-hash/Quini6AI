from quini6ai.providers.excel_provider import ExcelProvider


class Quini6Provider:

    def __init__(self):
        self.provider = ExcelProvider()

    def cargar(self):

        df = self.provider.cargar()

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
            "categoria",
        ]

        return df[columnas]