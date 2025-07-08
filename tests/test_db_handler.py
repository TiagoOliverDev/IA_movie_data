import sqlite3
import pytest
from storage import db_handler

@pytest.fixture
def memoria_db(monkeypatch):
    # Cria uma conexão SQLite em memória
    conn = sqlite3.connect(":memory:")
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE historico_consultas (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            titulo_filme TEXT NOT NULL,
            data_lancamento TEXT,
            bilheteria TEXT,
            sinopse TEXT
        )
    """)
    conn.commit()

    # Monkeypatch substitui get_connection do db_handler
    monkeypatch.setattr(db_handler, "get_connection", lambda: conn)

    return conn


def test_salvar_historico_pesquisa(memoria_db):
    db_handler.save_search_history(
        titulo="Matrix",
        data_lancamento="1999-03-31",
        bilheteria="$463 milhões",
        sinopse="Um programador descobre que a realidade é uma simulação."
    )

    cursor = memoria_db.cursor()
    cursor.execute("SELECT * FROM historico_consultas WHERE titulo_filme = ?", ("Matrix",))
    row = cursor.fetchone()

    assert row is not None
    assert row[1] == "Matrix"
    assert "simulação" in row[4]


def test_consultar_historico_por_titulo(memoria_db):
    # Pré-insere dado
    memoria_db.cursor().execute("""
        INSERT INTO historico_consultas (titulo_filme, data_lancamento, bilheteria, sinopse)
        VALUES (?, ?, ?, ?)
    """, ("Titanic", "1997-12-19", "$2.187 bilhões", "Um romance trágico no Titanic"))
    memoria_db.commit()

    resultado = db_handler.consult_history_by_title("Titanic")
    assert isinstance(resultado, dict)
    assert resultado["data_lancamento"] == "1997-12-19"
    assert "romance" in resultado["sinopse"]

