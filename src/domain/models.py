from typing import Annotated, Literal

from pydantic import BaseModel, ConfigDict, Field, model_validator
import datetime as dt
from src.domain.enums import (
    NpiSex,
    NpiStatus,
    NpiStateAbbreviation,
    NpiCountryAbbreviation,
    NpiEnumerationType,
)


class NpiBase(BaseModel):
    model_config = ConfigDict(
        from_attributes=True,
        populate_by_name=True,
    )

    enumeration_date: dt.date | None = Field(
        default=None, description="The enumeration date"
    )
    last_updated: dt.date | None = Field(default=None, description="The last updated")
    status: NpiStatus | None = Field(default=None, description="The status")


class PersonProvider(NpiBase):
    first_name: str | None = Field(default=None, description="The first name")
    middle_name: str | None = Field(default=None, description="The middle name")
    last_name: str | None = Field(default=None, description="The last name")
    name_prefix: str | None = Field(default=None, description="The name prefix")
    name_suffix: str | None = Field(default=None, description="The name suffix")
    sex: NpiSex | None = Field(default=None, description="The sex")
    credential: str | None = Field(default=None, description="The credential")
    sole_proprietor: str | None = Field(
        default=None, description="The sole proprietor"
    )  # TODO: enum


class OrganizationProvider(NpiBase):
    organization_name: str | None = Field(
        default=None, description="The organization name"
    )
    organizational_subpart: str | None = Field(
        default=None, description="The organizational subpart"
    )
    # Authorized official fields
    authorized_official_first_name: str | None = Field(
        default=None, description="The authorized official first name"
    )
    authorized_official_middle_name: str | None = Field(
        default=None, description="The authorized official middle name"
    )
    authorized_official_last_name: str | None = Field(
        default=None, description="The authorized official last name"
    )
    authorized_official_name_prefix: str | None = Field(
        default=None, description="The authorized official name prefix"
    )
    authorized_official_name_suffix: str | None = Field(
        default=None, description="The authorized official name suffix"
    )
    authorized_official_title_or_position: str | None = Field(
        default=None, description="The authorized official title or position"
    )
    authorized_official_telephone_number: str | None = Field(
        default=None, description="The authorized official telephone number"
    )
    authorized_official_credential: str | None = Field(
        default=None, description="The authorized official credential"
    )


class _ProviderResponseBase(NpiBase):
    number: str = Field(description="The 10-digit NPI number")
    created_epoch: dt.datetime = Field(description="The created epoch")
    last_updated_epoch: dt.datetime = Field(description="The last updated epoch")
    addresses: list["Address"] = Field(
        default_factory=list, description="The addresses"
    )
    taxonomies: list["Taxonomy"] = Field(
        default_factory=list, description="The taxonomies"
    )
    identifiers: list["Identifier"] = Field(
        default_factory=list,
        description="Other identifiers (Medicaid, state licenses, etc.)",
    )
    other_names: list["OtherName"] = Field(
        default_factory=list,
        description="Alternative names (DBA, former names, etc.)",
    )
    endpoints: list["Endpoint"] = Field(
        default_factory=list,
        description="Health Information Exchange endpoints",
    )
    practice_locations: list["Address"] = Field(
        default_factory=list,
        description="Practice locations",
        alias="practiceLocations",
    )


class IndividualProviderResponse(_ProviderResponseBase):
    enumeration_type: Literal[NpiEnumerationType.NPI_1] = NpiEnumerationType.NPI_1
    basic: PersonProvider = Field(description="The basic provider information")


class OrganizationProviderResponse(_ProviderResponseBase):
    enumeration_type: Literal[NpiEnumerationType.NPI_2] = NpiEnumerationType.NPI_2
    basic: OrganizationProvider = Field(description="The basic provider information")


ProviderResponse = Annotated[
    IndividualProviderResponse | OrganizationProviderResponse,
    Field(discriminator="enumeration_type"),
]


class Address(NpiBase):
    address_1: str | None = Field(default=None, description="The address 1")
    address_2: str | None = Field(default=None, description="The address 2")
    city: str | None = Field(default=None, description="The city")
    state: NpiStateAbbreviation | None = Field(default=None, description="The state")
    postal_code: str | None = Field(default=None, description="The postal code")
    country_code: NpiCountryAbbreviation | None = Field(
        default=None, description="The country code"
    )
    country_name: str | None = Field(
        default=None, description="The country name - derived from country code"
    )
    address_type: str | None = Field(default=None, description="The address type")
    address_purpose: str | None = Field(default=None, description="The address purpose")
    address_telephone_number: str | None = Field(
        default=None, description="The address telephone number"
    )
    address_fax_number: str | None = Field(
        default=None, description="The address fax number"
    )


class Taxonomy(NpiBase):
    code: str = Field(description="The code")
    license: str | None = Field(default=None, description="The license")
    state: NpiStateAbbreviation | None = Field(default=None, description="The state")
    desc: str | None = Field(
        default=None, description="The description - derived from code"
    )
    primary: bool | None = Field(
        default=None, description="The primary taxonomy switch"
    )
    taxonomy_group: str | None = Field(description="The taxonomy group")


class Identifier(NpiBase):
    """Other identifiers for the provider (e.g., Medicaid, state license numbers)"""

    code: str = Field(description="The identifier type code")
    desc: str | None = Field(
        default=None, description="The identifier type description"
    )
    identifier: str = Field(description="The identifier value")
    issuer: str | None = Field(default=None, description="The issuing entity")
    state: NpiStateAbbreviation | None = Field(
        default=None, description="The state that issued the identifier"
    )


class OtherName(NpiBase):
    """Alternative names for organizations (DBA, former names, etc.)"""

    code: str = Field(description="The name type code")
    type: str | None = Field(
        default=None,
        description="The name type (e.g., 'Doing Business As', 'Former Legal Business Name')",
    )
    organization_name: str | None = Field(
        default=None, description="The alternative organization name"
    )
    first_name: str | None = Field(
        default=None, description="The alternative first name (for individuals)"
    )
    last_name: str | None = Field(
        default=None, description="The alternative last name (for individuals)"
    )
    middle_name: str | None = Field(
        default=None, description="The alternative middle name (for individuals)"
    )
    name_prefix: str | None = Field(
        default=None, description="The alternative name prefix"
    )
    name_suffix: str | None = Field(
        default=None, description="The alternative name suffix"
    )
    credential: str | None = Field(
        default=None, description="The alternative credential"
    )


class Endpoint(NpiBase):
    """Health Information Exchange endpoints (Direct messaging, FHIR, etc.)"""

    endpoint: str = Field(
        description="The endpoint URL or email address for HIE communication"
    )
    endpoint_type: str | None = Field(
        default=None,
        description="The endpoint type (e.g., 'DIRECT', 'FHIR', 'REST')",
        alias="endpointType",
    )
    endpoint_type_description: str | None = Field(
        default=None,
        description="Human-readable endpoint type description",
        alias="endpointTypeDescription",
    )
    endpoint_description: str | None = Field(
        default=None,
        description="Description of this specific endpoint",
        alias="endpointDescription",
    )
    affiliation: str | None = Field(
        default=None,
        description="Affiliation indicator (Y/N)",
    )
    use: str | None = Field(
        default=None,
        description="Use code (e.g., 'HIE' for Health Information Exchange)",
    )
    use_description: str | None = Field(
        default=None,
        description="Human-readable use description",
        alias="useDescription",
    )
    content_type: str | None = Field(
        default=None,
        description="Content type code (e.g., 'CSV', 'XML', 'JSON')",
        alias="contentType",
    )
    content_type_description: str | None = Field(
        default=None,
        description="Human-readable content type description",
        alias="contentTypeDescription",
    )
    # Address fields for the endpoint location
    address_1: str | None = Field(default=None, description="The address line 1")
    address_type: str | None = Field(
        default=None,
        description="The address type (DOM/FGN)",
        alias="address_type",
    )
    city: str | None = Field(default=None, description="The city")
    state: NpiStateAbbreviation | None = Field(default=None, description="The state")
    postal_code: str | None = Field(default=None, description="The postal code")
    country_code: NpiCountryAbbreviation | None = Field(
        default=None, description="The country code"
    )
    country_name: str | None = Field(default=None, description="The country name")


class SearchResponse(NpiBase):
    result_count: int = Field(description="The result count")
    results: list[ProviderResponse] = Field(description="The results")

    @model_validator(mode="before")
    @classmethod
    def coerce_enumeration_type_to_enum(cls, data: object) -> object:
        """Coerce raw API 'NPI-1'/'NPI-2' strings to enum so the discriminated union matches."""
        if not isinstance(data, dict) or "results" not in data:
            return data
        for result in data["results"]:  # type: ignore[union-attr]
            if isinstance(result, dict) and "enumeration_type" in result:
                raw = result["enumeration_type"]
                if isinstance(raw, str):
                    result["enumeration_type"] = NpiEnumerationType(raw)
        return data


class ErrorResponse(NpiBase):
    errors: list["Error"] = Field(description="The errors", alias="Errors")


class Error(NpiBase):
    description: str = Field(description="The description")
    field: str = Field(description="The field")
    number: str = Field(description="The number")


SearchResponse.model_rebuild()
