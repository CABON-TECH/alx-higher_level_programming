#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)

if number > 0:
    div = 10
else:
    div = -10

if (number % div) > 5:
    print("Last digit of {:d} is {:d} and is greater than 5"
          .format(number, number % div))
elif (number % div) == 0:
    print("Last digit of {:d} is {:d} and is 0".format(number, number % div))
else:
    print("Last digit of {:d} is {:d} and is less than 6 and not 0"
          .format(number, number % div))
