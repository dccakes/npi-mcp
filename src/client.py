import httpx
from src.domain.models import SearchResponse, ErrorResponse
from src.domain.enums import NpiEnumerationType
from pydantic import BaseModel, Field


class NpiApiError(Exception):
    pass


class NpiSearchRequest(BaseModel):
    version: str = "2.1"

    limit: int = Field(default=10, description="The limit", ge=1, le=200)
    skip: int = Field(default=0, description="The skip", ge=0)


class NpiWhere(NpiSearchRequest):
    npi_number: str | None = Field(
        default=None, description="The NPI number", serialization_alias="number"
    )
    enumeration_type: NpiEnumerationType | None = None
    taxonomy_description: str | None = None
    first_name: str | None = None
    last_name: str | None = None
    organization_name: str | None = None
    city: str | None = None
    state: str | None = None
    postal_code: str | None = None
    country_code: str | None = None
    address_purpose: str | None = None


class NpiClient:
    def __init__(self):
        self.client = httpx.AsyncClient()
        self.base_url = "https://npiregistry.cms.hhs.gov/api/"
        self.version = "2.1"

    async def lookup(self, request: NpiWhere) -> SearchResponse | ErrorResponse:
        params = request.model_dump(exclude_none=True, by_alias=True)
        try:
            response = await self.client.get(self.base_url, params=params)
        except httpx.HTTPError as exc:  # network, timeout, DNS, etc.
            raise NpiApiError("Network error while calling NPI registry") from exc

        if response.status_code != 200:
            raise NpiApiError(f"Failed to lookup NPI: {response.status_code}")

        data = response.json()

        if "Errors" in data:
            return ErrorResponse.model_validate(data)

        return SearchResponse.model_validate(data)
