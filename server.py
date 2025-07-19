from fastmcp import FastMCP
from fmcp.mpl_mcp.server import mpl_mcp
from fmcp.numpy_mcp.server import numpy_mcp
from fmcp.sympy_mcp.server import sympy_mcp
import asyncio

app = FastMCP(
    name="fmcp",
    instructions="""
    This MCP server is for mathematical calculations (both numerical and symbolic)
    and plotting.
    ---
    
    For Plotting use prefix : mpl_mcp
    For numerical Computation use prefix : numpy_mcp
    For Symbolic Computation use prefix : sympy_mcp 
    
    """,
)


async def setup():
    # Mount each server
    await app.import_server(mpl_mcp, prefix="mpl_mcp")
    await app.import_server(numpy_mcp, prefix="numpy_mcp")
    await app.import_server(sympy_mcp, prefix="sympy_mcp")


if __name__ == "__main__":
    asyncio.run(setup())
    app.run(transport="stdio")
