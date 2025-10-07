import pytest


@pytest.mark.asyncio
async def test_server_initialization(client):
    """Tests that the main fmcp server initializes correctly and all sub-servers are mounted."""
    tools = await client.list_tools()
    tool_names = [tool.name for tool in tools]
    print("Available tools:", tool_names)

    assert any(
        name.startswith("mpl_mcp_") for name in tool_names
    ), f"Expected at least one mpl_mcp_* tool, but got: {tool_names}"
    assert any(
        name.startswith("numpy_mcp_") for name in tool_names
    ), f"Expected at least one numpy_mcp_* tool, but got: {tool_names}"
    assert any(
        name.startswith("sympy_mcp_") for name in tool_names
    ), f"Expected at least one sympy_mcp_* tool, but got: {tool_names}"
