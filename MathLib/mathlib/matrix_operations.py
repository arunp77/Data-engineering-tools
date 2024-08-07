import numpy as np

def matrix_addition(matrix1, matrix2):
    """
    Add two matrices element-wise.

    Parameters:
    matrix1 (np.ndarray): The first matrix.
    matrix2 (np.ndarray): The second matrix.

    Returns:
    np.ndarray: The result of adding matrix1 and matrix2.

    Examples:
    >>> matrix_addition(np.array([[1, 2], [3, 4]]), np.array([[5, 6], [7, 8]]))
    array([[ 6,  8],
           [10, 12]])
    """
    return np.add(matrix1, matrix2)

def matrix_multiplication(matrix1, matrix2):
    """
    Multiply two matrices using dot product.

    Parameters:
    matrix1 (np.ndarray): The first matrix.
    matrix2 (np.ndarray): The second matrix.

    Returns:
    np.ndarray: The result of multiplying matrix1 and matrix2.

    Examples:
    >>> matrix_multiplication(np.array([[1, 2], [3, 4]]), np.array([[5, 6], [7, 8]]))
    array([[19, 22],
           [43, 50]])
    """
    return np.dot(matrix1, matrix2)

def matrix_determinant(matrix):
    """
    Compute the determinant of a matrix.

    Parameters:
    matrix (np.ndarray): The matrix.

    Returns:
    float: The determinant of the matrix.

    Examples:
    >>> matrix_determinant(np.array([[1, 2], [3, 4]]))
    -2.0
    """
    return np.linalg.det(matrix)

def matrix_inverse(matrix):
    """
    Compute the inverse of a matrix.

    Parameters:
    matrix (np.ndarray): The matrix to invert.

    Returns:
    np.ndarray: The inverse of the matrix.

    Raises:
    LinAlgError: If the matrix is singular and cannot be inverted.

    Examples:
    >>> matrix_inverse(np.array([[1, 2], [3, 4]]))
    array([[-2. ,  1. ],
           [ 1.5, -0.5]])
    """
    return np.linalg.inv(matrix)
