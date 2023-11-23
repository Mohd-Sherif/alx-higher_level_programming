#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    list3 = []
    for i in range(list_length):
        try:
            dev = my_list_1[i] / my_list_2[i]
        except TypeError:
            print("wrong type")
            dev = 0
        except ZeroDivisionError:
            print("division by 0")
            dev = 0
        except IndexError:
            print("out of range")
            dev = 0
        finally:
            list3.append(dev)
    return list3
