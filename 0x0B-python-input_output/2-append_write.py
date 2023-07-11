#!/usr/bin/python3
"""appends to file """


def append_write(filename="", text=""):
    """appends to file"""
    with open(filename, "a", encoding="utf-8") as file:
        file.seek(0, 2)
        num_char = file.write(text)
        return num_char
