from fastmcp import FastMCP
from .core.bar_chart import plot_barchart
from .core.scatter_chart import plot_scatter
from .core.plot_chart import plot_chart
from .core.stem_chart import plot_stem
from .core.stack_chart import plot_stack
from .core.eqn_chart import eqn_chart


mpl_mcp = FastMCP(
    name="mpl_mcp",
    instructions="""
        This sever provides tools for plotting,
        both numerical and symbolic data.
    """,
)

# Register all the plotting tools
mpl_mcp.tool(plot_barchart, description="Plots barchart of given datavalues")
mpl_mcp.tool(plot_scatter, description="Plots scatter chart of given datavalues")
mpl_mcp.tool(plot_chart, description="Plots line/scatter/bar chart of given datavalues")
mpl_mcp.tool(plot_stem, description="Plots stem chart of given datavalues")
mpl_mcp.tool(plot_stack, description="Plots stacked area/bar chart of given datavalues")
mpl_mcp.tool(eqn_chart, description="Plots mathematical equations")
