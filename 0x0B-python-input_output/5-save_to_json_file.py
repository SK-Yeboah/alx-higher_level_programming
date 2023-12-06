#!/usr/bin/python3
import json
"""Defile save json file"""
def save_to_json_file(my_obj, filename):
    """Write an object to a text file using json representation"""
    with open(filename, 'w') as file:
        json.dump(my_obj, file)
