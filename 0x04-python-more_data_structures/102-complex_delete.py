#!/usr/bin/python3
def complex_delete(a_dictionary, value):
    delete = []
    for key, val in a_dictionary.items():
        if val == value:
            delete.append(key)
    for k in delete:
        del a_dictionary[k]
    return a_dictionary
