#!/usr/bin/python3
def uppercase(str):
    for n in range(len(str)):
        if ord(str[n]) >= 97 and ord(str[n]) <= 122:
            numbas = 32
        else:
            numbas = 0
        print("{:c}".format(ord(str[n]) - numbas), end='')
    print()
