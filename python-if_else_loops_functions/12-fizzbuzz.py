#!/usr/bin/python3
def fizzbuzz():
    for 1 in range(1, 101):
        if 1 % 3 == 0 and i % 5 == 0:
            print("FizzBuzz", end=" ")
        elif i % 5 == 0:
            print("Buzz", end=" ")
        elif i % 3 == 0:
            print("Fizz", end=" ")
        else:
            print("{}".format(i), end=" ")
