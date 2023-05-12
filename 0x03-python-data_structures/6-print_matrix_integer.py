#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for n in range(len(matrix)):
        for y in range(len(matrix[n])):
            if y != 0:
                print(" ", end='')
            print("{:d}".format(matrix[n][y]), end='')
        print()
