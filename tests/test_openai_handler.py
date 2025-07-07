import pytest
from unittest.mock import patch
from core.openai_handler import get_movie_insights


@patch("core.openai_handler.client.chat.completions.create")
def test_get_movie_insights_success(mock_openai_call):
    mock_openai_call.return_value.choices = [
        type("obj", (object,), {
            "message": {
                "content": (
                    '{"data_lancamento": "1994-10-14", '
                    '"bilheteria": "$28,341,469", '
                    '"sinopse": "Dois assassinos de aluguel vivem situações inusitadas em Los Angeles."}'
                )
            }
        })()
    ]

    movie = "Pulp Fiction"
    result = get_movie_insights(movie)

    assert isinstance(result, dict)
    assert "data_lancamento" in result
    assert "bilheteria" in result
    assert "sinopse" in result
    assert result["data_lancamento"] == "1994-10-14"


def test_get_movie_insights_empty_input():
    with pytest.raises(ValueError, match="O título do filme não pode estar vazio."):
        get_movie_insights("")
