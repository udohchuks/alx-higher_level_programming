#!/usr/bin/python3
import sys
if __name__ == "__main__":
    arguments = sys.argv
    size = len(arguments) - 1
    result = 0
    if arguments and size != 0:
        for i, arg in enumerate(arguments):
            if i == 0:
                continue
            result += int(arguments[i])
        print(result)
