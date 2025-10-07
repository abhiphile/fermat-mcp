import os
from fastmcp import FastMCP
from fmcp.mpl_mcp.server import mpl_mcp
from fmcp.numpy_mcp.server import numpy_mcp
from fmcp.sympy_mcp.server import sympy_mcp
import asyncio

__all__ = ["app", "setup"]

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


def main():
    # Mount and set up all sub-servers first
    asyncio.run(setup())

    # If running inside a Smithery deployment, run the full app over HTTP
    if os.environ.get("SMITHERY_DEPLOYMENT"):
        # In containerized Smithery deployments the platform provides a PORT
        # environment variable (defaults to 8081). Bind to 0.0.0.0 so the
        # container is reachable from outside.
        port = int(os.environ.get("PORT", "8081"))
        host = os.environ.get("HOST", "0.0.0.0")
        try:
            app.run(transport="http", host=host, port=port)
        except TypeError:
            # Fallback if FastMCP.run doesn't accept host/port kwargs
            # (older versions). In that case we rely on the default HTTP
            # binding behavior of FastMCP and assume it reads PORT itself.
            app.run(transport="http")
    else:
        app.run(transport="stdio")


if __name__ == "__main__":
    main()
