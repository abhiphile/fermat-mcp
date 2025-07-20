from typing import List, Optional, Union, Literal, get_args
from sympy import (
    Expr,
    Symbol,
    sympify,
    solve as _solve,
    solveset as _solveset,
    linsolve as _linsolve,
    Eq,
    FiniteSet,
)
from sympy.solvers.solveset import nonlinsolve as _nonlinsolve

# Define operation types for type hints
EquationOperation = Literal["solve", "solveset", "linsolve", "nonlinsolve"]


def _convert_to_set(result) -> str:
    """Convert various SymPy solution formats to a consistent string representation."""
    if result is None:
        return "[]"
    elif isinstance(result, (list, tuple, set, frozenset, FiniteSet)):
        return str(list(result))
    elif isinstance(result, dict):
        return str([{str(k): str(v) for k, v in result.items()}])
    elif hasattr(result, "args") and hasattr(result, "free_symbols"):
        # Handle SymPy solution sets
        return str([str(result)])
    return str(result)


def _parse_equations(equations: Union[str, List[str]]) -> List[Expr]:
    """Parse equations from various input formats."""
    if isinstance(equations, (str, Expr)):
        equations = [equations]

    parsed = []
    for eq in equations:
        if isinstance(eq, str):
            # Handle both 'x + y = 1' and 'Eq(x + y, 1)' formats
            if "=" in eq and not eq.strip().startswith("Eq("):
                left, right = eq.split("=", 1)
                parsed.append(Eq(sympify(left), sympify(right)))
            else:
                parsed.append(sympify(eq))
        else:
            parsed.append(eq)
    return parsed


def _parse_symbols(symbols: Union[str, List[str], None]) -> List[Symbol]:
    """Parse symbols from various input formats."""
    if symbols is None:
        return None

    if not isinstance(symbols, (list, tuple)):
        symbols = [symbols]

    return [sympify(sym) if isinstance(sym, str) else sym for sym in symbols]


def equation_operation(
    operation: EquationOperation,
    equations: Union[str, List[str]],
    symbols: Optional[Union[str, List[str]]] = None,
    # Common parameters
    domain: Optional[str] = None,
    # Additional parameters for specific solvers
    check: bool = True,
    simplify: bool = True,
    rational: Optional[bool] = None,
    minimal: bool = False,
    # Parameters for nonlinsolve
    force: bool = False,
    # Parameters for solveset
    implicit: bool = False,
) -> str:
    """
    Unified interface for equation solving operations.

    Args:
        operation: The equation operation to perform. One of:
            - 'solve': General purpose solver for algebraic equations
            - 'solveset': Solves equations with solution sets
            - 'linsolve': Solves system of linear equations
            - 'nonlinsolve': Solves system of nonlinear equations
        equations: The equation(s) to solve, as string(s) or SymPy expression(s)
        symbols: The variable(s) to solve for
        **kwargs: Additional arguments to pass to the underlying SymPy function:
            - For 'solve' and 'solveset':
                - domain: The domain for solving (default: complex numbers)
            - For 'linsolve' and 'nonlinsolve':
                - Additional arguments are passed to the respective solver

    Returns:
        str: The solution as a string in list format

    Examples:
        >>> equation_operation('solve', 'x**2 - 1', 'x')
        '[-1, 1]'
        >>> equation_operation('solveset', 'x**2 - 1', 'x')
        '{-1, 1}'
        >>> equation_operation('linsolve', ['x + y = 1', 'x - y = 0'], ['x', 'y'])
        '[(1/2, 1/2)]'
        >>> equation_operation('nonlinsolve', ['x**2 + y - 1', 'x - y'], ['x', 'y'])
        '[(-1/2 + sqrt(5)/2, -1/2 + sqrt(5)/2), (-sqrt(5)/2 - 1/2, -sqrt(5)/2 - 1/2)]'
    """
    # Parse input equations and symbols
    eqs = _parse_equations(equations)
    syms = _parse_symbols(symbols)

    # Handle different operations
    if operation == "solve":
        # General purpose solver
        if not syms:
            # Try to extract symbols automatically if not provided
            result = _solve(
                eqs,
                check=check,
                simplify=simplify,
                rational=rational,
                minimal=minimal,
                domain=domain,
            )
        else:
            result = _solve(
                eqs,
                syms,
                check=check,
                simplify=simplify,
                rational=rational,
                minimal=minimal,
                domain=domain,
            )

    elif operation == "solveset":
        # Solver that returns solution sets
        if not eqs:
            raise ValueError("At least one equation must be provided")
        if not syms:
            raise ValueError("Symbols must be provided for solveset")

        if len(eqs) > 1 or len(syms) > 1:
            # Handle multiple equations or symbols
            result = []
            for eq in eqs:
                for sym in syms:
                    result.append(
                        _solveset(
                            eq,
                            sym,
                            domain=domain,
                            check=check,
                            simplify=simplify,
                            implicit=implicit,
                        )
                    )
        else:
            result = _solveset(
                eqs[0],
                syms[0],
                domain=domain,
                check=check,
                simplify=simplify,
                implicit=implicit,
            )

    elif operation == "linsolve":
        # Linear system solver
        if not eqs:
            raise ValueError("At least one equation must be provided")

        # Convert to matrix form if needed
        if not syms:
            raise ValueError("Symbols must be provided for linsolve")

        # Convert to augmented matrix form if equations are in list form
        if all(isinstance(eq, Expr) for eq in eqs):
            # Equations are already in expression form
            result = _linsolve(eqs, *syms)
        else:
            # Try to convert string equations to matrix form
            A = []
            for eq in eqs:
                if isinstance(eq, str):
                    if "=" in eq:
                        left, right = eq.split("=", 1)
                        A.append(sympify(left) - sympify(right))
                    else:
                        A.append(sympify(eq))
                else:
                    A.append(eq)
            result = _linsolve(A, syms)

    elif operation == "nonlinsolve":
        # Nonlinear system solver
        if not eqs:
            raise ValueError("At least one equation must be provided")
        if not syms:
            raise ValueError("Symbols must be provided for nonlinsolve")

        result = _nonlinsolve(eqs, syms)

    else:
        valid_ops = get_args(EquationOperation)
        raise ValueError(f"Invalid operation. Must be one of: {valid_ops}")

    return _convert_to_set(result)
