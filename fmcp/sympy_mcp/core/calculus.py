from typing import Optional, Literal, get_args
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
    operation: CalculusOperation, expr: str, sym: Optional[str] = None, **kwargs
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
        **kwargs: Additional arguments to pass to the underlying SymPy function:
            - For 'diff':
                - n: int - Order of derivative (default: 1)
            - For 'integrate':
                - lower: Optional[Union[int, float, str]] - Lower limit for definite integral
                - upper: Optional[Union[int, float, str]] - Upper limit for definite integral
            - For 'limit':
                - point: Union[int, float, str] - The point to approach (default: 0)
                - dir: Literal['+', '-'] - Direction to approach from (default: '+')
            - For 'series':
                - point: Union[int, float, str] - The point about which to expand (default: 0)
                - n: int - Order of the series expansion (default: 6)

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
        n = kwargs.get("n", 1)
        if sym_obj is None:
            raise ValueError("Symbol must be provided for differentiation")
        return str(_diff(expr_obj, sym_obj, n, **kwargs))

    elif operation == "integrate":
        # Handle integration
        if sym_obj is None:
            raise ValueError("Symbol must be provided for integration")

        # Check for definite integral
        lower = kwargs.get("lower")
        upper = kwargs.get("upper")

        if lower is not None or upper is not None:
            # Definite integral
            lower = sympify(lower) if isinstance(lower, str) else lower
            upper = sympify(upper) if isinstance(upper, str) else upper
            return str(_integrate(expr_obj, (sym_obj, lower, upper), **kwargs))
        else:
            # Indefinite integral
            return str(_integrate(expr_obj, sym_obj, **kwargs))

    elif operation == "limit":
        # Handle limits
        if sym_obj is None:
            raise ValueError("Symbol must be provided for limit")

        point = kwargs.get("point", 0)
        direction = kwargs.get("dir", "+")

        # Convert point to SymPy expression if it's a string
        if isinstance(point, str):
            point = sympify(point)

        return str(_limit(expr_obj, sym_obj, point, direction, **kwargs))

    elif operation == "series":
        # Handle series expansion
        if sym_obj is None:
            raise ValueError("Symbol must be provided for series expansion")

        point = kwargs.get("point", 0)
        n = kwargs.get("n", 6)

        # Convert point to SymPy expression if it's a string
        if isinstance(point, str):
            point = sympify(point)

        return str(_series(expr_obj, sym_obj, point, n, **kwargs).removeO())

    else:
        valid_ops = get_args(CalculusOperation)
        raise ValueError(f"Invalid operation. Must be one of: {valid_ops}")
