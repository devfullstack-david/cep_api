from pydantic_settings import BaseSettings
from functools import lru_cache


class Settings(BaseSettings):
    VIA_CEP_API: str
    BRASIL_API: str

    model_config = {"env_file": ".env"}


@lru_cache
def get_settings() -> Settings:
    return Settings()
