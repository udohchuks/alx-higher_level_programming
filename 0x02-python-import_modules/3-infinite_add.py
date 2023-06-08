#!/usr/bin/python3
import sys
if __name__ == "__main__":
    arguments = sys.argv[1:]
    size = len(arguments)
    result = 0
    if size != 0:
        for arg in arguments:
            result += int(arg)
    print("{:d}".format(result))
