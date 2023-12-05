#!/usr/bin/python3
"""Defines a function that adds attributes to objects."""


def add_attribute(obj, attribute_name, attribute_value):
    """
    Add a new attribute to an object if it's possible.

    Parameters:
    - obj: The object to which the attribute will be added.
    - attribute_name: The name of the new attribute.
    - attribute_value: The value of the new attribute.

    Raises:
    - TypeError: If the object can't have a new attribute.
    """
    if not hasattr(obj, '__dict__'):
        raise TypeError("can't add new attribute")

    setattr(obj, attribute_name, attribute_value)
