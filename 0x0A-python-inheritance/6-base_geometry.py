#!/usr/bin/python3
"""Defines a base geometry class BaseGeometry."""



class BaseGeometry:
    def area(self):
        """
        Calculate the area of the geometry.

        Raises:
        - Exception: Always raises an exception with the message 'area() is not implemented'.
        """
        raise Exception('area() is not implemented')
