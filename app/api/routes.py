from fastapi import APIRouter, HTTPException
from schemas.request import MovieRequest
from schemas.response import MovieResponse
from core.openai_handler import get_movie_insights

router = APIRouter()

@router.post("/filme", response_model=MovieResponse)
def consultar_filme(req: MovieRequest):
    result = get_movie_insights(req.titulo)

    if isinstance(result, dict) and result.get("erro"):
        raise HTTPException(status_code=404, detail=result["erro"])

    return result
