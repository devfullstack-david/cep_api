import httpx
from fastapi import HTTPException
from app.config import VIA_CEP_API, BRASIL_API
from app.schemas.cep import CepResponse
from app.exceptions.valid_cep import ValidCepException
from app.exceptions.cep_not_found import CepNotFoundException

def normalize_cep(cep: str) -> str:
    return cep.replace("-", "").strip()

def validate_cep(cep: str) -> None:
    is_valid_cep = len(cep) == 8 and cep.isdigit()
    if not is_valid_cep: ValidCepException()

async def get_cep_info(cep: str) -> CepResponse:
    normalized_cep = normalize_cep(cep)
    validate_cep(normalized_cep)
    
    try:
        async with httpx.AsyncClient() as client:
            via_cep_response = await client.get(f"{VIA_CEP_API}/{normalized_cep}/json/")
            brasil_cep_response = await client.get(f"{BRASIL_API}/{normalized_cep}")

            data_via_cep = via_cep_response.json()
            data_brasil_api = brasil_cep_response.json()

            coords = data_brasil_api.get("location", {}).get("coordinates", {})

            if not data_via_cep.get("erro"):
                return CepResponse(
                    data_via_cep.get("cep", data_brasil_api.get("cep", "not found")),
                    data_via_cep.get("logradouro", data_brasil_api.get("street", "not found")),
                    data_via_cep.get("bairro", data_brasil_api.get("neighborhood", "not found")),
                    data_via_cep.get("localidade", data_brasil_api.get("city", "not found")),
                    data_via_cep.get("uf", data_brasil_api.get("state", "not found")),
                    "Via Cep & Brasil API",
                    0.95,
                    True,
                    data_via_cep.get("regiao"),
                    data_via_cep.get("ibge"),
                    data_via_cep.get("ddd"),
                    latitude=float(coords.get("latitude")) if coords.get("latitude") else None,
                    longitude=float(coords.get("longitude")) if coords.get("longitude") else None,
                )
    except Exception as e:
        raise CepNotFoundException()