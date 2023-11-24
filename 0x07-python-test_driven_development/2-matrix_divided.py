#!/usr/bin/python3
"""A module for matrix division."""


def matrix_divided(matrix, div):
    """Divides all elements of a matrix by a given divisor.

    :param matrix: A matrix represented as a
                    list of lists of integers or floats.
    :param div: The divisor, a number (integer or float),
                by which to divide all elements of the matrix.

    :raises: - TypeError: If the matrix is not a valid
                        matrix (list of lists of integers/floats),
                    or if each row of the matrix does not have the same size,
                    or if the divisor is not a number (integer or float).
             - ZeroDivisionError: If the divisor is equal to 0.

    :return: A new matrix with all elements divided by the divisor,
            rounded to 2 decimal places.
    """
    if (
            not isinstance(matrix, list) or
            not all(isinstance(row, list) for row in matrix) or
            not all(isinstance(n, (int, float)) for row in matrix for n in row)
        ):
        raise TypeError("matrix must be a matrix (list of lists) of integers/floats")

    row_sizes = set(len(row) for row in matrix)
    if len(row_sizes) > 1:
        raise TypeError("Each row of the matrix must have the same size")

    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")

    div_matrix = list(
            map(
                (lambda row: list(map((lambda n: round(n / div, 2)), row))), matrix
                )
            )
    return div_matrix
