from pydantic import BaseModel, ConfigDict, Field
import datetime as dt
from src.domain.enums import (
    NpiSex,
    NpiStatus,
    NpiStateAbbreviation,
    NpiCountryAbbreviation,
    NpiEnumerationType,
)


class NpiBase(BaseModel):
    model_config = ConfigDict(from_attributes=True)


class ProviderResponse(NpiBase):
    number: str = Field(description="The 10-digit NPI number")
    enumeration_type: NpiEnumerationType = Field(description="The enumeration type")
    created_epoch: dt.datetime = Field(description="The created epoch")
    last_updated_epoch: dt.datetime = Field(description="The last updated epoch")
    basic: "PersonProvider | OrganizationProvider" = Field(
        description="The basic provider information"
    )
    addresses: list["Address"] | None = Field(default=None, description="The addresses")
    taxonomies: list["Taxonomy"] | None = Field(
        default=None, description="The taxonomies"
    )
    # identifiers: list["Identifier"] | None = Field(default=None, description="The identifiers")
    # other_names: list["OtherName"] | None = Field(default=None, description="The other names")
    # practiceLocations: list["PracticeLocation"] | None = Field(default=None, description="The practice locations")
    # endpoints: list["Endpoint"] | None = Field(default=None, description="The endpoints")


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
    enumeration_date: dt.date | None = Field(
        default=None, description="The enumeration date"
    )  # could be duplicate?
    last_updated: dt.date | None = Field(
        default=None, description="The last updated"
    )  # could be duplicate?
    status: NpiStatus | None = Field(
        default=None, description="The status"
    )  # TODO: enum - could be duplicate?


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
        default=None, description="The description - dervied from code"
    )
    primary: bool | None = Field(
        default=None, description="The primary taxonomy switch"
    )
    taxonomy_group: str | None = Field(description="The taxonomy group")


class Identifier(NpiBase):
    pass


class OtherName(NpiBase):
    pass


class Endpoint(NpiBase):
    pass


class SearchResponse(NpiBase):
    result_count: int = Field(description="The result count")
    results: list["ProviderResponse"] = Field(description="The results")


class ErrorResponse(NpiBase):
    errors: list["Error"] = Field(description="The errors")


class Error(NpiBase):
    description: str = Field(description="The description")
    field: str = Field(description="The field")
    number: str = Field(description="The number")


ProviderResponse.model_rebuild()
