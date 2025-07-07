import sqlite3
from pathlib import Path

DB_PATH = Path("storage/history.db")


def init_db():
    with sqlite3.connect(DB_PATH) as conn:
        cursor = conn.cursor()
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS historico_consultas (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                titulo_filme TEXT NOT NULL,
                data_lancamento TEXT,
                bilheteria TEXT,
                sinopse TEXT,
                data_consulta TIMESTAMP DEFAULT CURRENT_TIMESTAMP
            );
        """)
        conn.commit()


def salvar_historico_pesquisa(titulo: str, data_lancamento: str, bilheteria: str, sinopse: str):
    with sqlite3.connect(DB_PATH) as conn:
        cursor = conn.cursor()
        cursor.execute("""
            INSERT INTO historico_consultas (titulo_filme, data_lancamento, bilheteria, sinopse)
            VALUES (?, ?, ?, ?)
        """, (titulo, data_lancamento, bilheteria, sinopse))
        conn.commit()


def buscar_historico_salvo(titulo: str) -> dict | None:
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute("SELECT data_lancamento, bilheteria, sinopse FROM historico_consultas WHERE titulo_filme = ?", (titulo,))
    row = cursor.fetchone()
    conn.close()
    
    if row:
        return {
            "data_lancamento": row[0],
            "bilheteria": row[1],
            "sinopse": row[2]
        }
    return None