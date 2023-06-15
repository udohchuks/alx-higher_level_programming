#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    new_matrix = []
    for row in matrix:
        sub_mtrx = map(lambda x: x ** 2, row)
        new_matrix.append(list(sub_mtrx))
    return new_matrix
