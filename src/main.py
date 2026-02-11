from fastmcp import FastMCP
from src.client import NpiClient, NpiWhere
from src.domain.models import SearchResponse, ErrorResponse, Error
import re

mcp = FastMCP("NPI MCP Server")

_client: NpiClient | None = None


async def get_client() -> NpiClient:
    global _client
    if _client is None:
        _client = NpiClient()
    return _client


@mcp.tool(tags={"search", "npi"}, description="Lookup a provider by NPI number")
async def lookup_npi_number(npi_number: str) -> SearchResponse | ErrorResponse:
    if not re.match(r"^\d{10}$", npi_number):
        return ErrorResponse(
            Errors=[
                Error(
                    description="NPI must be exactly 10 digits",
                    field="npi_number",
                    number="VAL001",
                )
            ]
        )
    client = await get_client()
    result = await client.lookup(request=NpiWhere(npi_number=npi_number))
    return result


@mcp.tool(
    tags={"individual", "search"},
    description="Search for individual providers by name and state",
)
async def search_individual_providers(
    first_name: str, last_name: str, state: str
) -> SearchResponse | ErrorResponse:
    client = await get_client()
    result = await client.lookup(
        request=NpiWhere(first_name=first_name, last_name=last_name, state=state)
    )
    return result


@mcp.tool(
    tags={"organization", "search"},
    description="Search for organizations by name and state",
)
async def search_organizations(
    organization_name: str, state: str
) -> SearchResponse | ErrorResponse:
    client = await get_client()
    result = await client.lookup(
        request=NpiWhere(organization_name=organization_name, state=state)
    )
    return result
