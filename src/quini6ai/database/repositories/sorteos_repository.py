from quini6ai.database.database import Database


class SorteosRepository:

    MODALIDADES = (
        "Tradicional",
        "La Segunda",
        "Revancha",
        "Siempre Sale",
    )

    def __init__(self):
        self.db = Database()

    def guardar(
        self,
        numero_sorteo,
        fecha,
        modalidad,
        numeros,
    ):
        if modalidad not in self.MODALIDADES:
            raise ValueError(f"Modalidad inválida: {modalidad}")

        if len(numeros) != 6:
            raise ValueError("Un sorteo debe tener exactamente 6 números")

        numeros = [int(n) for n in numeros]

        if len(set(numeros)) != 6:
            raise ValueError("Los números del sorteo no pueden repetirse")

        if any(n < 0 or n > 45 for n in numeros):
            raise ValueError("Los números deben estar entre 0 y 45")

        self.db.execute(
            """
            INSERT INTO sorteos
            (
                numero_sorteo,
                fecha,
                modalidad,
                n1, n2, n3, n4, n5, n6
            )
            VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
            """,
            (
                numero_sorteo,
                fecha,
                modalidad,
                *numeros,
            ),
        )

    def guardar_lote(self, sorteos):
        for sorteo in sorteos:
            self.guardar(
                numero_sorteo=sorteo["numero_sorteo"],
                fecha=sorteo["fecha"],
                modalidad=sorteo["modalidad"],
                numeros=sorteo["numeros"],
            )

    def listar(self, limite=20):
        cursor = self.db.execute(
            """
            SELECT
                id,
                numero_sorteo,
                fecha,
                modalidad,
                n1, n2, n3, n4, n5, n6
            FROM sorteos
            ORDER BY fecha DESC, numero_sorteo DESC, id DESC
            LIMIT ?
            """,
            (limite,),
        )

        return cursor.fetchall()

    def obtener_ultimo(self, modalidad=None):
        if modalidad:
            cursor = self.db.execute(
                """
                SELECT
                    id,
                    numero_sorteo,
                    fecha,
                    modalidad,
                    n1, n2, n3, n4, n5, n6
                FROM sorteos
                WHERE modalidad = ?
                ORDER BY fecha DESC, numero_sorteo DESC, id DESC
                LIMIT 1
                """,
                (modalidad,),
            )
        else:
            cursor = self.db.execute(
                """
                SELECT
                    id,
                    numero_sorteo,
                    fecha,
                    modalidad,
                    n1, n2, n3, n4, n5, n6
                FROM sorteos
                ORDER BY fecha DESC, numero_sorteo DESC, id DESC
                LIMIT 1
                """
            )

        return cursor.fetchone()

    def contar(self, modalidad=None):
        if modalidad:
            cursor = self.db.execute(
                "SELECT COUNT(*) FROM sorteos WHERE modalidad = ?",
                (modalidad,),
            )
        else:
            cursor = self.db.execute(
                "SELECT COUNT(*) FROM sorteos"
            )

        return cursor.fetchone()[0]

    def cerrar(self):
        self.db.close()
