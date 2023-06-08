#!/usr/bin/python3
import sys
if __name__ == "__main__":
    arguments = sys.argv
    size = len(arguments) - 1
    string = "arguments:" if size != 1 else "argument:"
    string = "arguments." if size == 0 else string
    print("{} ".format(size) + string)
    if arguments and size != 0:
        for i, arg in enumerate(arguments):
            if i == 0:
                continue
            print("{}: {}".format(i, arguments[i]))
