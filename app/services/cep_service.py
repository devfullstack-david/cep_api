import asyncio
import re
import httpx
from fastapi import HTTPException
from app.config import get_settings
from app.schemas.cep import CepResponse


def normalize_cep(cep: str) -> str:
    return cep.replace("-", "").strip()


def validate_cep(cep: str) -> bool:
    return bool(re.match(r"^\d{5}-?\d{3}$", cep))


async def get_cep_info(cep: str, client: httpx.AsyncClient) -> CepResponse:
    if not validate_cep(cep):
        raise HTTPException(status_code=400, detail="Invalid CEP")

    settings = get_settings()
    normalized_cep = normalize_cep(cep)

    try:
        via_resp, brasil_resp = await asyncio.gather(
            client.get(f"{settings.VIA_CEP_API}/{normalized_cep}/json/"),
            client.get(f"{settings.BRASIL_API}/{normalized_cep}"),
        )

        data_via_cep = via_resp.json()
        data_brasil_api = brasil_resp.json()

        coords = data_brasil_api.get("location", {}).get("coordinates", {})

        if data_via_cep.get("erro"):
            raise HTTPException(status_code=404, detail="CEP not found")

        return CepResponse(
            cep=data_via_cep.get("cep", data_brasil_api.get("cep", "not found")),
            street=data_via_cep.get(
                "logradouro", data_brasil_api.get("street", "not found")
            ),
            neighborhood=data_via_cep.get(
                "bairro", data_brasil_api.get("neighborhood", "not found")
            ),
            city=data_via_cep.get(
                "localidade", data_brasil_api.get("city", "not found")
            ),
            state=data_via_cep.get(
                "uf", data_brasil_api.get("state", "not found")
            ),
            source="ViaCEP & BrasilAPI",
            confidence_score=0.95,
            normalized=True,
            region=data_via_cep.get("regiao"),
            ibge_code=data_via_cep.get("ibge"),
            ddd=data_via_cep.get("ddd"),
            latitude=float(coords.get("latitude"))
            if coords.get("latitude")
            else None,
            longitude=float(coords.get("longitude"))
            if coords.get("longitude")
            else None,
        )
    except HTTPException:
        raise
    except Exception:
        raise HTTPException(status_code=500, detail="Internal server error")