#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
end_of_digit = number % 10 if number >= 0 else ((-number % 10) * -1)
message = f"Last digit of {number} is {end_of_digit}"

if end_of_digit == 0:
    print(f"{message} and is 0")
elif end_of_digit > 5 and end_of_digit % 10 != 0:
    print(f"{message} and is greater than 5")
else:
    print(f"{message} and is less than 6 and not 0")
