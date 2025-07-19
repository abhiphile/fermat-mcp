import numpy as np


def mat_matrix(data: list) -> list:
    """mat_matrix(data: list) -> list: Return a matrix from an array-like object."""
    return np.array(data).tolist()


def mat_asmatrix(data: list) -> list:
    """mat_asmatrix(data: list) -> list: Interpret the input as a matrix."""
    return np.asarray(data).tolist()


def mat_bmat(data: list) -> list:
    """mat_bmat(data: list) -> list: Build a matrix object from a string, nested sequence, or array."""
    # Convert list of lists to numpy arrays, then use block to create the matrix
    if isinstance(data[0][0], (list, np.ndarray)):
        blocks = [[np.asarray(block) for block in row] for row in data]
        return np.block(blocks).tolist()
    return np.asarray(data).tolist()


def mat_empty(shape: list) -> list:
    """mat_empty(shape: list) -> list: Return a new array of given shape and type, without initializing entries."""
    return np.empty(shape).tolist()


def mat_zeros(shape: list) -> list:
    """mat_zeros(shape: list) -> list: Return an array of given shape and type, filled with zeros."""
    return np.zeros(shape).tolist()


def mat_ones(shape: list) -> list:
    """mat_ones(shape: list) -> list: Array of ones."""
    return np.ones(shape).tolist()


def mat_eye(n: int, m: int = None, k: int = 0) -> list:
    """mat_eye(n: int, m: int = None, k: int = 0) -> list: Return a 2-D array with ones on the diagonal and zeros elsewhere."""
    return np.eye(n, m, k).tolist()


def mat_identity(n: int) -> list:
    """mat_identity(n: int) -> list: Return the identity matrix."""
    return np.eye(n).tolist()


def mat_repmat(a: list, m: int, n: int) -> list:
    """mat_repmat(a: list, m: int, n: int) -> list: Repeat a 0-D to 2-D array or matrix MxN times."""
    a = np.asarray(a)
    return np.tile(a, (m, n)).tolist()


def mat_rand(shape: list[int]) -> list:
    """mat_rand(shape: list[int]) -> list: Return a matrix of random values with given shape."""
    return np.random.random(shape).tolist()


def mat_randn(shape: list[int]) -> list:
    """mat_randn(shape: list[int]) -> list: Return a matrix of random values from a standard normal distribution."""
    return np.random.standard_normal(shape).tolist()
