import vcr
from pydantic_settings import BaseSettings


class TestSettings(BaseSettings):
    vcr_cassette_library_dir: str = "tests/cassettes"
    vcr_record_mode: str = "none"

    class ConfigDict:
        env_file = "envs/.env.test"
        env_file_encoding = "utf-8"


settings = TestSettings()

# Use a different name so we don't shadow the vcr module (fixes type checker)
vcr_instance: vcr.VCR = vcr.VCR(
    cassette_library_dir=settings.vcr_cassette_library_dir,
    record_mode=settings.vcr_record_mode,
    match_on=["method", "scheme", "host", "port", "path", "query"],
    filter_query_parameters=[],
    decode_compressed_response=True,
)
