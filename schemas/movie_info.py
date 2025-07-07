from pydantic import BaseModel, validator
from typing import Optional


class MovieInfo(BaseModel):
    data_lancamento: str
    bilheteria: str
    sinopse: str
    erro: Optional[str] = None

    @validator('data_lancamento', 'bilheteria', 'sinopse', pre=True, always=True)
    def not_empty(cls, v, field):
        if v is None or (isinstance(v, str) and not v.strip()):
            raise ValueError(f'O campo "{field.name}" não pode estar vazio.')
        return v
