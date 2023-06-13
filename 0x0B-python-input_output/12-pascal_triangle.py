#!/usr/bin/python3
"""Pascal's Triangle function."""


def pascal_triangle(n):
    """To Representing Pascal's Triangle of size n.
    Returns list of lists of integers representing the triangle.
    """
    if n <= 0:
        return []

    triangular = [[1]]
    while len(triangular) != n:
        triangs = triangular[-1]
        tmp = [1]
        for i in range(len(triangs) - 1):
            tmp.append(triangs[i] + triangs[i + 1])
        tmp.append(1)
        triangular.append(tmp)
    return triangular
