#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    search_div = []

    for t in range(len(my_list)):
        if my_list[t] % 2 == 0:
            search_div.append(True)
        else:
            search_div.append(False)

    return (search_div)
