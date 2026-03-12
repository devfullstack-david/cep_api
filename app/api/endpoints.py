from fastapi import APIRouter
from app.schemas.cep import CepResponse
from app.services.cep_service import get_cep_info

router = APIRouter()

@router.get("/cep/{cep}", response_model=CepResponse)
async def get_cep(cep: str):
    return await get_cep_info(cep)