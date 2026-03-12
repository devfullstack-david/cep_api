from pydantic import BaseModel
from typing import Optional

class CepResponse(BaseModel):
    cep: str
    street: str
    neighborhood: str
    city: str
    state: str
    source: str
    confidence_score: float
    normalized: bool
    region: Optional[str] = None
    ibge_code: Optional[str] = None
    ddd: Optional[str] = None
    latitude: Optional[float] = None
    longitude: Optional[float] = None