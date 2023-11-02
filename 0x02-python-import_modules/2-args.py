#!/usr/bin/python3
import sys
if __name__ == "__main__":
    argv = sys.argv[1:]
    argc = len(argv)
    if argc == 0:
        print("{:d} arguments.".format(argc))
    elif argc == 1:
        print("{:d} argument.".format(argc))
    else:
        print("{:d} arguments:".format(argc))
        for i in range(argc):
            print("{:d}: {:s}".format(i + 1, argv[i]))
