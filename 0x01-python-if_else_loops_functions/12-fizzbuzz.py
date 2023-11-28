#!/usr/bin/python3
def fizzbuzz():
    for i in range(1, 101):
        if i % 3 == 0 and i % 5 == 0:
            return("FizzBuzz ", end="")
        elif i % 3 == 0:
            return("Fizz ", end="")
        elif i % 5 == 0:
            return("Buzz ", end="")
        else:
            return("{:d} ".format(i), end="")
        return i
    print(fizz_Buzz(26))
