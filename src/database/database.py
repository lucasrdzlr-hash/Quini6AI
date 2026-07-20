from pathlib import Path
import sqlite3


class Database:

    def __init__(self):

        Path("database").mkdir(exist_ok=True)

        self.connection = sqlite3.connect(
            "database/quini6ai.db"
        )

    def execute(self, sql, params=()):

        cursor = self.connection.cursor()

        cursor.execute(sql, params)

        self.connection.commit()

        return cursor

    def close(self):

        self.connection.close()