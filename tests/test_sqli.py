import pytest
from core.plugins import sqli

@pytest.mark.asyncio
async def test_sqli_scan():
    result = await sqli.scan("https://demo.testfire.net", {"timeout": 5})
    assert result is None  # Replace with actual assertion
