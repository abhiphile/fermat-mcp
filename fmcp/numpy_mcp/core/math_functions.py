import numpy as np


def create_array(data: list) -> list:
    """create_array(data: list) -> list: Convert a list to a NumPy array and back to list."""
    return np.array(data).tolist()


def zeros(shape: list) -> list:
    """zeros(shape: list) -> list: Return a new array of given shape filled with zeros."""
    return np.zeros(shape).tolist()


def ones(shape: list) -> list:
    """ones(shape: list) -> list: Return a new array of given shape filled with ones."""
    return np.ones(shape).tolist()


def full(shape: list, fill_value: float) -> list:
    """full(shape: list, fill_value: float) -> list: Return a new array of given shape filled with fill_value."""
    return np.full(shape, fill_value).tolist()


def arange(start: float, stop: float, step: float = 1.0) -> list:
    """arange(start: float, stop: float, step: float = 1.0) -> list: Return evenly spaced values within a given interval."""
    return np.arange(start, stop, step).tolist()


def linspace(start: float, stop: float, num: int) -> list:
    """linspace(start: float, stop: float, num: int) -> list: Return num evenly spaced samples over interval [start, stop]."""
    return np.linspace(start, stop, num).tolist()


def reshape(array: list, new_shape: list) -> list:
    """reshape(array: list, new_shape: list) -> list: Reshape an array to a new shape."""
    return np.array(array).reshape(new_shape).tolist()


def flatten(array: list) -> list:
    """flatten(array: list) -> list: Flatten an array into 1D."""
    return np.ravel(array).tolist()


def concatenate(arrays: list, axis: int = 0) -> list:
    """concatenate(arrays: list, axis: int = 0) -> list: Join arrays along an existing axis."""
    return np.concatenate([np.array(arr) for arr in arrays], axis=axis).tolist()


def transpose(array: list) -> list:
    """transpose(array: list) -> list: Reverse or permute the axes of an array."""
    return np.transpose(array).tolist()


def stack(arrays: list, axis: int = 0) -> list:
    """stack(arrays: list, axis: int = 0) -> list: Join arrays along a new axis."""
    return np.stack([np.array(arr) for arr in arrays], axis=axis).tolist()


def add(a: list, b: list) -> list:
    """add(a: list, b: list) -> list: Element-wise addition of two arrays."""
    return (np.array(a) + np.array(b)).tolist()


def subtract(a: list, b: list) -> list:
    """subtract(a: list, b: list) -> list: Element-wise subtraction of two arrays."""
    return (np.array(a) - np.array(b)).tolist()


def multiply(a: list, b: list) -> list:
    """multiply(a: list, b: list) -> list: Element-wise multiplication of two arrays."""
    return (np.array(a) * np.array(b)).tolist()


def divide(a: list, b: list) -> list:
    """divide(a: list, b: list) -> list: Element-wise division of two arrays."""
    return (np.array(a) / np.array(b)).tolist()


def power(a: list, b: list) -> list:
    """power(a: list, b: list) -> list: First array elements raised to powers from second array, element-wise."""
    return np.power(a, b).tolist()


def abs_val(a: list) -> list:
    """abs_val(a: list) -> list: Element-wise absolute value of the input array."""
    return np.abs(a).tolist()


def exp(array: list) -> list:
    """exp(array: list) -> list: Calculate the exponential of all elements in the input array."""
    return np.exp(array).tolist()


def log(array: list) -> list:
    """log(array: list) -> list: Natural logarithm, element-wise."""
    return np.log(array).tolist()


def sqrt(array: list) -> list:
    """sqrt(array: list) -> list: Return the non-negative square-root of an array, element-wise."""
    return np.sqrt(array).tolist()


def sin(array: list) -> list:
    """sin(array: list) -> list: Trigonometric sine, element-wise."""
    return np.sin(array).tolist()


def cos(array: list) -> list:
    """cos(array: list) -> list: Cosine element-wise."""
    return np.cos(array).tolist()


def tan(array: list) -> list:
    """tan(array: list) -> list: Compute tangent element-wise."""
    return np.tan(array).tolist()


def mean(array: list) -> float:
    """mean(array: list) -> float: Compute the arithmetic mean along the specified axis."""
    return float(np.mean(array))


def median(array: list) -> float:
    """median(array: list) -> float: Compute the median along the specified axis."""
    return float(np.median(array))


def std(array: list) -> float:
    """std(array: list) -> float: Compute the standard deviation along the specified axis."""
    return float(np.std(array))


def var(array: list) -> float:
    """var(array: list) -> float: Compute the variance along the specified axis."""
    return float(np.var(array))


def min_val(array: list) -> float:
    """min_val(array: list) -> float: Return the minimum of an array or minimum along an axis."""
    return float(np.min(array))


def max_val(array: list) -> float:
    """max_val(array: list) -> float: Return the maximum of an array or maximum along an axis."""
    return float(np.max(array))


def argmin(array: list) -> int:
    """argmin(array: list) -> int: Returns the indices of the minimum values along an axis."""
    return int(np.argmin(array))


def argmax(array: list) -> int:
    """argmax(array: list) -> int: Returns the indices of the maximum values along an axis."""
    return int(np.argmax(array))


def percentile(array: list, q: float) -> float:
    """percentile(array: list, q: float) -> float: Compute the q-th percentile of the data."""
    return float(np.percentile(array, q))


def dot(a: list, b: list) -> float:
    """dot(a: list, b: list) -> float: Dot product of two arrays."""
    return float(np.dot(a, b))


def matmul(a: list, b: list) -> list:
    """matmul(a: list, b: list) -> list: Matrix product of two arrays."""
    return np.matmul(a, b).tolist()


def inv(matrix: list) -> list:
    """inv(matrix: list) -> list: Compute the (multiplicative) inverse of a matrix."""
    return np.linalg.inv(matrix).tolist()


def det(matrix: list) -> float:
    """det(matrix: list) -> float: Compute the determinant of an array."""
    return float(np.linalg.det(matrix))


def eig(matrix: list) -> dict:
    """eig(matrix: list) -> dict: Compute the eigenvalues and right eigenvectors of a square array."""
    vals, vecs = np.linalg.eig(matrix)
    return {"eigenvalues": vals.tolist(), "eigenvectors": vecs.tolist()}


def solve(A: list, b: list) -> list:
    """solve(A: list, b: list) -> list: Solve a linear matrix equation, or system of linear scalar equations."""
    return np.linalg.solve(A, b).tolist()


def svd(matrix: list) -> dict:
    """svd(matrix: list) -> dict: Singular Value Decomposition."""
    U, S, Vt = np.linalg.svd(matrix)
    return {"U": U.tolist(), "S": S.tolist(), "Vt": Vt.tolist()}
