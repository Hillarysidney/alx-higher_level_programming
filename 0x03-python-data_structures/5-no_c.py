#!/usr/bin/python3
def no_c(my_string):
    measure = len(my_string)

    n = 0

    fresh_string = my_string[:]

    for y in range(measure):
        if (my_string[y] == 'c' or my_string[y] == 'C'):
            fresh_string = fresh_string[:(y - n)] + my_string[(y + 1):]
            n += 1

    return (fresh_string)
