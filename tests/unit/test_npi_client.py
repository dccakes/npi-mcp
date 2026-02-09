import pytest

from tests.conftest import vcr_instance
from src.client import NpiClient
from src.domain.models import NpiEnumerationType, IndividualProviderResponse


@pytest.mark.asyncio
@vcr_instance.use_cassette("search_by_npi_number.yaml")
async def test_search_by_npi_number():
    client = NpiClient()
    result = await client.lookup("1114382983")
    assert result is not None
    assert result.result_count == 1
    assert len(result.results) == 1
    assert isinstance(result.results[0], IndividualProviderResponse)
    assert result.results[0].number == "1114382983"
    assert result.results[0].enumeration_type == NpiEnumerationType.NPI_1
    assert result.results[0].basic.first_name == "JONATHON"
    assert result.results[0].basic.last_name == "LEE"
