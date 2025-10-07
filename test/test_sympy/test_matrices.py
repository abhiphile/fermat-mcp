import pytest


@pytest.mark.asyncio
async def test_matrix_det(client):
    resp = await client.call_tool(
        "sympy_mcp_matrix_operation",
        {"operation": "det", "data": [[4, 7], [2, 6]]},
    )

    # Extract numeric result: prefer structured .data, otherwise read text from content
    if hasattr(resp, "data") and resp.data is not None:
        val = resp.data
    else:
        # Try to pull text from the first content block
        try:
            val = resp.content[0].text
        except Exception:
            val = str(resp)

    assert float(str(val)) == pytest.approx(10.0)
