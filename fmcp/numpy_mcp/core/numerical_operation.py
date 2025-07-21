import numpy as np
from typing import Optional, Union


def numerical_operation(
    operation: str,
    a: Optional[Union[list, float, int]] = None,
    b: Optional[Union[list, float, int]] = None,
    shape: Optional[list] = None,
    new_shape: Optional[list] = None,
    axis: int = 0,
    q: Optional[float] = None,
    start: Optional[float] = None,
    stop: Optional[float] = None,
    step: Optional[float] = 1.0,
    num: Optional[int] = None,
    fill_value: Optional[float] = None,
) -> Union[list, float, int, dict]:
    """
    Unified interface for numerical operations using numpy.

    Args:
        operation: The operation to perform. One of:
            - 'create_array': Convert list to array (a: list)
            - 'zeros': Array of zeros (shape: list)
            - 'ones': Array of ones (shape: list)
            - 'full': Array filled with value (shape: list, fill_value: float)
            - 'arange': Evenly spaced values (start: float, stop: float, step: float)
            - 'linspace': Evenly spaced samples (start: float, stop: float, num: int)
            - 'reshape': Reshape array (a: list, new_shape: list)
            - 'flatten': Flatten array (a: list)
            - 'concatenate': Join arrays (a: list[list], axis: int)
            - 'transpose': Transpose array (a: list)
            - 'stack': Stack arrays (a: list[list], axis: int)
            - 'add': Element-wise addition (a: list, b: list)
            - 'subtract': Element-wise subtraction (a: list, b: list)
            - 'multiply': Element-wise multiplication (a: list, b: list)
            - 'divide': Element-wise division (a: list, b: list)
            - 'power': Element-wise power (a: list, b: list)
            - 'abs_val': Absolute value (a: list)
            - 'exp': Exponential (a: list)
            - 'log': Natural logarithm (a: list)
            - 'sqrt': Square root (a: list)
            - 'sin': Sine (a: list)
            - 'cos': Cosine (a: list)
            - 'tan': Tangent (a: list)
            - 'mean': Mean (a: list)
            - 'median': Median (a: list)
            - 'std': Standard deviation (a: list)
            - 'var': Variance (a: list)
            - 'min_val': Minimum value (a: list)
            - 'max_val': Maximum value (a: list)
            - 'argmin': Index of minimum (a: list)
            - 'argmax': Index of maximum (a: list)
            - 'percentile': Percentile (a: list, q: float)
            - 'dot': Dot product (a: list, b: list)
            - 'matmul': Matrix multiplication (a: list, b: list)
            - 'inv': Matrix inverse (a: list)
            - 'det': Matrix determinant (a: list)
            - 'eig': Eigenvalues/vectors (a: list)
            - 'eigenvals': Eigenvalues only (a: list)
            - 'solve': Solve linear system (a: list, b: list)
            - 'svd': Singular Value Decomposition (a: list)
        a: First input array or value
        b: Second input array or value (for binary operations)
        shape: Shape of the output array (for creation operations)
        new_shape: New shape for reshape operation
        axis: Axis along which to perform operations (default: 0)
        q: Percentile value (0-100) for percentile operation
        start: Start value for arange/linspace
        stop: Stop value for arange/linspace
        step: Step size for arange (default: 1.0)
        num: Number of samples for linspace
        fill_value: Fill value for 'full' operation

    Returns:
        Result of the operation, type depends on operation
    """
    a_array = np.array(a) if a is not None else None
    b_array = np.array(b) if b is not None else None

    if operation == "create_array":
        return a_array.tolist()
    elif operation == "zeros":
        return np.zeros(shape).tolist()
    elif operation == "ones":
        return np.ones(shape).tolist()
    elif operation == "full":
        return np.full(shape, fill_value).tolist()
    elif operation == "arange":
        return np.arange(start, stop, step).tolist()
    elif operation == "linspace":
        return np.linspace(start, stop, num).tolist()
    elif operation == "reshape":
        return a_array.reshape(new_shape).tolist()
    elif operation == "flatten":
        return a_array.ravel().tolist()
    elif operation == "concatenate":
        return np.concatenate([np.array(arr) for arr in a], axis=axis).tolist()
    elif operation == "transpose":
        return a_array.T.tolist()
    elif operation == "stack":
        return np.stack([np.array(arr) for arr in a], axis=axis).tolist()
    elif operation == "add":
        return (a_array + b_array).tolist()
    elif operation == "subtract":
        return (a_array - b_array).tolist()
    elif operation == "multiply":
        return (a_array * b_array).tolist()
    elif operation == "divide":
        return (a_array / b_array).tolist()
    elif operation == "power":
        return np.power(a_array, b_array).tolist()
    elif operation == "abs_val":
        return np.abs(a_array).tolist()
    elif operation == "exp":
        return np.exp(a_array).tolist()
    elif operation == "log":
        return np.log(a_array).tolist()
    elif operation == "sqrt":
        return np.sqrt(a_array).tolist()
    elif operation == "sin":
        return np.sin(a_array).tolist()
    elif operation == "cos":
        return np.cos(a_array).tolist()
    elif operation == "tan":
        return np.tan(a_array).tolist()
    elif operation == "mean":
        return float(np.mean(a_array))
    elif operation == "median":
        return float(np.median(a_array))
    elif operation == "std":
        return float(np.std(a_array))
    elif operation == "var":
        return float(np.var(a_array))
    elif operation == "min_val":
        return float(np.min(a_array))
    elif operation == "max_val":
        return float(np.max(a_array))
    elif operation == "argmin":
        return int(np.argmin(a_array))
    elif operation == "argmax":
        return int(np.argmax(a_array))
    elif operation == "percentile":
        return float(np.percentile(a_array, q))
    elif operation == "dot":
        return float(np.dot(a_array, b_array))
    elif operation == "matmul":
        return np.matmul(a_array, b_array).tolist()
    elif operation == "inv":
        return np.linalg.inv(a_array).tolist()
    elif operation == "det":
        return float(np.linalg.det(a_array))
    elif operation == "eig":
        vals, vecs = np.linalg.eig(a_array)
        return {"eigenvalues": vals.tolist(), "eigenvectors": vecs.tolist()}
    elif operation == "eigenvals":
        vals = np.linalg.eigvals(a_array)
        return vals.tolist()
    elif operation == "solve":
        return np.linalg.solve(a_array, b_array).tolist()
    elif operation == "svd":
        U, S, Vt = np.linalg.svd(a_array)
        return {"U": U.tolist(), "S": S.tolist(), "Vt": Vt.tolist()}
    else:
        raise ValueError(f"Unknown operation: {operation}")
