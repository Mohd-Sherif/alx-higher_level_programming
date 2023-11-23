#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    ctr = 0
    while ctr < x:
        try:
            print("{}".format(my_list[ctr]), end="")
            ctr += 1
        except IndexError:
            break
    print()
    return ctr
