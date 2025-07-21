import numpy as np
from typing import Optional, Union


def matlib_operation(
    operation: str,
    data: Optional[Union[list, int]] = None,
    shape: Optional[Union[list, int]] = None,
    m: Optional[int] = None,
    n: Optional[int] = None,
    k: int = 0,
) -> list:
    """
    Unified interface for numerical matrix operations using numpy.

    Args:
        operation: The matrix operation to perform. One of:
            - 'rand-mat': Matrix of random values (0-1) (data: None, shape: list)
            - 'matrix': Create a matrix from data (data: list[list], shape: list)
            - 'asmatrix': Interpret input as a matrix (data: list[list], shape: list)
            - 'bmat': Build a matrix from nested blocks (data: list[list[list]], shape: list)
            - 'empty': Uninitialized matrix of given shape (data: None, shape: list)
            - 'zeros': Matrix of zeros (data: None, shape: list)
            - 'ones': Matrix of ones (data: None, shape: list)
            - 'eye': 2D array with ones on diagonal (data: None, shape: list, m: int, n: int, k: int)
            - 'identity': Identity matrix (data: None, shape: list, m: int, n: int)
            - 'repmat': Repeat array MxN times (data: list[list], shape: list, m: int, n: int)

        data: Input data for matrix operations
        shape: Shape of the output matrix
        m: First dimension or repetition count
        n: Second dimension
        k: Diagonal offset for eye operation
    Returns:
        list: The resulting matrix as a nested list
    """
    if operation == "matrix":
        return np.array(data).tolist()

    elif operation == "asmatrix":
        return np.asarray(data).tolist()

    elif operation == "bmat":
        if isinstance(data[0][0], (list, np.ndarray)):
            blocks = [[np.asarray(block) for block in row] for row in data]
            return np.block(blocks).tolist()
        return np.asarray(data).tolist()

    elif operation == "empty":
        return np.empty(shape).tolist()

    elif operation == "zeros":
        return np.zeros(shape).tolist()

    elif operation == "ones":
        return np.ones(shape).tolist()

    elif operation == "eye":
        return np.eye(m or n, n, k).tolist()

    elif operation == "identity":
        return np.eye(m or n).tolist()

    elif operation == "repmat":
        a = np.asarray(data)
        return np.tile(a, (m, n)).tolist()

    elif operation == "rand-mat":
        return np.random.rand(n, m).tolist()

    else:
        raise ValueError(f"Unknown operation: {operation}")
