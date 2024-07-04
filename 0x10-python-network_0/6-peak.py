#!/usr/bin/python3
"""a function that finds a peak in a list of unsorted integers"""


def find_peak(list_of_integers):
    sorted_list = sorted(list_of_integers, reverse=True)
    return sorted_list[0] if len(sorted_list) > 0 else None
