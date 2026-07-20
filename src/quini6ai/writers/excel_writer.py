from pathlib import Path
from openpyxl import Workbook
from openpyxl.styles import Font


class ExcelWriter:

    def guardar_jugadas(self, jugadas):

        output = Path("output")
        output.mkdir(exist_ok=True)

        wb = Workbook()

        ws = wb.active
        ws.title = "Jugadas"

        # Encabezados
        encabezados = [
            "Ranking",
            "Score",
            "N1",
            "N2",
            "N3",
            "N4",
            "N5",
            "N6"
        ]

        ws.append(encabezados)

        # Negrita para encabezados
        for cell in ws[1]:
            cell.font = Font(bold=True)

        # Ordenar por score descendente
        jugadas_ordenadas = sorted(
            jugadas,
            key=lambda j: j.score,
            reverse=True
        )

        # Escribir jugadas
        for posicion, jugada in enumerate(jugadas_ordenadas, start=1):

            fila = [
                posicion,
                round(jugada.score, 4),
                *jugada.numeros
            ]

            ws.append(fila)

        # Ajustar ancho de columnas
        for columna in ws.columns:

            largo = max(
                len(str(celda.value))
                if celda.value is not None else 0
                for celda in columna
            )

            ws.column_dimensions[
                columna[0].column_letter
            ].width = largo + 3

        archivo = output / "jugadas.xlsx"

        wb.save(archivo)

        print(f"\nArchivo Excel generado: {archivo}")