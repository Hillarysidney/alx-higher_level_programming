#!/usr/bin/python3
def fizzbuzz():
    for my_numbers in range(1, 101):
        if my_numbers % 3 == 0 and my_numbers % 5 == 0:
            print("FizzBuzz ", end="")
        elif my_numbers % 5 == 0:
            print("Buzz ", end="")
        elif my_numbers % 3 == 0:
            print("Fizz ", end="")
        else:
            print(f"{my_numbers} ", end="")
