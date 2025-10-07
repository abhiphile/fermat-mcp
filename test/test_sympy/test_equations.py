import pytest


@pytest.mark.asyncio
async def test_equation_solve_quadratic(client):
    resp = await client.call_tool(
        "sympy_mcp_equation_operation",
        {"operation": "solve", "equations": "x**2 - 1", "symbols": "x"},
    )
    s = str(resp)
    assert "-1" in s and "1" in s
