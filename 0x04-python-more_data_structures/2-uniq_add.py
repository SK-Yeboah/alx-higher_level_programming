#!/usr/bin/python3
def uniq_add(my_list=[]):
    unique_integers = []

    for i in my_list:
        if i not in unique_integers:
            unique_integers.append(i)
    result = sum(unique_integers)

    return result
