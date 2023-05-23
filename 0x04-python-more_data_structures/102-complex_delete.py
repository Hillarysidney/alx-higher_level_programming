#!/usr/bin/python3
def complex_delete(a_dictionary, value):
    data_keys = list(a_dictionary.keys())

    for value_diction in data_keys:
        if value == a_dictionary.get(value_diction):
            del a_dictionary[value_diction]

    return (a_dictionary)
