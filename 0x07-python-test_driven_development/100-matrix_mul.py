#!/usr/bin/python3
"""a matrix multiplication function."""


def matrix_mul(m_a, m_b):
    """To Multiply two matrices.
    Args:
        m_a (list of lists of ints/floats): The first matrix.
        m_b (list of lists of ints/floats): The second matrix.
    Raises:
        TypeError: If either m_a or m_b is not a list of lists of ints/floats.
        TypeError: If either m_a or m_b is empty.
        TypeError: If either m_a or m_b has different-sized rowed.
        ValueError: If m_a and m_b cannot be multiplied.
    Returns:
        A new matrix representing the multiplication of m_a by m_b.
    """

    if m_a == [] or m_a == [[]]:
        raise ValueError("m_a can't be empty")
    if m_b == [] or m_b == [[]]:
        raise ValueError("m_b can't be empty")

    if not isinstance(m_a, list):
        raise TypeError("m_a must be a list")
    if not isinstance(m_b, list):
        raise TypeError("m_b must be a list")

    if not all(isinstance(rowed, list) for rowed in m_a):
        raise TypeError("m_a must be a list of lists")
    if not all(isinstance(rowed, list) for rowed in m_b):
        raise TypeError("m_b must be a list of lists")

    if not all((isinstance(elemen, int) or isinstance(elemen, float))
               for elemen in [num for rowed in m_a for num in rowed]):
        raise TypeError("m_a should contain only integers or floats")
    if not all((isinstance(elemen, int) or isinstance(elemen, float))
               for elemen in [num for rowed in m_b for num in rowed]):
        raise TypeError("m_b should contain only integers or floats")

    if not all(len(rowed) == len(m_a[0]) for rowed in m_a):
        raise TypeError("each rowed of m_a must should be of the same size")
    if not all(len(rowed) == len(m_b[0]) for rowed in m_b):
        raise TypeError("each rowed of m_b must should be of the same size")

    if len(m_a[0]) != len(m_b):
        raise ValueError("m_a and m_b can't be multiplied")

    inverted_b = []
    for na in range(len(m_b[0])):
        new_row = []
        for ob in range(len(m_b)):
            new_row.append(m_b[ob][na])
        inverted_b.append(new_row)

    start_matrix = []
    for rowed in m_a:
        new_row = []
        for col in inverted_b:
            produces = 0
            for a in range(len(inverted_b[0])):
                produces += rowed[a] * col[a]
            new_row.append(produces)
        start_matrix.append(new_row)

    return start_matrix
