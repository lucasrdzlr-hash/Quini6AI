from excel_io import leer_stats

from src.core.config import cargar_estrategia
from src.scoring.feature_engine import FeatureEngine
from src.scoring.score_engine import ScoreEngine


def main():

    df = leer_stats()

    df = FeatureEngine(df).calcular()

    pesos = cargar_estrategia("balanceada")

    ranking = ScoreEngine(
        df,
        pesos
    ).calcular()

    print(
        ranking[
            [
                "numero",
                "score_final",
                "grupo",
                "categoria"
            ]
        ].head(20)
    )


if __name__ == "__main__":
    main()