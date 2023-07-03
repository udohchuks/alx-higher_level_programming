#!/usr/bin/python3


"""
It takes 2 integers a and b
It returns the sum of the 2 integers with a type of int]
If convert a and b to int if they are float

"""


def add_integer(a, b=98):

    '''
    Add two numbers a and b
    test if a is an int or a float
    test if b is an int or a float
    convert a and b to int if they are float
    '''
    if not isinstance(a, int) and not isinstance(a, float):
        raise TypeError("a  must be an integer")

    if not isinstance(b, int) and not isinstance(b, float):
        raise TypeError("b must be an integer")

    if isinstance(a, float):
        a = int(a)
    if isinstance(b, float):
        b = int(b)

    return a + b
