#!/usr/bin/python3
def number_keys(a_dictionary):
    numbs = 0
    data_keys = list(a_dictionary.keys())

    for i in data_keys:
        numbs += 1

    return (numbs)
