#!/usr/bin/python3
def remove_char_at(str, n):
    nancy = 0
    new_strin = ""
    for j in str:
        if nancy != n:
            new_strin += j
        nancy += 1
    return new_strin
