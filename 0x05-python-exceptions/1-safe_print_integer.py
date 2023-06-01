#!/usr/bin/python3

def safe_print_integer(value):
    """Print integer with "{:d}".format().
    Args:
        value (int): The integer to be print.
    Returns:
        If TypeError or ValueError occurs - False.
        Otherwise - True.
    """
    try:
        print("{:d}".format(value))
        return (True)
    except (TypeError, ValueError):
        return (False)
