#!/usr/bin/python3
def print_last_digit(number):
    last_number = number % 10
    if number < 0:
        last_number -= 10
    return last_number
