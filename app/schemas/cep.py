from pydantic import BaseModel
from typing import Optional

class CepResponse(BaseModel):
    def __init__(
        self, 
        cep: str, 
        street: str, 
        neighborhood: str, 
        city: str, 
        state: str, 
        source: str,
        confidence_score: float,
        normalized: bool,
        region: Optional[str] = None, 
        ibge_code: Optional[str] = None,
        ddd: Optional[str] = None,
        latitude: Optional[str] = None,
        longitude: Optional[str] = None,
    ):
        self._cep = cep
        self._street = street
        self._neighborhood = neighborhood
        self._city = city
        self._state = state
        self._source = source
        self._confidence_score = confidence_score
        self._normalized = normalized
        self._region = region
        self._ibge_code = ibge_code
        self._ddd = ddd
        self._latitude = latitude
        self._longitude = longitude

    @property
    def cep(self) -> str:
        return self._cep

    @cep.setter
    def cep(self, cep: str):
        self._cep = cep

    @property
    def street(self) -> str:
        return self._street

    @street.setter
    def street(self, street: str):
        self._street = street

    @property
    def neighborhood(self) -> str:
        return self._neighborhood

    @neighborhood.setter
    def neighborhood(self, neighborhood: str):
        self._neighborhood = neighborhood

    @property
    def city(self) -> str:
        return self._city

    @city.setter
    def city(self, city: str):
        self._city = city

    @property
    def state(self) -> str:
        return self._state

    @state.setter
    def state(self, state: str):
        self._state = state

    @property
    def source(self) -> str:
        return self._source

    @source.setter
    def source(self, source: str):
        self._source = source

    @property
    def confidence_score(self) -> float:
        return self._confidence_score

    @confidence_score.setter
    def confidence_score(self, confidence_score: float):
        self._confidence_score = confidence_score

    @property
    def normalized(self) -> bool:
        return self._normalized

    @normalized.setter
    def normalized(self, normalized: bool):
        self._normalized = normalized

    @property
    def region(self) -> Optional[str]:
        return self._region

    @region.setter
    def region(self, region: Optional[str]):
        self._region = region

    @property
    def ibge_code(self) -> Optional[str]:
        return self._ibge_code

    @ibge_code.setter
    def ibge_code(self, ibge_code: Optional[str]):
        self._ibge_code = ibge_code

    @property
    def ddd(self) -> Optional[str]:
        return self._ddd

    @ddd.setter
    def ddd(self, ddd: Optional[str]):
        self._ddd = ddd

    @property
    def latitude(self) -> Optional[str]:
        return self._latitude

    @latitude.setter
    def latitude(self, latitude: Optional[str]):
        self._latitude = latitude

    @property
    def longitude(self) -> Optional[str]:
        return self._longitude

    @longitude.setter
    def longitude(self, longitude: Optional[str]):
        self._longitude = longitude