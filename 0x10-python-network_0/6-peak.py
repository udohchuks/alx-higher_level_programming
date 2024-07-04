#!/usr/bin/python3
"""
Finds the peak
"""
def find_peak(list_of_integers):
    """
    Finds a peak element in a list of integers.
    Args:
    list_of_integers (list):
    A list of integers where the peak needs to be found.

    Returns:
    int or None:
    The peak element found in the list, or None if the list is empty.
    """
    if not list_of_integers:
        return None
    low, high = 0, len(list_of_integers) - 1
    while low < high:
        mid = (low + high) // 2
        if list_of_integers[mid] > list_of_integers[mid + 1]:
            high = mid
        else:
            low = mid + 1
    return list_of_integers[low]
