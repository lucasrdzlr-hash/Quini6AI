from datetime import datetime

from quini6ai.database.database import Database

from quini6ai.models.sorteo import Sorteo


class SorteosRepository:

    def __init__(self):
        self.db = Database()

    def guardar(self, sorteo: Sorteo):

        self.db.execute(
    """
    INSERT INTO sorteos
    (
        numero,
        fecha,
        tradicional,
        segunda,
        revancha,
        siempre_sale,
        creado_en
    )
    VALUES (?, ?, ?, ?, ?, ?, ?)
    """,
    (
        sorteo.numero,
        sorteo.fecha,
        sorteo.tradicional,
        sorteo.segunda,
        sorteo.revancha,
        sorteo.siempre_sale,
        datetime.now().isoformat(),
    ),
)

    def obtener(self, numero):

        cursor = self.db.execute(
            """
            SELECT *
            FROM sorteos
            WHERE numero=?
            """,
            (sorteo.numero,),
        )

        fila = cursor.fetchone()

        if fila is None:
            return None

        return Sorteo(
            numero=fila[1],
            fecha=fila[2],
            tradicional=fila[3],
            segunda=fila[4],
            revancha=fila[5],
            siempre_sale=fila[6],
        )

    def listar(self):

        cursor = self.db.execute(
            """
            SELECT *
            FROM sorteos
            ORDER BY numero DESC
            """
        )

        return cursor.fetchall()
    def ultimo(self):

        cursor = self.db.execute(
            """
            SELECT *
            FROM sorteos
            ORDER BY numero DESC
            LIMIT 1
            """
        )

        fila = cursor.fetchone()

        if fila is None:
            return None

        return Sorteo(
            numero=fila[1],
            fecha=fila[2],
            tradicional=fila[3],
            segunda=fila[4],
            revancha=fila[5],
            siempre_sale=fila[6],
        )
    def cerrar(self):
        self.db.close()