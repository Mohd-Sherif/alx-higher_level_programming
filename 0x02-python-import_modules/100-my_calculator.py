#!/usr/bin/python3

from calculator_1 import add, sub, mul, div
import sys

if __name__ == "__main__":
    # get arguments
    argv = sys.argv[1:]

    # count arguments
    argc = len(argv)

    # check If the number of arguments is not 3
    if argc != 3:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        sys.exit(1)
    else:

        # assign a, b, operator
        a = int(argv[0])
        b = int(argv[2])
        op = argv[1]

        # check for the operator
        if op == "+":
            result = add(a, b)
        elif op == "-":
            result = sub(a, b)
        elif op == "*":
            result = mul(a, b)
        elif op == "/":
            result = div(a, b)
        else:
            print("Unknown operator. Available operators: +, -, * and /")
            sys.exit(1)

        # print full equation
        print("{:d} {:s} {:d} = {:d}".format(a, op, b, result))
