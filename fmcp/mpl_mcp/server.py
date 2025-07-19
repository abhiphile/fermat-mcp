from fastmcp import FastMCP
from fmcp.mpl_mcp.core.bar_chart import plot_barchart

mpl_mcp = FastMCP(
    name="mpl_mcp",
    instructions="""
        This sever provides tools for plotting,
        both numerical and symbolic data.
    """,
)

mpl_mcp.tool(plot_barchart, description="Plots barchart of given datavalues")
