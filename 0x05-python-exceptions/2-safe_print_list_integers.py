#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    ctr = 0
    for i in range(x):
        try:
            print("{:d}".format(my_list[i]), end="")
            ctr += 1
        except (TypeError, ValueError):
            continue
    print()
    return ctr
