#!/usr/bin/python3

class Rectangle:
    """
    The Rectangle class represents a rectangle.

    Attributes:
        width (int): Width of the rectangle.
        height (int): Height of the rectangle.

    Methods:
        __init__(self, width=0, height=0): Initializes a new instance of the Rectangle class.
    """
    def __init__(self, width=0, height=0):
        """
        Initializes a new instance of the Rectangle class.

        Args:
            width (int, optional): Width of the rectangle (default is 0).
            height (int, optional): Height of the rectangle (default is 0).
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """Property to retrieve the width of the rectangle."""
        return self.__width

    @width.setter
    def width(self, value):
        """
        Property setter to set the width of the rectangle.

        Args:
            value (int): New width value.

        Raises:
            TypeError: If the new width value is not an integer.
            ValueError: If the new width value is less than 0.
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Property to retrieve the height of the rectangle."""
        return self.__height

    @height.setter
    def height(self, value):
        """
        Property setter to set the height of the rectangle.

        Args:
            value (int): New height value.

        Raises:
            TypeError: If the new height value is not an integer.
            ValueError: If the new height value is less than 0.
        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value
