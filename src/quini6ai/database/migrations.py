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

        db.close()