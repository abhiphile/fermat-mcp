import numpy as np
from typing import Optional, Union


def matlib_operation(
    operation: str,
    data: Optional[Union[list, int, float]] = None,
    shape: Optional[Union[list, int]] = None,
    m: Optional[int] = None,
    n: Optional[int] = None,
    k: int = 0,
    start: Optional[float] = None,
    stop: Optional[float] = None,
    step: Optional[float] = None,
    num: Optional[int] = None,
    axis: int = 0,
) -> list:
    """
    Unified interface for numerical matrix operations using numpy.

    Args:
        operation: The matrix operation to perform. One of:
            - 'rand-mat': Matrix of random values (0-1) (m: int, n: int) -> 2D array
            - 'zeros': Matrix of zeros (shape: list) -> array
            - 'ones': Matrix of ones (shape: list) -> array
            - 'eye': 2D array with ones on diagonal (m: int, n: int, k: int) -> 2D array
            - 'identity': Identity matrix (n: int) -> 2D array
            - 'arange': Evenly spaced values (start: float, stop: float, step: float) -> 1D array
            - 'linspace': Evenly spaced numbers (start: float, stop: float, num: int) -> 1D array
            - 'reshape': Reshape array (data: list, shape: list) -> array
            - 'flatten': Flatten array (data: list) -> 1D array
            - 'concatenate': Join arrays (data: list[list], axis: int) -> array
            - 'transpose': Transpose array (data: list) -> array
            - 'stack': Stack arrays (data: list[list], axis: int) -> array

        data: Input data for matrix operations
        shape: Shape of the output matrix
        m: First dimension
        n: Second dimension
        k: Diagonal offset for eye operation
        start: Start value for arange/linspace
        stop: Stop value for arange/linspace
        step: Step size for arange
        num: Number of samples for linspace
        axis: Axis along which to perform operations

    Returns:
        list: The resulting matrix/array as a nested list
    """

    if operation == "zeros":
        return np.zeros(shape).tolist()

    elif operation == "ones":
        return np.ones(shape).tolist()

    elif operation == "eye":
        return np.eye(m or n, n, k).tolist()

    elif operation == "identity":
        return np.eye(n).tolist()

    elif operation == "rand-mat":
        return np.random.rand(m or 1, n or (m or 1)).tolist()

    elif operation == "arange":
        if start is None or stop is None:
            raise ValueError("start and stop are required for arange operation")
        if step is None:
            return np.arange(start, stop).tolist()
        return np.arange(start, stop, step).tolist()

    elif operation == "linspace":
        if start is None or stop is None or num is None:
            raise ValueError("start, stop, and num are required for linspace operation")
        return np.linspace(start, stop, num).tolist()

    elif operation == "reshape":
        if data is None or shape is None:
            raise ValueError("data and shape are required for reshape operation")
        return np.array(data).reshape(shape).tolist()

    elif operation == "flatten":
        if data is None:
            raise ValueError("data is required for flatten operation")
        return np.array(data).flatten().tolist()

    elif operation == "concatenate":
        if data is None:
            raise ValueError("data is required for concatenate operation")
        return np.concatenate([np.array(x) for x in data], axis=axis).tolist()

    elif operation == "transpose":
        if data is None:
            raise ValueError("data is required for transpose operation")
        return np.array(data).T.tolist()

    elif operation == "stack":
        if data is None:
            raise ValueError("data is required for stack operation")
        return np.stack([np.array(x) for x in data], axis=axis).tolist()

    else:
        raise ValueError(f"Unknown operation: {operation}")
