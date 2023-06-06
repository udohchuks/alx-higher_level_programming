#!/usr/bin/python3
def uppercase(str):
    str1 = ""
    for c in str:
        if ord(c) in range(97, 123):
            c = chr(ord(c) - 32)
        str1 += c
    print("{}".format(str1))
