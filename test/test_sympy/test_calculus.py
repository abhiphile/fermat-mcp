import pytest


@pytest.mark.asyncio
async def test_calculus_diff(client):
    resp = await client.call_tool(
        "sympy_mcp_calculus_operation",
        {"operation": "diff", "expr": "x**3 + 2*x", "sym": "x", "n": 1},
    )
    assert "3*x**2 + 2" in str(resp)
