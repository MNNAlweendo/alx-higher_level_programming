#!/usr/bin/python3
def matrix_mul(m_a, m_b):
    """
    Multiply two matrices.

    Args:
        m_a (list of lists): The first matrix.
        m_b (list of lists): The second matrix.

    Returns:
        list of lists: The result of the matrix multiplication.

    Raises:
        TypeError: If m_a or m_b is not a list, not a list of lists, or not a rectangle.
        ValueError: If m_a or m_b is empty or cannot be multiplied.
    """
    # Validate m_a and m_b
    for matrix in [m_a, m_b]:
        if not isinstance(matrix, list):
            raise TypeError("m_a must be a list or m_b must be a list")
        if not matrix or not all(isinstance(row, list) for row in matrix):
            raise ValueError("m_a can't be empty or m_b can't be empty")
        if not all(isinstance(num, (int, float)) for row in matrix for num in row):
            raise TypeError("m_a should contain only integers or floats or m_b should contain only integers or floats")
        if len(set(len(row) for row in matrix)) != 1:
            raise TypeError("each row of m_a must be of the same size or each row of m_b must be of the same size")

    # Validate dimensions for matrix multiplication
    if len(m_a[0]) != len(m_b):
        raise ValueError("m_a and m_b can't be multiplied")

    # Perform matrix multiplication
    result = [[sum(a * b for a, b in zip(row_a, col_b)) for col_b in zip(*m_b)] for row_a in m_a]

    return result

