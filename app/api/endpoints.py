import httpx
from fastapi import APIRouter, Request, Depends
from slowapi import Limiter
from slowapi.util import get_remote_address

from app.schemas.cep import CepResponse
from app.services.cep_service import get_cep_info

router = APIRouter()
limiter = Limiter(key_func=get_remote_address)


async def get_http_client(request: Request) -> httpx.AsyncClient:
    return request.app.state.http_client


@router.get(
    "/cep/{cep}",
    response_model=CepResponse,
    summary="Consultar CEP",
    description="Retorna dados completos de endereço, coordenadas e metadados a partir de um CEP brasileiro.",
    responses={
        400: {"description": "CEP com formato inválido"},
        404: {"description": "CEP não encontrado nas bases de dados"},
        429: {"description": "Limite de requisições excedido"},
    },
)

@limiter.limit("30/minute")
async def get_cep(
    request: Request, cep: str, client: httpx.AsyncClient = Depends(get_http_client)
):
    return await get_cep_info(cep, client)


@router.get(
    "/health",
    summary="Health Check",
    description="Verifica se a API está operacional.",
)
async def health_check():
    return {"status": "ok"}