#!/usr/bin/python3
import hidden_4
if __name__ == "__main__":
    names = dir(hidden_4)
    size = len(names)
    for i in range(size):
        if names[i][0:2] == "__":
            continue
        print(names[i])
