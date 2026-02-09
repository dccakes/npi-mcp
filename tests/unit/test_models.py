from src.domain.models import (
    ProviderResponse,
    PersonProvider,
    OrganizationProvider,
    Address,
    Taxonomy,
    SearchResponse,
    ErrorResponse,
    Error,
)


def test_person_provider_result_parsing():
    result = ProviderResponse(
        number="1234567890",
        enumeration_type="NPI-1",
        created_epoch="1717987200",
        last_updated_epoch="1717987200",
        basic=PersonProvider(
            first_name="John",
            last_name="Doe",
        ),
    )
    assert result.number == "1234567890"
    assert result.basic.first_name == "John"
    assert result.basic.last_name == "Doe"


def test_organization_provider_result_parsing():
    result = ProviderResponse(
        number="1234567890",
        enumeration_type="NPI-2",
        created_epoch="1717987200",
        last_updated_epoch="1717987200",
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
        state="NY",
        postal_code="10010",
        country_code="US",
        country_name="United States",
        address_type="DOM",
        address_purpose="LOCATION",
        address_telephone_number="212-555-0100",
        address_fax_number="212-555-0101",
    )
    assert result.address_1 == "123 Main St"
    assert result.address_2 == "Suite 100"
    assert result.city == "New York"
    assert result.state.value == "NY"
    assert result.postal_code == "10010"
    assert result.country_code.value == "US"
    assert result.country_name == "United States"
    assert result.address_type == "DOM"
    assert result.address_purpose == "LOCATION"


def test_basic_taxonomy_parsing():
    result = Taxonomy(
        code="207R00000X",
        desc="Internal Medicine",
        primary=True,
        state="NY",
        license="123456",
        taxonomy_group="",
    )
    assert result.code == "207R00000X"
    assert result.desc == "Internal Medicine"
    assert result.primary is True
    assert result.state.value == "NY"
    assert result.license == "123456"
    assert result.taxonomy_group == ""


def test_search_response_parsing():
    result = SearchResponse(
        result_count=1,
        results=[
            ProviderResponse(
                number="1234567890",
                enumeration_type="NPI-1",
                created_epoch="1717987200",
                last_updated_epoch="1717987200",
                basic=PersonProvider(
                    first_name="John",
                    last_name="Doe",
                ),
            ),
        ],
    )
    assert result.result_count == 1
    assert len(result.results) == 1
    assert result.results[0].number == "1234567890"
    assert result.results[0].enumeration_type.value == "NPI-1"
    assert result.results[0].created_epoch.timestamp() == 1717987200.0
    assert result.results[0].last_updated_epoch.timestamp() == 1717987200.0
    assert result.results[0].basic.first_name == "John"
    assert result.results[0].basic.last_name == "Doe"


def test_error_response_parsing():
    result = ErrorResponse(
        errors=[
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
