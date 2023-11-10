def best_score(a_dictionary):
    # Check if the dictionary is empty
    if not a_dictionary:
        return None

    # Find the key with the maximum value using max()
    best_key = max(a_dictionary, key=a_dictionary.get)

    return best_key
