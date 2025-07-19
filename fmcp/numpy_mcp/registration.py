"""
Registration module for NumPy MCP server.

This module handles the registration of all NumPy functions and utilities
with the FastMCP server.
"""

from fastmcp import FastMCP
from .core.math_functions import (
    create_array,
    zeros,
    ones,
    full,
    arange,
    linspace,
    reshape,
    flatten,
    concatenate,
    transpose,
    stack,
    add,
    subtract,
    multiply,
    divide,
    power,
    abs_val,
    exp,
    log,
    sqrt,
    sin,
    cos,
    tan,
    mean,
    median,
    std,
    var,
    min_val,
    max_val,
    argmin,
    argmax,
    percentile,
    dot,
    matmul,
    inv,
    det,
    eig,
    solve,
    svd,
)

from .core.matlib import (
    mat_matrix,
    mat_asmatrix,
    mat_bmat,
    mat_empty,
    mat_zeros,
    mat_ones,
    mat_eye,
    mat_identity,
    mat_repmat,
    mat_rand,
    mat_randn,
)


def register_functions(mcp_instance: FastMCP) -> None:
    """
    Register all NumPy functions with the MCP server.

    Args:
        mcp_instance: An instance of FastMCP to register the functions with.
    """
    functions_to_register = [
        # Math functions
        create_array,
        zeros,
        ones,
        full,
        arange,
        linspace,
        reshape,
        flatten,
        concatenate,
        transpose,
        stack,
        add,
        subtract,
        multiply,
        divide,
        power,
        abs_val,
        exp,
        log,
        sqrt,
        sin,
        cos,
        tan,
        mean,
        median,
        std,
        var,
        min_val,
        max_val,
        argmin,
        argmax,
        percentile,
        dot,
        matmul,
        inv,
        det,
        eig,
        solve,
        svd,
        # Matrix library functions
        mat_matrix,
        mat_asmatrix,
        mat_bmat,
        mat_empty,
        mat_zeros,
        mat_ones,
        mat_eye,
        mat_identity,
        mat_repmat,
        mat_rand,
        mat_randn,
    ]

    for func in functions_to_register:
        mcp_instance.tool(func)

    # Register the MCP instance itself if needed
    mcp_instance.tool()
