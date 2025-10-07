import pytest


@pytest.mark.asyncio
async def test_algebra_expand(client):
    resp = await client.call_tool(
        "sympy_mcp_algebra_operation", {"operation": "expand", "expr": "(x + 1)**2"}
    )
    s = str(resp)
    assert "x**2" in s and "2*x" in s
