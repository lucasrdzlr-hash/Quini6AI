from games.quini6.provider import Quini6Provider

from quini6ai.version import VERSION

from quini6ai.core.strategy_loader import StrategyLoader

from quini6ai.scoring.feature_engine import FeatureEngine
from quini6ai.scoring.score_engine import ScoreEngine
from quini6ai.scoring.jugada_score import JugadaScore

from quini6ai.generators.weighted_generator import WeightedGenerator

from quini6ai.evaluators.evaluator import Evaluator

from quini6ai.writers.excel_writer import ExcelWriter

from quini6ai.database.repositories.ejecuciones_repository import (
    EjecucionesRepository,
)

from quini6ai.services.base_service import BaseService


class GenerarService(BaseService):

    @property
    def nombre(self):
        return "Generar jugadas"

    def ejecutar(self):

        print("\n===================================")
        print("GENERACIÓN DE JUGADAS")
        print("===================================\n")

        strategy = self._cargar_estrategia()

        df, ranking = self._generar_ranking(strategy)

        jugadas = self._generar_jugadas(ranking)

        jugadas_validas = self._evaluar_jugadas(
            jugadas,
            ranking
        )

        self._exportar(jugadas_validas)

        promedio = self._calcular_promedio(
            jugadas_validas
        )

        self._registrar_ejecucion(
            strategy,
            jugadas_validas,
            promedio
        )

        self._mostrar_resumen(
            df,
            jugadas,
            jugadas_validas,
            promedio
        )


    # -------------------------------------------------

    def _cargar_estrategia(self):

        strategy = StrategyLoader().cargar(
            "balanceada"
        )

        print("=== ESTRATEGIA ===")
        print(f'Nombre      : {strategy["nombre"]}')
        print(f'Descripción : {strategy["descripcion"]}')
        print()

        return strategy


    # -------------------------------------------------

    def _generar_ranking(self, strategy):

        provider = Quini6Provider()

        df = provider.cargar()

        print(
            f"Registros cargados: {len(df)}\n"
        )

        df = FeatureEngine(df).calcular()

        pesos = strategy["score"]
    

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

        return df, ranking


    # -------------------------------------------------

    def _generar_jugadas(self, ranking):

        generator = WeightedGenerator(
            ranking
        )

        jugadas = generator.generar(20)

        print(
            f"\nJugadas generadas: {len(jugadas)}"
        )

        return jugadas


    # -------------------------------------------------

    def _evaluar_jugadas(
        self,
        jugadas,
        ranking
    ):

        evaluator = Evaluator()

        jugadas_validas = []

        for jugada in jugadas:

            jugada = evaluator.evaluar(
                jugada
            )

            if jugada.valida:

                jugadas_validas.append(
                    jugada
                )

        print(
            f"Jugadas válidas: {len(jugadas_validas)}"
        )

        score_engine = JugadaScore()

        for jugada in jugadas_validas:

            score_engine.calcular(
                jugada,
                ranking
            )


        jugadas_validas.sort(
            key=lambda j: j.score,
            reverse=True
        )


        print("\n=== TOP JUGADAS ===")

        for posicion, jugada in enumerate(
            jugadas_validas,
            start=1
        ):

            print(
                f"{posicion:02d} | "
                f"Score {jugada.score:.4f} | "
                f"{jugada.numeros}"
            )

        return jugadas_validas


    # -------------------------------------------------

    def _exportar(self, jugadas):

        writer = ExcelWriter()

        writer.guardar_jugadas(
            jugadas
        )


    # -------------------------------------------------

    def _calcular_promedio(self, jugadas):

        if jugadas:

            return (
                sum(j.score for j in jugadas)
                /
                len(jugadas)
            )

        return 0


    # -------------------------------------------------

    def _registrar_ejecucion(
        self,
        strategy,
        jugadas,
        promedio
    ):

        repo = EjecucionesRepository()

        repo.guardar(
            version=VERSION,
            estrategia=strategy["nombre"],
            cantidad_jugadas=len(jugadas),
            score_promedio=promedio
        )

        repo.cerrar()


    # -------------------------------------------------

    def _mostrar_resumen(
        self,
        df,
        jugadas_generadas,
        jugadas_validas,
        promedio
    ):

        print("\n===================================")
        print("RESUMEN")
        print("===================================")

        print(
            f"Registros analizados : {len(df)}"
        )

        print(
            f"Jugadas generadas    : {len(jugadas_generadas)}"
        )

        print(
            f"Jugadas válidas      : {len(jugadas_validas)}"
        )

        if jugadas_validas:

            print(
                f"Mejor score          : "
                f"{jugadas_validas[0].score:.4f}"
            )

            print(
                f"Score promedio       : "
                f"{promedio:.4f}"
            )

        print(
            "\nProceso finalizado correctamente."
        )