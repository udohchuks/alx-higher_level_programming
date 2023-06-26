#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    results = []
    try:
        for i in range(list_length):
            num1 = my_list_1[i]
            num2 = my_list_2[i]
            result = 0
            try:
                result = num1 / num2
                results.append(result)
            except ZeroDivisionError:
                print("division by 0")
                results.append(0)
            except TypeError:
                print("wrong type")
                results.append(0)
    except IndexError:
        print("out of range")
        results.append(0)
    finally:
        pass

    return results
