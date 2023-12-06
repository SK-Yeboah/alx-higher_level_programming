#!/usr/bin/python3
import json

def to_json_string(my_obj):
    """
    Function to define JSON representation.

    Parameters:
    - my_obj: The object to be converted to a JSON-formatted string.

    Returns:
    - str: The JSON-formatted string.
    """
    return json.dumps(my_obj)
