#!/usr/bin/python3
"""a function that finds a peak in a list of unsorted integers"""


def find_peak(list_of_integers):
    if list_of_integers == []:
        return None
    l = len(list_of_integers)
    mid = int(l / 2)
    if l == 1:
        return list_of_integers[0]
    if l == 2:
        return max(list_of_integers[0], list_of_integers[1])
    if list_of_integers[mid - 1] <= list_of_integers[mid] and\
          list_of_integers[mid + 1] <= list_of_integers[mid]:
        return list_of_integers[mid]
    if mid > 0 and list_of_integers[mid] < list_of_integers[mid + 1]:
        return find_peak(list_of_integers[mid:])
    if mid > 0 and list_of_integers[mid] < list_of_integers[mid - 1]:
        return find_peak(list_of_integers[:mid])
