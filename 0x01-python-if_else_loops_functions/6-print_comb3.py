#!/usr/bin/python3
for numbas in range(100):
    if int(numbas / 10) != numbas % 10 and int(numbas / 10) < numbas % 10:
        print("{}{}".format(int(numbas / 10), numbas % 10), end="")
        if (numbas != 89):
            print(", ", end="")
print("")
