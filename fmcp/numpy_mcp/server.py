from fastmcp import FastMCP
from fmcp.numpy_mcp.core.numerical_operation import numerical_operation
from fmcp.numpy_mcp.core.matlib import matlib_operation

# Initialize the MCP server
numpy_mcp = FastMCP(
    name="numpy_mcp",
    instructions="""
        This server provides tools for numerical computation using NumPy.
        It includes various mathematical functions, array operations, and linear algebra utilities.
    """,
)

numpy_mcp.tool(
    numerical_operation,
    description="Do numerical operation like add, sub, mul, div, power, abs, exp, log, sqrt, sin, cos, tan, mean, median, std, var, min, max, argmin, argmax, percentile, dot, matmul, inv, det, eig, solve, svd",
)
numpy_mcp.tool(
    matlib_operation,
    description="Do matrix operations: rand-mat, zeros, ones, eye, identity, arange, linspace, reshape, flatten, concatenate, transpose, stack",
)
