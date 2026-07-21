from datetime import datetime

from quini6ai.database.database import Database


class EjecucionesRepository:

    def __init__(self):

        self.db = Database()

    def guardar(
        self,
        version,
        estrategia,
        cantidad_jugadas,
        score_promedio
    ):

        self.db.execute(
            """
            INSERT INTO ejecuciones
            (
                fecha,
                version,
                estrategia,
                cantidad_jugadas,
                score_promedio
            )
            VALUES (?, ?, ?, ?, ?)
            """,
            (
                datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
                version,
                estrategia,
                cantidad_jugadas,
                score_promedio
            )
        )

    def listar(self):

        cursor = self.db.execute(
            """
            SELECT
                fecha,
                version,
                estrategia,
                cantidad_jugadas,
                score_promedio
            FROM ejecuciones
            ORDER BY id DESC
            """
        )

        return cursor.fetchall()

    def cerrar(self):

        self.db.close()