#!/usr/bin/python3


"""
Replaces {",", "?", ":"} with \n\n

"""


def text_indentation(text):

    """
    Replaces {",", "?", ":"} with \n\n

    """

    if not isinstance(text, str):
        raise TypeError("text must be a string")
    puctuation = [".", "?", ":"]
    ftext = ""

    for c in text:
        ftext += c
        if c in puctuation:
            ftext += "\n\n"

    print(ftext.strip(), end="")
