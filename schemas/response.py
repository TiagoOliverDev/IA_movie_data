from pydantic import BaseModel

class MovieResponse(BaseModel):
    data_lancamento: str
    bilheteria: str
    sinopse: str
