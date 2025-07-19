from fastmcp import FastMCP
from fmcp.numpy_mcp.registration import register_functions

# Initialize the MCP server
numpy_mcp = FastMCP(
    name="numpy_mcp",
    instructions="""
        This server provides tools for numerical computation using NumPy.
        It includes various mathematical functions, array operations, and linear algebra utilities.
    """,
)

# Register all functions with the MCP server
register_functions(numpy_mcp)
