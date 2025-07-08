import pytest
from fastapi.testclient import TestClient
from app.main import app
from app.api import routes


def test_filme_endpoint_sucesso(monkeypatch):
    """
    Testa o endpoint /filme simulando um cenário de sucesso, onde a função
    get_movie_insights retorna corretamente os dados do filme solicitado.
    """
    mock_resultado = {
        "data_lancamento": "1997-12-19",
        "bilheteria": "$2.187 bilhões",
        "sinopse": "Um romance trágico a bordo do Titanic."
    }

    def mock_get_movie_insights(titulo):
        return mock_resultado

    monkeypatch.setattr(routes, "get_movie_insights", mock_get_movie_insights)

    client = TestClient(app)
    response = client.post("/filme", json={"titulo": "Titanic"})

    assert response.status_code == 200
    assert response.json() == mock_resultado


def test_filme_endpoint_erro(monkeypatch):
    """
    Testa o endpoint /filme simulando um cenário de erro, onde a função
    get_movie_insights retorna uma mensagem de erro indicando que o filme não foi encontrado.
    """
    def mock_get_movie_insights(titulo):
        return {"erro": "Filme não encontrado"}

    monkeypatch.setattr(routes, "get_movie_insights", mock_get_movie_insights)

    client = TestClient(app)
    response = client.post("/filme", json={"titulo": "XyzFilmeInexistente"})

    assert response.status_code == 404
    assert response.json()["detail"] == "Filme não encontrado"
