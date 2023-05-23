#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    real_dir = a_dictionary.copy()
    data_keys = list(real_dir.keys())

    for o in data_keys:
        real_dir[o] *= 2

    return (real_dir)
