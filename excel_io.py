from pathlib import Path
import pandas as pd


def leer_stats():

    archivo = Path("data") / "Q2.xlsx"

    if not archivo.exists():
        raise FileNotFoundError(f"No se encontró el archivo: {archivo}")

    df = pd.read_excel(
        archivo,
        sheet_name="Stats"
    )

    # Normalizar nombres de columnas
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

    faltantes = [c for c in columnas if c not in df.columns]

    if faltantes:
        raise ValueError(
            f"Faltan columnas en Stats: {faltantes}"
        )

    return df[columnas]