#!/usr/bin/python3
"""
Divides all elements of a matrix
"""


def matrix_divided(matrix, div):
    """
    divides all elements of a matrix
    Params:
        matrix – list of lists of integers or floats
        div – divisor
    Returns:
        a new matrix containing the quotients
    Raises:
        TypeError – if matrix elements are neither int nor float,
         if matrix rows are not the same size
        ZeroDivisionError – if dividing by zero
    """
    new = []

    if div is None or type(div) is not int and type(div) is not float:
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")
    if type(matrix) is not list:
        raise TypeError("matrix must be a matrix (list of lists) " +
                        "of integers/floats")

    for i in range(len(matrix)):
        if type(matrix[i]) is not list:
            raise TypeError("matrix must be a matrix (list of lists) " +
                            "of integers/floats")
        row = []
        for c in range(len(matrix[i])):
            if type(matrix[i][c]) is not int \
                    and type(matrix[i][c]) is not float:
                raise TypeError("matrix must be a matrix (list of lists) " +
                                "of integers/floats")
            if len(matrix[0]) != len(matrix[i]):
                raise TypeError("Each row of the matrix"
                                " must have the same size")
            row.append(round((matrix[i][c]) / div, 2))
        new.append(row)
    return new
