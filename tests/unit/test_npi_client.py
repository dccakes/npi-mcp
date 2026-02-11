import pytest

from tests.conftest import vcr_instance
from src.client import NpiClient
from src.domain.models import (
    NpiEnumerationType,
    IndividualProviderResponse,
    OrganizationProviderResponse,
    ErrorResponse,
    SearchResponse,
)
from src.client import NpiWhere, NpiApiError
from datetime import date
from src.domain.enums import NpiStatus
from pytest_httpx import HTTPXMock
import httpx


@pytest.mark.asyncio
@vcr_instance.use_cassette("search_by_npi_number.yaml")
async def test_search_by_npi_number():
    client = NpiClient()
    request = NpiWhere(npi_number="1114382983")
    result = await client.lookup(request)
    assert result is not None
    assert isinstance(result, SearchResponse)
    assert result.result_count == 1
    assert len(result.results) == 1
    assert isinstance(result.results[0], IndividualProviderResponse)
    assert result.results[0].number == "1114382983"
    assert result.results[0].enumeration_type == NpiEnumerationType.NPI_1
    assert result.results[0].basic.first_name == "JONATHON"
    assert result.results[0].basic.last_name == "LEE"
    assert result.results[0].basic.enumeration_date == date(2015, 12, 22)
    assert result.results[0].basic.status == NpiStatus.A


@pytest.mark.asyncio
@vcr_instance.use_cassette("search_by_name.yaml")
async def test_search_by_name():
    client = NpiClient()
    request = NpiWhere(first_name="JONATHON", last_name="LEE", state="OR", limit=2)
    result = await client.lookup(request)
    assert result is not None
    assert isinstance(result, SearchResponse)
    assert result.result_count == 1
    assert len(result.results) == 1
    assert isinstance(result.results[0], IndividualProviderResponse)
    assert result.results[0].number == "1114382983"
    assert result.results[0].enumeration_type == NpiEnumerationType.NPI_1
    assert result.results[0].basic.first_name == "JONATHON"
    assert result.results[0].basic.last_name == "LEE"


@pytest.mark.asyncio
@vcr_instance.use_cassette("search_by_name_no_results.yaml")
async def test_search_by_name_no_results():
    client = NpiClient()
    request = NpiWhere(first_name="JONATHON", last_name="LEE", state="NY")
    result = await client.lookup(request)
    print(result)
    assert isinstance(result, SearchResponse)
    assert result is not None
    assert result.result_count == 0
    assert len(result.results) == 0
    assert isinstance(result.results, list)
    assert result.results == []


@pytest.mark.asyncio
@vcr_instance.use_cassette("search_by_organization_name.yaml")
async def test_search_by_organization_name():
    client = NpiClient()
    request = NpiWhere(
        organization_name="H2 REHABILITATION SERVICES OF VA", limit=3, state="VA"
    )
    result = await client.lookup(request)
    assert result is not None
    assert isinstance(result, SearchResponse)
    assert result.result_count == 1
    assert len(result.results) == 1
    assert isinstance(result.results[0], OrganizationProviderResponse)
    assert result.results[0].number == "1508906702"
    assert result.results[0].enumeration_type == NpiEnumerationType.NPI_2
    assert (
        result.results[0].basic.organization_name
        == "H2 REHABILITATION SERVICES OF VIRGINIA, LLC"
    )
    assert result.results[0].basic.authorized_official_first_name == "AMANDA"
    assert result.results[0].basic.authorized_official_last_name == "STREETER"
    assert (
        result.results[0].basic.authorized_official_title_or_position
        == "Vice President"
    )
    assert result.results[0].basic.enumeration_date == date(2007, 2, 7)
    assert result.results[0].basic.status == NpiStatus.A

    # Test other_names (alternative names)
    assert len(result.results[0].other_names) >= 2
    # Find the "Doing Business As" name
    dba_names = [
        n
        for n in result.results[0].other_names
        if "H2 HEALTH" in (n.organization_name or "")
    ]
    assert len(dba_names) >= 1
    assert dba_names[0].organization_name == "H2 HEALTH"


@pytest.mark.asyncio
@vcr_instance.use_cassette("search_with_error.yaml")
async def test_search_with_error():
    client = NpiClient()
    request = NpiWhere()
    response = await client.lookup(request)
    assert response is not None
    assert isinstance(response, ErrorResponse)
    assert len(response.errors) == 1
    assert response.errors[0].description == "No valid search criteria provided"
    assert response.errors[0].field == "generic"
    assert response.errors[0].number == "04"


@pytest.mark.asyncio
async def test_exception_raising(httpx_mock: HTTPXMock):
    httpx_mock.add_exception(httpx.TimeoutException("timeout"))

    client = NpiClient()
    request = NpiWhere(first_name="Jane", last_name="Doe", state="NY")
    with pytest.raises(NpiApiError):
        await client.lookup(request)
