import pytest
import sys
import os
from fastmcp import Client

# Add project root to Python path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from server import setup, app


@pytest.mark.asyncio
async def test_server_initialization():
    """
    Tests that the main fmcp server initializes correctly and all sub-servers are mounted.
    """
    await setup()  # Await the async setup
    async with Client(app) as client:
        tools = await client.list_tools()
        tool_names = [tool.name for tool in tools]
        print("Available tools:", tool_names)

        # Check that we have at least one tool from mpl_mcp (the only implemented server so far)
        assert any(
            name.startswith("mpl_mcp_") for name in tool_names
        ), f"Expected at least one mpl_mcp_* tool, but got: {tool_names}"
        assert any(
            name.startswith("numpy_mcp_") for name in tool_names
        ), f"Expected at least one numpy_mcp_* tool, but got: {tool_names}"
        assert any(
            name.startswith("sympy_mcp_") for name in tool_names
        ), f"Expected at least one sympy_mcp_* tool, but got: {tool_names}"
