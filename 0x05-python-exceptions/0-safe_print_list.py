#!/usr/bin/python3

def safe_print_list(my_list=[], x=0):
    """Print x elememts of a list.
    Args:
        my_list (list): The list to print elements from.
        x (int): The number of elements of my_list to print.
    Returns:
        The number of elements printed.
    """
    countt = 0
    for t in range(x):
        try:
            print("{}".format(my_list[t]), end="")
            countt += 1
        except IndexError:
            break
    print("")
    return (countt)
