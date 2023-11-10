#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    # Use map and list comprehension to create the squared matrix
    result_matrix = [list(map(lambda x: x**2, row)) for row in matrix]

    return result_matrix

