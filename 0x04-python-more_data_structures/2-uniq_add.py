#!/usr/bin/python3
def uniq_add(my_list=[]):
    unq_list = set()
    for x in my_list:
        unq_list.add(x)
    result = sum(unq_list)
    return result
