import os
from dotenv import load_dotenv
from app.exceptions.missing_key_env import MissingKeyEnvException

load_dotenv()

base_url_via_cep = os.getenv("VIA_CEP_API")
base_url_brasil_api = os.getenv("BRASIL_API")

if not base_url_via_cep:
    raise MissingKeyEnvException("VIA_CEP_API")

if not base_url_brasil_api:
    raise MissingKeyEnvException("BRASIL_API")

VIA_CEP_API = base_url_via_cep
BRASIL_API = base_url_brasil_api
