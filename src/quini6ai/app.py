from games.quini6.provider import Quini6Provider

from quini6ai.core.feature_engine import FeatureEngine
from quini6ai.core.score_engine import ScoreEngine
from quini6ai.core.config import cargar_estrategia
from quini6ai.core.strategy_loader import StrategyLoader

from quini6ai.database.migrations import Migration

from quini6ai.generators.weighted_generator import WeightedGenerator
from quini6ai.evaluators.evaluator import Evaluator
from quini6ai.scoring.jugada_score import JugadaScore
from quini6ai.writers.excel_writer import ExcelWriter


class App:

    def run(self):

        # ---------------------------------------------
        # Inicialización
        # ---------------------------------------------

        Migration().run()

        print("===================================")
        print("          Quini6AI v0.8.5")
        print("===================================\n")

        # ---------------------------------------------
        # Estrategia
        # ---------------------------------------------

        strategy = StrategyLoader().cargar("balanceada")

        print("=== ESTRATEGIA ===")
        print(f'Nombre      : {strategy["nombre"]}')
        print(f'Descripción : {strategy["descripcion"]}')
        print()

        # ---------------------------------------------
        # Carga de datos
        # ---------------------------------------------

        provider = Quini6Provider()

        df = provider.cargar()

        print(f"Registros cargados: {len(df)}")
        print()

        # ---------------------------------------------
        # Feature Engineering
        # ---------------------------------------------

        df = FeatureEngine(df).calcular()

        # ---------------------------------------------
        # Ranking de números
        # ---------------------------------------------

        pesos = cargar_estrategia("balanceada")

        ranking = ScoreEngine(
            df,
            pesos
        ).calcular()

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

        # ---------------------------------------------
        # Generación de jugadas
        # ---------------------------------------------

        generator = WeightedGenerator(ranking)

        jugadas = generator.generar(20)

        print(f"\nJugadas generadas: {len(jugadas)}")

        # ---------------------------------------------
        # Evaluación
        # ---------------------------------------------

        evaluator = Evaluator()

        jugadas_validas = []

        for jugada in jugadas:

            jugada = evaluator.evaluar(jugada)

            if jugada.valida:

                jugadas_validas.append(jugada)

        print(f"Jugadas válidas: {len(jugadas_validas)}")

        # ---------------------------------------------
        # Score de jugadas
        # ---------------------------------------------

        score_engine = JugadaScore()

        for jugada in jugadas_validas:

            score_engine.calcular(
                jugada,
                ranking
            )

        # ---------------------------------------------
        # Ordenar por score
        # ---------------------------------------------

        jugadas_validas.sort(
            key=lambda j: j.score,
            reverse=True
        )

        # ---------------------------------------------
        # Mostrar Top 20
        # ---------------------------------------------

        print("\n=== TOP JUGADAS ===")

        for posicion, jugada in enumerate(jugadas_validas, start=1):

            print(
                f"{posicion:02d} | "
                f"Score {jugada.score:.4f} | "
                f"{jugada.numeros}"
            )

        # ---------------------------------------------
        # Exportación
        # ---------------------------------------------

        writer = ExcelWriter()

        writer.guardar_jugadas(
            jugadas_validas
        )

        # ---------------------------------------------
        # Resumen
        # ---------------------------------------------

        print("\n===================================")
        print("RESUMEN")
        print("===================================")

        print(f"Registros analizados : {len(df)}")
        print(f"Jugadas generadas    : {len(jugadas)}")
        print(f"Jugadas válidas      : {len(jugadas_validas)}")

        if jugadas_validas:

            mejor = jugadas_validas[0].score
            promedio = sum(j.score for j in jugadas_validas) / len(jugadas_validas)

            print(f"Mejor score          : {mejor:.4f}")
            print(f"Score promedio       : {promedio:.4f}")

        print("\nProceso finalizado correctamente.")