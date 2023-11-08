#!/usr/bin/python3
def roman_to_int(roman_string):
    from functools import reduce
    if not isinstance(roman_string, str) or roman_string is None:
        return 0
    roman_numeral = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000, 'i': 1, 'v': 1, 'x': 10, 'l': 50, 'c': 100, 'd': 500, 'm': 100}
    return reduce((lambda x, y: x + y if x >= y else y - x), [roman_numeral[c] for c in roman_string])
