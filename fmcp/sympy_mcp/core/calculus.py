from typing import Optional, Literal, get_args, Union
from sympy import (
    sympify,
    diff as _diff,
    integrate as _integrate,
    limit as _limit,
    series as _series,
)

# Define operation types for type hints
CalculusOperation = Literal["diff", "integrate", "limit", "series"]


def calculus_operation(
    operation: CalculusOperation,
    expr: str,
    sym: Optional[str] = None,
    # diff parameters
    n: int = 1,
    # integrate parameters
    lower: Optional[Union[int, float, str]] = None,
    upper: Optional[Union[int, float, str]] = None,
    # limit parameters
    point: Union[int, float, str] = 0,
    direction: Literal["+", "-"] = "+",
    # series parameters
    series_n: int = 6,
) -> str:
    """
    Unified interface for calculus operations.

    Args:
        operation: The calculus operation to perform. One of:
            - 'diff': Differentiate the expression
            - 'integrate': Integrate the expression
            - 'limit': Compute the limit of the expression
            - 'series': Compute the series expansion of the expression
        expr: The expression to process as a string
        sym: The symbol to differentiate/integrate with respect to, or the variable for limits/series
        n: Order of derivative for 'diff' or order of series expansion for 'series' (default: 1 for 'diff', 6 for 'series')
        lower: Lower limit for definite integral (only for 'integrate')
        upper: Upper limit for definite integral (only for 'integrate')
        point: The point to approach for 'limit' or about which to expand for 'series' (default: 0)
        direction: Direction to approach from for 'limit' ('+' or '-', default: '+')

    Returns:
        str: The result of the operation as a string

    Examples:
        >>> calculus_operation('diff', 'x**2 + 2*x + 1', 'x')
        '2*x + 2'
        >>> calculus_operation('integrate', '2*x + 2', 'x')
        'x**2 + 2*x'
        >>> calculus_operation('limit', 'sin(x)/x', 'x', point=0)
        '1'
        >>> calculus_operation('series', 'exp(x)', 'x', point=0, n=3)
        '1 + x + x**2/2 + O(x**3)'
    """
    # Convert string to SymPy expression
    expr_obj = sympify(expr)

    # Convert symbol string to Symbol if provided
    sym_obj = sympify(sym) if sym is not None else None

    if operation == "diff":
        # Handle differentiation
        if sym_obj is None:
            raise ValueError("Symbol must be provided for differentiation")
        return str(_diff(expr_obj, sym_obj, n))

    elif operation == "integrate":
        # Handle integration
        if sym_obj is None:
            raise ValueError("Symbol must be provided for integration")

        # Check for definite integral
        if lower is not None or upper is not None:
            # Definite integral
            lower_val = sympify(lower) if isinstance(lower, str) else lower
            upper_val = sympify(upper) if isinstance(upper, str) else upper
            return str(_integrate(expr_obj, (sym_obj, lower_val, upper_val)))
        else:
            # Indefinite integral
            return str(_integrate(expr_obj, sym_obj))

    elif operation == "limit":
        # Handle limits
        if sym_obj is None:
            raise ValueError("Symbol must be provided for limit")

        # Convert point to SymPy expression if it's a string
        point_val = sympify(point) if isinstance(point, str) else point

        return str(_limit(expr_obj, sym_obj, point_val, direction))

    elif operation == "series":
        # Handle series expansion
        if sym_obj is None:
            raise ValueError("Symbol must be provided for series expansion")

        # Convert point to SymPy expression if it's a string
        point_val = sympify(point) if isinstance(point, str) else point

        return str(_series(expr_obj, sym_obj, point_val, series_n).removeO())

    else:
        valid_ops = get_args(CalculusOperation)
        raise ValueError(f"Invalid operation. Must be one of: {valid_ops}")
