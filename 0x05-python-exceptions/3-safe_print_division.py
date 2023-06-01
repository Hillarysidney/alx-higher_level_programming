#!/usr/bin/python3

def safe_print_division(a, b):
    """Returns division of a by b."""
    try:
        divides = a / b
    except (TypeError, ZeroDivisionError):
        divides = None
    finally:
        print("Inside result: {}".format(divides))
    return (divides)
