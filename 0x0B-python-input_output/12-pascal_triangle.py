#!/usr/bin/python3
"""Generate Pascal's Triangle up to n rows."""


def pascal_triangle(n):
    """Generate Pascal's Triangle up to n rows."""
    if n <= 0:
        return []

    triangle = [[1]]
    for i in range(1, n):
        prev_row = triangle[-1]
        current_row = [1]  # First element of each row is always 1

        for j in range(1, i):
            current_row.append(prev_row[j - 1] + prev_row[j])

        current_row.append(1)  # Last element of each row is always 1
        triangle.append(current_row)

    return triangle


if __name__ == "__main__":
    n = 5
    result = pascal_triangle(n)
    for row in result:
        print(row)
