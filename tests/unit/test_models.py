from datetime import datetime, timezone

from src.domain.enums import (
    NpiCountryAbbreviation,
    NpiEnumerationType,
    NpiStateAbbreviation,
)
from src.domain.models import (
    IndividualProviderResponse,
    OrganizationProviderResponse,
    PersonProvider,
    OrganizationProvider,
    Address,
    Taxonomy,
    SearchResponse,
    ErrorResponse,
    Error,
)

_EPOCH = datetime.fromtimestamp(1717987200, tz=timezone.utc)


def test_person_provider_result_parsing():
    result = IndividualProviderResponse(
        number="1234567890",
        enumeration_type=NpiEnumerationType.NPI_1,
        created_epoch=_EPOCH,
        last_updated_epoch=_EPOCH,
        basic=PersonProvider(
            first_name="John",
            last_name="Doe",
        ),
    )
    assert result.number == "1234567890"
    assert result.basic.first_name == "John"
    assert result.basic.last_name == "Doe"


def test_organization_provider_result_parsing():
    result = OrganizationProviderResponse(
        number="1234567890",
        enumeration_type=NpiEnumerationType.NPI_2,
        created_epoch=_EPOCH,
        last_updated_epoch=_EPOCH,
        basic=OrganizationProvider(
            organization_name="Acme Health Clinic",
        ),
    )
    assert result.number == "1234567890"
    assert result.basic.organization_name == "Acme Health Clinic"


def test_basic_address_parsing():
    result = Address(
        address_1="123 Main St",
        address_2="Suite 100",
        city="New York",
        state=NpiStateAbbreviation.NY,
        postal_code="10010",
        country_code=NpiCountryAbbreviation.US,
        country_name="United States",
        address_type="DOM",
        address_purpose="LOCATION",
        address_telephone_number="212-555-0100",
        address_fax_number="212-555-0101",
    )
    assert result.address_1 == "123 Main St"
    assert result.address_2 == "Suite 100"
    assert result.city == "New York"
    assert result.state is not None and result.state.value == "NY"
    assert result.postal_code == "10010"
    assert result.country_code is not None and result.country_code.value == "US"
    assert result.country_name == "United States"
    assert result.address_type == "DOM"
    assert result.address_purpose == "LOCATION"


def test_basic_taxonomy_parsing():
    result = Taxonomy(
        code="207R00000X",
        desc="Internal Medicine",
        primary=True,
        state=NpiStateAbbreviation.NY,
        license="123456",
        taxonomy_group="",
    )
    assert result.code == "207R00000X"
    assert result.desc == "Internal Medicine"
    assert result.primary is True
    assert result.state is not None and result.state.value == "NY"
    assert result.license == "123456"
    assert result.taxonomy_group == ""


def test_search_response_parsing():
    result = SearchResponse(
        result_count=1,
        results=[
            IndividualProviderResponse(
                number="1234567890",
                enumeration_type=NpiEnumerationType.NPI_1,
                created_epoch=_EPOCH,
                last_updated_epoch=_EPOCH,
                basic=PersonProvider(
                    first_name="John",
                    last_name="Doe",
                ),
            ),
        ],
    )
    assert result.result_count == 1
    assert len(result.results) == 1
    assert isinstance(result.results[0], IndividualProviderResponse)
    assert result.results[0].number == "1234567890"
    assert result.results[0].enumeration_type.value == "NPI-1"
    assert result.results[0].created_epoch.timestamp() == 1717987200.0
    assert result.results[0].last_updated_epoch.timestamp() == 1717987200.0
    assert result.results[0].basic.first_name == "John"
    assert result.results[0].basic.last_name == "Doe"


def test_error_response_parsing():
    result = ErrorResponse(
        Errors=[
            Error(
                description="Invalid request",
                field="first_name",
                number="01",
            ),
        ],
    )
    assert len(result.errors) == 1
    assert result.errors[0].description == "Invalid request"
    assert result.errors[0].field == "first_name"
    assert result.errors[0].number == "01"


def test_identifier_parsing():
    """Test parsing of provider identifiers"""
    from src.domain.models import Identifier
    from src.domain.enums import NpiStateAbbreviation

    data = {
        "code": "05",
        "desc": "MEDICAID",
        "identifier": "001289017",
        "issuer": None,
        "state": "CT",
    }
    identifier = Identifier.model_validate(data)
    assert identifier.code == "05"
    assert identifier.desc == "MEDICAID"
    assert identifier.identifier == "001289017"
    assert identifier.state == NpiStateAbbreviation.CT


def test_other_name_parsing():
    """Test parsing of alternative names"""
    from src.domain.models import OtherName

    data = {
        "code": "3",
        "organization_name": "H2 HEALTH",
        "type": "Doing Business As",
    }
    other_name = OtherName.model_validate(data)
    assert other_name.code == "3"
    assert other_name.type == "Doing Business As"
    assert other_name.organization_name == "H2 HEALTH"


def test_endpoint_parsing():
    """Test parsing of HIE endpoints"""
    from src.domain.models import Endpoint
    from src.domain.enums import NpiStateAbbreviation, NpiCountryAbbreviation

    data = {
        "address_1": "1047 Oakwood Ave",
        "address_type": "DOM",
        "affiliation": "N",
        "city": "Des Plaines",
        "contentType": "CSV",
        "contentTypeDescription": "CSV",
        "country_code": "US",
        "country_name": "United States",
        "endpoint": "john.oplawski@uprisedirect.com",
        "endpointDescription": "secure email address",
        "endpointType": "DIRECT",
        "endpointTypeDescription": "Direct Messaging Address",
        "postal_code": "600166332",
        "state": "IL",
        "use": "HIE",
        "useDescription": "Health Information Exchange (HIE)",
    }
    endpoint = Endpoint.model_validate(data)
    assert endpoint.endpoint == "john.oplawski@uprisedirect.com"
    assert endpoint.endpoint_type == "DIRECT"
    assert endpoint.endpoint_type_description == "Direct Messaging Address"
    assert endpoint.use == "HIE"
    assert endpoint.state == NpiStateAbbreviation.IL
    assert endpoint.country_code == NpiCountryAbbreviation.US
