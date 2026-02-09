import httpx
from src.domain.models import SearchResponse


class NpiClient:
    def __init__(self):
        self.client = httpx.AsyncClient()
        self.base_url = "https://npiregistry.cms.hhs.gov/api/"
        self.version = "2.1"

    async def lookup(self, npi_number: str) -> SearchResponse | None:
        params = {"version": self.version, "number": npi_number}
        response = await self.client.get(self.base_url, params=params)

        if response.status_code != 200:
            raise Exception(f"Failed to lookup NPI number: {response.status_code}")

        data = response.json()
        if data["result_count"] == 0:
            return None

        return SearchResponse.model_validate(data)
