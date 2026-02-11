from fastmcp import FastMCP
from src.client import NpiClient, NpiWhere
from src.domain.models import SearchResponse, ErrorResponse

mcp = FastMCP("NPI MCP Server")


@mcp.tool(tags={"search", "npi"}, description="Lookup a provider by NPI number")
async def lookup_npi_number(npi_number: str) -> SearchResponse | ErrorResponse:
    client = NpiClient()
    result = await client.lookup(request=NpiWhere(npi_number=npi_number))
    return result


@mcp.tool(
    tags={"individual", "search"},
    description="Search for individual providers by name and state",
)
async def search_individual_providers(
    first_name: str, last_name: str, state: str
) -> SearchResponse | ErrorResponse:
    client = NpiClient()
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
    client = NpiClient()
    result = await client.lookup(
        request=NpiWhere(organization_name=organization_name, state=state)
    )
    return result
