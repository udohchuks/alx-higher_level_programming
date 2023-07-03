#!/usr/bin/python3


"""
Divide Matrix Item by a number

Return: A new Matrix

"""


def matrix_divided(matrix, div):

    """
    Divide Matrix Item by a number

    Return: A new Matrix
    """

    if not isinstance(matrix, list) or \
            not all(isinstance(row, list) for row in matrix):
        raise \
                TypeError("matrix must\
                be a matrix (list of lists) of integers/float")
    if len(matrix) > 1 and \
            any(len(row) != len(matrix[0]) for row in matrix[1:]):
        raise TypeError("Each row of the matrix must have the same size")
    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")
    new_mat = [[round(element / div, 2) for element in row] for row in matrix]

    return new_mat
