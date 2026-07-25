from quini6ai.database.database import Database


class Migration:

    def __init__(self):

        self.db = Database()

    def run(self):

        # -----------------------------------------
        # Tabla de ejecuciones
        # -----------------------------------------

        self.db.execute(
            """
            CREATE TABLE IF NOT EXISTS ejecuciones (

                id INTEGER PRIMARY KEY AUTOINCREMENT,

                fecha TEXT NOT NULL,

                version TEXT NOT NULL,

                estrategia TEXT NOT NULL,

                cantidad_jugadas INTEGER NOT NULL,

                score_promedio REAL NOT NULL

            )
            """
        )

        # -----------------------------------------
        # Tabla de sorteos
        # -----------------------------------------

        self.db.execute(
            """
            CREATE TABLE IF NOT EXISTS sorteos (

                id INTEGER PRIMARY KEY AUTOINCREMENT,

                numero INTEGER NOT NULL UNIQUE,

                fecha TEXT NOT NULL,

                tradicional TEXT NOT NULL,

                segunda TEXT NOT NULL,

                revancha TEXT NOT NULL,

                siempre_sale TEXT NOT NULL,

                creado_en TEXT NOT NULL

            )
            """
        )

    def close(self):

        self.db.close()