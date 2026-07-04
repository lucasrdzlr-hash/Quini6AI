from pathlib import Path
from openpyxl import Workbook


class ExcelWriter:

    def guardar_jugadas(self, jugadas):

        output = Path("output")
        output.mkdir(exist_ok=True)

        wb = Workbook()

        ws = wb.active
        ws.title = "Jugadas"

        ws.append([
            "J1",
            "J2",
            "J3",
            "J4",
            "J5",
            "J6"
        ])

        for jugada in jugadas:

            ws.append(jugada.numeros)

        wb.save(output / "jugadas.xlsx")

        print("\nArchivo generado:")
        print(output / "jugadas.xlsx")