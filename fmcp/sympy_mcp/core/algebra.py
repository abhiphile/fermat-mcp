from typing import List, Optional, Union, Literal, get_args
from sympy import (
    sympify,
    simplify as _simplify,
    expand as _expand,
    factor as _factor,
    collect as _collect,
)

# Define operation types for type hints
AlgebraOperation = Literal["simplify", "expand", "factor", "collect"]


def algebra_operation(
    operation: AlgebraOperation,
    expr: Union[str],
    syms: Optional[Union[str, List[str]]] = None,
    **kwargs,
) -> str:
    """
    Unified interface for algebra operations.

    Args:
        operation: The algebra operation to perform. One of:
            - 'simplify': Simplify the expression
            - 'expand': Expand the expression
            - 'factor': Factor the expression
            - 'collect': Collect terms with respect to symbols
        expr: The expression to process (string or SymPy expression)
        syms: Symbols to collect with respect to (only used for 'collect' operation)
        **kwargs: Additional arguments to pass to the underlying SymPy function

    Returns:
        str: The result of the operation as a string

    Examples:
        >>> algebra_operation('simplify', 'x**2 + 2*x + 1 + (x + 1)**2')
        '2*x**2 + 4*x + 2'
        >>> algebra_operation('collect', 'x*y + x - 3 + 2*x**2 - z*x**2 + x**3', 'x')
        'x**3 + x**2*(2 - z) + x*(y + 1) - 3'
    """
    # Convert string to SymPy expression if needed
    expr_obj = sympify(expr) if isinstance(expr, str) else expr

    # Process symbols if provided
    syms_list = None
    if syms is not None:
        if isinstance(syms, (str)):
            syms_list = [syms]
        elif isinstance(syms, list):
            syms_list = [sym for sym in syms]

    # Dispatch to the appropriate operation
    if operation == "simplify":
        return str(_simplify(expr_obj, **kwargs))
    elif operation == "expand":
        return str(_expand(expr_obj, **kwargs))
    elif operation == "factor":
        return str(_factor(expr_obj, **kwargs))
    elif operation == "collect":
        if syms_list is None:
            raise ValueError("Symbols must be provided for 'collect' operation")
        return str(_collect(expr_obj, syms_list, **kwargs))
    else:
        valid_ops = get_args(AlgebraOperation)
        raise ValueError(f"Invalid operation. Must be one of: {valid_ops}")
