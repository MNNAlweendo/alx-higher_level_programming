def matrix_divided(matrix, div):
    """
    Divide all elements of a matrix by a divisor.

    Args:
        matrix (list of lists): The matrix to be divided.
        div (int or float): The divisor.

    Returns:
        list of lists: The matrix with each element divided by div,
                       rounded to 2 decimal places.
    Raises:
        TypeError: If matrix is not a list of lists of integers or floats,
                   or if div is not a number.
        TypeError: If each row of the matrix does not have the same size.
        ZeroDivisionError: If div is equal to 0.
    """
    # Check if matrix is a list of lists of integers or floats
    if not isinstance(matrix, list) or not all(isinstance(row, list) for row in matrix):
        raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
    if not all(isinstance(num, (int, float)) for row in matrix for num in row):
        raise TypeError("matrix must contain only integers or floats")
    if not all(len(row) == len(matrix[0]) for row in matrix):
        raise TypeError("Each row of the matrix must have the same size")

    # Check if div is a number and not equal to 0
    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")

    # Divide each element of the matrix by div, rounded to 2 decimal places
    return [[round(num / div, 2) for num in row] for row in matrix]

