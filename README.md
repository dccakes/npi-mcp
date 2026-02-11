# NPI MCP Server

An MCP (Model Context Protocol) server that provides tools for searching the National Provider Identifier (NPI) Registry. This server enables AI assistants to look up healthcare providers and organizations from the NPPES database.

## Deployment

The server is deployed at: **https://dc-npi-mcp.fastmcp.app/mcp**

## Overview

The NPI Registry is maintained by CMS (Centers for Medicare & Medicaid Services) and contains information about all healthcare providers in the United States. This MCP server wraps the public NPI Registry API and provides three tools for searching provider data:

- **lookup_npi_number** - Look up a provider by their 10-digit NPI number
- **search_individual_providers** - Search for individual providers by name and state
- **search_organizations** - Search for healthcare organizations by name and state

## Tools

### lookup_npi_number

Look up a specific provider by their NPI number.

**Parameters:**
- `npi_number` (string): The 10-digit NPI number

**Example:**
```json
{
  "npi_number": "1234567890"
}
```

### search_individual_providers

Search for individual healthcare providers by name and state.

**Parameters:**
- `first_name` (string): Provider's first name
- `last_name` (string): Provider's last name
- `state` (string): US state abbreviation (e.g., "NY", "CA")

**Example:**
```json
{
  "first_name": "John",
  "last_name": "Smith",
  "state": "NY"
}
```

### search_organizations

Search for healthcare organizations by name and state.

**Parameters:**
- `organization_name` (string): Name of the organization
- `state` (string): US state abbreviation (e.g., "NY", "CA")

**Example:**
```json
{
  "organization_name": "Acme Health",
  "state": "CA"
}
```

## Development

### Requirements

- Python 3.12 or higher
- Dependencies are managed via `pyproject.toml`

### Installation

```bash
# Clone the repository
git clone <repository-url>
cd npi-mcp

# Install dependencies
pip install -e .

# Install development dependencies
pip install -e ".[dev]"
```

### Running Locally

```bash
# Run the MCP server in development mode with the inspector
fastmcp dev src/main.py

# Or run in production mode
fastmcp run src/main.py
```

### Testing

```bash
# Run tests
pytest

# Run tests with coverage
pytest --cov=src tests/
```

## API Reference

This server uses the public NPPES NPI Registry API:
- **Base URL**: https://npiregistry.cms.hhs.gov/api/
- **Authentication**: None required
- **Rate Limits**: No documented limits (be respectful of government resources)
- **API Version**: 2.1

For detailed API documentation, see [docs/02-npi-api-reference.md](docs/02-npi-api-reference.md).

## Response Format

All tools return either a `SearchResponse` with provider results or an `ErrorResponse` if the search fails.

**SearchResponse:**
```json
{
  "result_count": 15,
  "results": [
    {
      "number": "1234567890",
      "enumeration_type": "NPI-1",
      "basic": {
        "first_name": "JOHN",
        "last_name": "SMITH",
        "credential": "MD"
      },
      "addresses": [...],
      "taxonomies": [...]
    }
  ]
}
```

**ErrorResponse:**
```json
{
  "Errors": [
    {
      "description": "No valid search criteria provided",
      "field": "generic",
      "number": "04"
    }
  ]
}
```

## Project Structure

```
npi-mcp/
├── src/
│   ├── main.py           # MCP server definition and tools
│   ├── client.py         # NPI Registry API client
│   └── domain/
│       ├── models.py     # Pydantic models for requests/responses
│       └── enums.py      # Enumerations (states, taxonomy, etc.)
├── tests/
│   ├── unit/             # Unit tests
│   └── integration/      # Integration tests
├── docs/                 # Additional documentation
└── pyproject.toml        # Project dependencies and metadata
```

## Contributing

1. Create a feature branch
2. Make your changes
3. Run tests and ensure they pass
4. Submit a pull request

## License

[Add license information here]

## Resources

- [NPI Registry Website](https://npiregistry.cms.hhs.gov/)
- [NPI Registry API Documentation](https://npiregistry.cms.hhs.gov/api-page)
- [FastMCP Documentation](https://github.com/jlowin/fastmcp)
- [Model Context Protocol](https://modelcontextprotocol.io/)
