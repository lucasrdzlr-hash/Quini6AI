from quini6ai.database.database import Database


class Migration:

    def run(self):

        db = Database()

        db.execute("""
        CREATE TABLE IF NOT EXISTS ejecuciones (

            id INTEGER PRIMARY KEY AUTOINCREMENT,

            fecha TEXT,

            version TEXT,

            estrategia TEXT,

            cantidad_jugadas INTEGER,

            score_promedio REAL

        )
        """)

        db.execute("""
        CREATE TABLE IF NOT EXISTS sorteos (

            id INTEGER PRIMARY KEY AUTOINCREMENT,

            numero_sorteo INTEGER,

            fecha TEXT NOT NULL,

            modalidad TEXT NOT NULL,

            n1 INTEGER NOT NULL,
            n2 INTEGER NOT NULL,
            n3 INTEGER NOT NULL,
            n4 INTEGER NOT NULL,
            n5 INTEGER NOT NULL,
            n6 INTEGER NOT NULL,

            UNIQUE(numero_sorteo, modalidad)

        )
        """)

        db.close()
