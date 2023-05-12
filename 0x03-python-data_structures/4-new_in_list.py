#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    measure = len(my_list)

    latest_list = my_list[:]

    if 0 <= idx < measure:
        latest_list[idx] = element

    return (latest_list)
