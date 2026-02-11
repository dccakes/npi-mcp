from fastmcp import FastMCP
from src.client import NpiClient, NpiWhere
from src.domain.models import SearchResponse, ErrorResponse

mcp = FastMCP("NPI MCP Server")


@mcp.tool
async def lookup_tool(where: NpiWhere) -> SearchResponse | ErrorResponse:
    client = NpiClient()
    result = await client.lookup(request=where)
    return result
