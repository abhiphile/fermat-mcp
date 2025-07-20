from fastmcp import FastMCP
from fmcp.sympy_mcp.core.algebra import algebra_operation
from fmcp.sympy_mcp.core.calculus import calculus_operation
from fmcp.sympy_mcp.core.equations import equation_operation
from fmcp.sympy_mcp.core.matrices import matrix_operation

sympy_mcp = FastMCP(
    name="sympy_mcp",
    instructions="""
    This sever provides tools for symbolic computation.
    """,
)

sympy_mcp.tool(
    algebra_operation,
    description="Do algebraic operations like simplify, expand, factor, collect",
)
sympy_mcp.tool(
    calculus_operation,
    description="Do calculus operations like diff, integrate, limit, series",
)
sympy_mcp.tool(
    equation_operation,
    description="Do symbolic equation operations like solve, solveset, linsolve, nonlinsolve",
)
sympy_mcp.tool(
    matrix_operation,
    description="Do symbolic matrix operations like create, det, inv, rref, eigenvals",
)
# sympy_mcp.tool(sets_operation, description="Do set operations like union, intersection, difference, complement")
# sympy_mcp.tool(geometry_operation, description="Do geometry operations like distance, midpoint, slope, angle")
# sympy_mcp.tool(logic_operation, description="Do logic operations like and, or, not, xor")
# sympy_mcp.tool(evaluation_operation, description="Do evaluation operations like subs, evalf, N")
