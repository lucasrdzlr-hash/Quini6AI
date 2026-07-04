from games.quini6.provider import Quini6Provider

from quini6ai.core.feature_engine import FeatureEngine
from quini6ai.core.score_engine import ScoreEngine
from quini6ai.core.config import cargar_estrategia

from quini6ai.generators.weighted_generator import WeightedGenerator
from quini6ai.evaluators.evaluator import Evaluator
from quini6ai.writers.excel_writer import ExcelWriter


class App:

    def run(self):

        print("===================================")
        print("           Quini6AI")
        print("===================================\n")

        # 1. Cargar datos
        provider = Quini6Provider()
        df = provider.cargar()

        # 2. Calcular features
        df = FeatureEngine(df).calcular()

        # 3. Cargar estrategia
        pesos = cargar_estrategia("balanceada")

        # 4. Calcular ranking
        ranking = ScoreEngine(
            df,
            pesos
        ).calcular()

        # 5. Mostrar ranking
        print("=== TOP 20 NÚMEROS ===")
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

        # 6. Generar jugadas
        generator = WeightedGenerator(ranking)
        jugadas = generator.generar(20)

        # 7. Evaluar jugadas
        evaluator = Evaluator()

        jugadas_validas = []

        print("\n=== JUGADAS VÁLIDAS ===")

        for i, jugada in enumerate(jugadas, start=1):

            jugada = evaluator.evaluar(jugada)

            if jugada.valida:

                jugadas_validas.append(jugada)

                print(
                    f"{len(jugadas_validas):02d} - {jugada.numeros}"
                )

        # 8. Exportar a Excel
        writer = ExcelWriter()

        writer.guardar_jugadas(
            jugadas_validas
        )

        print("\nProceso finalizado correctamente.")