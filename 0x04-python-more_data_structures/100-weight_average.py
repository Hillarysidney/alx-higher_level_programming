#!/usr/bin/python3
def weight_average(my_list=[]):
    if not my_list:
        return 0

    numbars = 0
    densi = 0

    for tup in my_list:
        numbars += tup[0] * tup[1]
        densi += tup[1]

    return (numbars / densi)
