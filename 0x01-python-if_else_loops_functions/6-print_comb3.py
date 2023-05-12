#!/usr/bin/python3
for my_numbers in range(100):
    if int(my_numbers / 10) != my_numbers % 10 and int(my_numbers / 10) < my_numbers % 10:
        print("{}{}".format(int(my_numbers / 10), my_numbers % 10), end="")
        if (my_numbers != 89):
            print(", ", end="")
print("")
