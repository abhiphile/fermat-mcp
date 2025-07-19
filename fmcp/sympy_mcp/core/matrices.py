from typing import List, Union, Literal, get_args, Dict, Any, Tuple
from sympy import Matrix, sympify, nsimplify

# Define operation types for type hints
MatrixOperation = Literal["create", "det", "inv", "rref", "eigenvals"]


def _parse_matrix_data(data: Union[List, Tuple, str]) -> List[List[Any]]:
    """Parse matrix data from various input formats."""
    if isinstance(data, str):
        # Handle string input like "1 2; 3 4" or "[1, 2] [3, 4]"
        if ";" in data:
            # Handle MATLAB-style format: "1 2; 3 4"
            rows = [row.strip() for row in data.split(";") if row.strip()]
            return [[sympify(x) for x in row.split()] for row in rows]
        else:
            # Handle list of lists format: "[1, 2] [3, 4]"
            import ast

            try:
                # Try to parse as a list of lists
                parsed = ast.literal_eval("[" + data.replace(" ", ",") + "]")
                if all(isinstance(row, (list, tuple)) for row in parsed):
                    return [[sympify(x) for x in row] for row in parsed]
                elif all(not isinstance(x, (list, tuple)) for x in parsed):
                    # Single row matrix
                    return [[sympify(x) for x in parsed]]
            except (ValueError, SyntaxError):
                pass

            # Try space-separated values
            return [
                [sympify(x) for x in row.split()]
                for row in data.split("\n")
                if row.strip()
            ]

    # Handle list/tuple input
    if all(isinstance(row, (list, tuple)) for row in data):
        return [[sympify(x) for x in row] for row in data]
    elif all(not isinstance(x, (list, tuple)) for x in data):
        # Single row matrix
        return [[sympify(x) for x in data]]

    raise ValueError("Invalid matrix format")


def _convert_to_json_serializable(obj):
    """Convert SymPy objects to JSON-serializable types."""
    if hasattr(obj, "as_immutable"):
        return str(obj)
    elif isinstance(obj, (list, tuple)):
        return [_convert_to_json_serializable(x) for x in obj]
    elif isinstance(obj, dict):
        return {str(k): _convert_to_json_serializable(v) for k, v in obj.items()}
    return obj


def matrix_operation(
    operation: MatrixOperation, data: Union[str, List, Tuple], **kwargs
) -> Union[Dict, List, str, float]:
    """
    Unified interface for matrix operations.

    Args:
        operation: The matrix operation to perform. One of:
            - 'create': Create a matrix from data
            - 'det': Calculate the determinant
            - 'inv': Calculate the inverse
            - 'rref': Compute reduced row echelon form
            - 'eigenvals': Compute eigenvalues
        data: The matrix data in one of these formats:
            - String: "1 2; 3 4" or "[1, 2] [3, 4]"
            - List of lists: [[1, 2], [3, 4]]
            - Single list: [1, 2, 3, 4] (will be converted to a row matrix)
        **kwargs: Additional arguments:
            - For 'create':
                - 'rational': If True, convert to rational numbers (default: True)
                - 'nrows', 'ncols': For creating matrices of specific dimensions

    Returns:
        The result of the operation in a JSON-serializable format.
        For 'create', returns the matrix as a list of lists.
        For 'det', returns the determinant as a float or symbolic expression.
        For 'inv', returns the inverse matrix as a list of lists.
        For 'rref', returns a tuple (RREF_matrix, pivot_columns).
        For 'eigenvals', returns a dictionary of eigenvalues with multiplicities.

    Examples:
        >>> matrix_operation('create', '1 2; 3 4')
        [[1, 2], [3, 4]]
        >>> matrix_operation('det', [[1, 2], [3, 4]])
        -2
        >>> matrix_operation('inv', '1 2; 3 4')
        [[-2.0, 1.0], [1.5, -0.5]]
        >>> matrix_operation('rref', '1 2 3; 4 5 6')
        ([[1, 0, -1], [0, 1, 2]], (0, 1))
        >>> matrix_operation('eigenvals', '3 -2; 4 -1')
        {'1 - 2*I': 1, '1 + 2*I': 1}
    """
    # Parse matrix data
    matrix_data = _parse_matrix_data(data)

    # Create matrix, optionally converting to rational numbers
    rational = kwargs.get("rational", True)
    if rational:
        matrix = Matrix(matrix_data).applyfunc(lambda x: nsimplify(x, rational=True))
    else:
        matrix = Matrix(matrix_data)

    # Perform the requested operation
    if operation == "create":
        return _convert_to_json_serializable(matrix.tolist())

    elif operation == "det":
        det = matrix.det()
        # Try to convert to float if it's a simple number
        try:
            return float(det.evalf())
        except (TypeError, AttributeError):
            return str(det)

    elif operation == "inv":
        try:
            inv_matrix = matrix.inv()
            return _convert_to_json_serializable(inv_matrix.tolist())
        except ValueError as e:
            if "matrix is not invertible" in str(e).lower():
                raise ValueError("Matrix is not invertible (determinant is zero)")
            raise

    elif operation == "rref":
        rref_matrix, pivot_columns = matrix.rref()
        return (
            _convert_to_json_serializable(rref_matrix.tolist()),
            tuple(pivot_columns),
        )

    elif operation == "eigenvals":
        try:
            eigenvals = matrix.eigenvals()
            # Convert to a serializable format
            result = {}
            for val, mult in eigenvals.items():
                key = str(val)
                # Try to simplify complex expressions
                if "I" in key and " " not in key:
                    key = key.replace("*I", "j").replace("I", "j")
                result[key] = int(mult)
            return result
        except Exception as e:
            raise ValueError(f"Failed to compute eigenvalues: {str(e)}")

    else:
        valid_ops = get_args(MatrixOperation)
        raise ValueError(f"Invalid operation. Must be one of: {valid_ops}")
