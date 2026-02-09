import httpx
from src.domain.models import SearchResponse
from src.domain.enums import NpiEnumerationType
from pydantic import BaseModel, Field


class NpiSearchRequest(BaseModel):
    version: str = "2.1"


# limit: int = 10
# skip: int = 0


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

    async def lookup(self, request: NpiWhere) -> SearchResponse | None:
        params = request.model_dump(exclude_none=True, by_alias=True)
        response = await self.client.get(self.base_url, params=params)

        if response.status_code != 200:
            raise Exception(f"Failed to lookup NPI number: {response.status_code}")

        data = response.json()
        if data["result_count"] == 0:
            return None

        return SearchResponse.model_validate(data)
