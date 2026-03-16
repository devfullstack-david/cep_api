from pydantic import BaseModel, Field
from typing import Optional


class CepResponse(BaseModel):
    cep: str = Field(..., description="CEP formatado", examples=["01001-000"])
    street: str = Field(
        ..., min_length=1, description="Logradouro", examples=["Praça da Sé"]
    )
    neighborhood: str = Field(
        ..., min_length=1, description="Bairro", examples=["Sé"]
    )
    city: str = Field(
        ..., min_length=1, description="Cidade", examples=["São Paulo"]
    )
    state: str = Field(
        ..., min_length=2, max_length=2, description="UF", examples=["SP"]
    )
    source: str = Field(
        ..., description="Fonte dos dados", examples=["ViaCEP & BrasilAPI"]
    )
    confidence_score: float = Field(
        ..., ge=0.0, le=1.0, description="Grau de confiança", examples=[0.95]
    )
    normalized: bool = Field(
        ..., description="Se o CEP foi normalizado", examples=[True]
    )
    region: Optional[str] = Field(
        None, description="Região do Brasil", examples=["Sudeste"]
    )
    ibge_code: Optional[str] = Field(
        None, description="Código IBGE do município", examples=["3550308"]
    )
    ddd: Optional[str] = Field(
        None, description="DDD da localidade", examples=["11"]
    )
    latitude: Optional[float] = Field(
        None, description="Latitude", examples=[-23.5505]
    )
    longitude: Optional[float] = Field(
        None, description="Longitude", examples=[-46.6333]
    )