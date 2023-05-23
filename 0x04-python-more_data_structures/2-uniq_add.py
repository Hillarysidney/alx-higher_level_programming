#!/usr/bin/python3
def uniq_add(my_list=[]):
    one_list = set(my_list)
    numbs = 0

    for o in one_list:
        numbs += o

    return (numbs)
