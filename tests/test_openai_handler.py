import pytest
from unittest.mock import patch, MagicMock
from core.openai_handler import get_movie_insights


@patch("core.openai_handler.client.chat.completions.create")
def test_get_movie_insights_success(mock_openai_call):
    """
    Testa se get_movie_insights retorna corretamente os dados de um filme
    quando a OpenAI responde com um JSON válido via function_call.arguments.
    """
    mock_response = MagicMock()
    mock_response.choices = [
        MagicMock(
            message=MagicMock(
                function_call=MagicMock(
                    name="obter_detalhes_filme",
                    arguments=(
                        '{"data_lancamento": "1994-10-14", '
                        '"bilheteria": "$28,341,469", '
                        '"sinopse": "Dois assassinos de aluguel vivem situações inusitadas em Los Angeles."}'
                    )
                )
            )
        )
    ]
    mock_openai_call.return_value = mock_response

    result = get_movie_insights("Pulp Fiction")

    assert isinstance(result, dict)
    assert result["data_lancamento"] == "1994-10-14"
    assert result["bilheteria"] == "$28,341,469"
    assert "assassinos de aluguel" in result["sinopse"]


@patch("core.openai_handler.client.chat.completions.create")
def test_get_movie_insights_not_found(mock_openai_call):
    """
    Testa se get_movie_insights retorna uma mensagem de erro apropriada
    quando a OpenAI informa que o filme não foi encontrado.
    """
    mock_response = MagicMock()
    mock_response.choices = [
        MagicMock(
            message=MagicMock(
                function_call=MagicMock(
                    name="obter_detalhes_filme",
                    arguments='{"erro": "Filme não encontrado"}'
                )
            )
        )
    ]
    mock_openai_call.return_value = mock_response

    result = get_movie_insights("FilmeInexistente")

    assert isinstance(result, dict)
    assert "erro" in result
    assert result["erro"] == "Filme não encontrado. Verifique o título e tente novamente."


def test_get_movie_insights_empty_input():
    """
    Testa se get_movie_insights levanta uma exceção do tipo ValueError
    ao receber uma string vazia como título de filme.
    """
    with pytest.raises(ValueError, match="O título do filme não pode estar vazio."):
        get_movie_insights("")
