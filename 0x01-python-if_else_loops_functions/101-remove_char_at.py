#!/usr/bin/python3
def remove_char_at(string, n):
    copy = ""
    for i, c in enumerate(string):
        if i == n:
            continue
        copy += c
    return copy
