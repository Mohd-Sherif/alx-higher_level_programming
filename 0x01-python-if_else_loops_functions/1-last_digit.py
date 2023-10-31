#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
last_number = number % 10
print(f"Last digit of {number :d} is", end = " ")
if number < 0:
    last_number -= 10
print(f"{last_number :d} and is", end = " ")
if last_number > 5:
    print("greater than 5")
elif last_number == 0:
    print("0")
else:
    print("less than 6 and not 0")
