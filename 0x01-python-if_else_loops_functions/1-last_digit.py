#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
lastNo = number % 10
if number > 5:
    print("Last digit of {:d} is {:d} and is greater than 5".format(number,
lastNo))
elif number == 0:
    print("Last digit of {:d} is {:d} and is 0".format(number, lastNo))
else:
    print("Last digit of {:d} is {:d} and is less than 6 and not 0".format(
number, lastNo))