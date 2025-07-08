import sqlite3
from pathlib import Path

DB_PATH = Path("storage/history.db")


def get_connection():
    return sqlite3.connect(DB_PATH)


def init_db():
    with get_connection() as conn:
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


def save_search_history(titulo: str, data_lancamento: str, bilheteria: str, sinopse: str):
    with get_connection() as conn:
        cursor = conn.cursor()
        cursor.execute("""
            INSERT INTO historico_consultas (titulo_filme, data_lancamento, bilheteria, sinopse)
            VALUES (?, ?, ?, ?)
        """, (titulo, data_lancamento, bilheteria, sinopse))
        conn.commit()


def consult_history_by_title(titulo: str) -> dict | None:
    with get_connection() as conn:
        cursor = conn.cursor()
        cursor.execute("""
            SELECT data_lancamento, bilheteria, sinopse
            FROM historico_consultas
            WHERE titulo_filme = ?
        """, (titulo,))
        row = cursor.fetchone()
    
    if row:
        return {
            "data_lancamento": row[0],
            "bilheteria": row[1],
            "sinopse": row[2]
        }
    return None
