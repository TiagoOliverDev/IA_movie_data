from pydantic import BaseModel

class MovieRequest(BaseModel):
    titulo: str
