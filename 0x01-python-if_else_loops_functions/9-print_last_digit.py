#!/usr/bin/python3
def print_last_digit(number):
    if number >= 0:
        end_of_numbers = number % 10
    else:
        end_of_numbers = number % -10
        end_of_numbers *= -1

    print("{:d}".format(end_of_numbers), end='')
    return (end_of_numbers)
