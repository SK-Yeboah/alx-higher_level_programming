#!/usr/bin/python3
def only_diff_elements(set_1, set_2):
    # Create a new set to store elements present in only one set
    diff_set = set()

    # Iterate through elements in set_1
    for element in set_1:
        # Check if the element is not present in set_2
        if element not in set_2:
            # Add the element to the diff_set
            diff_set.add(element)

    # Iterate through elements in set_2
    for element in set_2:
        # Check if the element is not present in set_1
        if element not in set_1:
            # Add the element to the diff_set
            diff_set.add(element)

    return diff_set
