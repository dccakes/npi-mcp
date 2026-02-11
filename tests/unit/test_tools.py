import pytest
import pytest_asyncio
from fastmcp.client import Client
from fastmcp.client.transports import FastMCPTransport
from tests.conftest import vcr_instance
from src.main import mcp


@pytest_asyncio.fixture
async def main_mcp_client():
    async with Client(transport=mcp) as mcp_client:
        yield mcp_client


@pytest.mark.asyncio
async def test_list_tools(main_mcp_client: Client[FastMCPTransport]):
    list_tools = await main_mcp_client.list_tools()

    assert len(list_tools) == 3
    assert list_tools[0].name == "lookup_npi_number"
    assert list_tools[1].name == "search_individual_providers"
    assert list_tools[2].name == "search_organizations"


@pytest.mark.asyncio
@vcr_instance.use_cassette("search_by_npi_number_tool.yaml")
async def test_lookup_tool(main_mcp_client: Client[FastMCPTransport]):
    lookup_tool = await main_mcp_client.call_tool(
        name="lookup_npi_number",
        arguments={"npi_number": "1114382983"},
    )

    assert lookup_tool is not None
    print(lookup_tool)
    assert lookup_tool.is_error is False
