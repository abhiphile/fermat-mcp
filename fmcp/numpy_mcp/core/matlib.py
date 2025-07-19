import numpy.matlib as matlib


def mat_matrix(data: list) -> list:
    """mat_matrix(data: list) -> list: Return a matrix from an array-like object."""
    return matlib.matrix(data).tolist()


def mat_asmatrix(data: list) -> list:
    """mat_asmatrix(data: list) -> list: Interpret the input as a matrix."""
    return matlib.asmatrix(data).tolist()


def mat_bmat(data: list) -> list:
    """mat_bmat(data: list) -> list: Build a matrix object from a string, nested sequence, or array."""
    return matlib.bmat(data).tolist()


def mat_empty(shape: list) -> list:
    """mat_empty(shape: list) -> list: Return a new matrix of given shape and type, without initializing entries."""
    return matlib.empty(shape).tolist()


def mat_zeros(shape: list) -> list:
    """mat_zeros(shape: list) -> list: Return a matrix of given shape and type, filled with zeros."""
    return matlib.zeros(shape).tolist()


def mat_ones(shape: list) -> list:
    """mat_ones(shape: list) -> list: Matrix of ones."""
    return matlib.ones(shape).tolist()


def mat_eye(n: int, m: int = None, k: int = 0) -> list:
    """mat_eye(n: int, m: int = None, k: int = 0) -> list: Return a 2-D array with ones on the diagonal and zeros elsewhere."""
    return matlib.eye(n, M=m, k=k).tolist()


def mat_identity(n: int) -> list:
    """mat_identity(n: int) -> list: Return the identity matrix."""
    return matlib.identity(n).tolist()


def mat_repmat(a: list, m: int, n: int) -> list:
    """mat_repmat(a: list, m: int, n: int) -> list: Repeat a 0-D to 2-D array or matrix MxN times."""
    return matlib.repmat(a, m, n).tolist()


def mat_rand(shape: list[int]) -> list:
    """mat_rand(shape: list[int]) -> list: Return a matrix of random values with given shape."""
    return matlib.rand(*shape).tolist()


def mat_randn(shape: list[int]) -> list:
    """mat_randn(shape: list[int]) -> list: Return a matrix of random values from a standard normal distribution."""
    return matlib.randn(*shape).tolist()
