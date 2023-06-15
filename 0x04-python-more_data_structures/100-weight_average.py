#!/usr/bin/python3
def weight_average(my_list=[]):
    if not my_list:
        return 0
    sum_prdt = 0
    weight_sum = 0

    for score, weight in my_list:
        sum_prdt += score * weight
        weight_sum += weight

    return (sum_prdt / weight_sum)
