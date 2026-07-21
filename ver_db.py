import sqlite3

conn = sqlite3.connect("database/quini6ai.db")

cursor = conn.execute("""
SELECT
    fecha,
    version,
    estrategia,
    cantidad_jugadas,
    score_promedio
FROM ejecuciones
ORDER BY id DESC
""")

for fila in cursor.fetchall():
    print(fila)

conn.close()