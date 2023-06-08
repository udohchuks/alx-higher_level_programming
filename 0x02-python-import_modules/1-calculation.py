#!/usr/bin/python3
import calculator_1 as cal

if __name__ == "__main__":
    a = 10
    b = 5
    print("{} + {} = {}".format(a, b, cal.add(10, 5)))

    print("{} - {} = {}".format(a, b, cal.sub(10, 5)))

    print("{} * {} = {}".format(a, b, cal.mul(10, 5)))

    print("{} / {} = {}".format(a, b, cal.div(10, 5)))

