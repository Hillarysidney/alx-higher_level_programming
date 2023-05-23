#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    current_matrix = matrix.copy()

    for o in range(len(matrix)):
        current_matrix[o] = list(map(lambda x: x**2, matrix[o]))

    return (current_matrix)
