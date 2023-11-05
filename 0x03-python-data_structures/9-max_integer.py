#!/usr/bin/python3
def max_integer(my_list=[]):
    if my_list == []:
        return None
    sorted_list = sorted(my_list, reverse=True)
    return sorted_list[0]
