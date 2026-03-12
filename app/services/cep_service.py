import httpx
from fastapi import HTTPException
from app.config import VIA_CEP_API, BRASIL_API
from app.schemas.cep import CepResponse
import re

def normalize_cep(cep: str) -> str:
    return cep.replace("-", "").strip()

def validate_cep(cep: str) -> bool:
    verified_cep_format = re.match(r"^\d{5}-\d{3}$", cep)
    print("verified_cep_format", verified_cep_format)
    return bool(verified_cep_format)

async def get_cep_info(cep: str) -> CepResponse | dict:
    try:
        is_valid_cep = validate_cep(cep)
        if not is_valid_cep: raise HTTPException(status_code=400, detail="Invalid CEP")
        
        normalized_cep = normalize_cep(cep)
        async with httpx.AsyncClient() as client:
            via_cep_response = await client.get(f"{VIA_CEP_API}/{normalized_cep}/json/")
            brasil_cep_response = await client.get(f"{BRASIL_API}/{normalized_cep}")
            
            data_via_cep = via_cep_response.json()
            data_brasil_api = brasil_cep_response.json()

            coords = data_brasil_api.get("location", {}).get("coordinates", {})

            if not data_via_cep.get("erro"):
                return CepResponse(
                    cep=data_via_cep.get("cep", data_brasil_api.get("cep", "not found")),
                    street=data_via_cep.get("logradouro", data_brasil_api.get("street", "not found")),
                    neighborhood=data_via_cep.get("bairro", data_brasil_api.get("neighborhood", "not found")),
                    city=data_via_cep.get("localidade", data_brasil_api.get("city", "not found")),
                    state=data_via_cep.get("uf", data_brasil_api.get("state", "not found")),
                    source="Via Cep & Brasil API",
                    confidence_score=0.95,
                    normalized=True,
                    region=data_via_cep.get("regiao"),
                    ibge_code=data_via_cep.get("ibge"),
                    ddd=data_via_cep.get("ddd"),
                    latitude=float(coords.get("latitude")) if coords.get("latitude") else None,
                    longitude=float(coords.get("longitude")) if coords.get("longitude") else None,
                )
            else:
                raise HTTPException(status_code=404, detail="CEP not found")
    except HTTPException as http_exc:
        raise http_exc
    except Exception as e:
        raise HTTPException(status_code=500, detail="Internal server error")