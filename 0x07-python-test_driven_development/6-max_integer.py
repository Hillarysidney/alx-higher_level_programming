#!/usr/bin/python3
"""A Module to find the max integer in a list
"""


def max_integer(list=[]):
    """A Function to the find and return the max integer in a list of integers
        If the list is empty, the function returns None
    """
    if len(list) == 0:
        return None
    solve = list[0]
    t = 1
    while t < len(list):
        if list[t] > solve:
            solve = list[t]
        t += 1
    return solve
