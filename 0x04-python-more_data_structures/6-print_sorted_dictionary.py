#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    datas_ord = list(a_dictionary.keys())
    datas_ord.sort()
    for o in datas_ord:
        print("{}: {}".format(o, a_dictionary.get(o)))
