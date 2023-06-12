#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for row in matrix:
        for index, num in enumerate(row):
            print("{:d}".format(num), end='')
            if index < len(row) - 1:
                print(' ', end='')
        print()
