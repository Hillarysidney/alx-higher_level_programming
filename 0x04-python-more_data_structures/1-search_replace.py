#!/usr/bin/python3
def search_replace(my_list, search, replace):
    real_lists = list(map(lambda x: replace if x == search else x, my_list))
    return (real_lists)
