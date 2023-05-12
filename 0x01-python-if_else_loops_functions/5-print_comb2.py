#!/usr/bin/python3
for my_numbers in range(100):
    if (my_numbers != 99):
        print("{}{}, ".format(int(my_numbers / 10), my_numbers % 10), end="")
    else:
        print("{}{}".format(int(my_numbers / 10), my_numbers % 10))
