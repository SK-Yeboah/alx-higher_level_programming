#!/usr/bin/python3
class Rectangle:
    """
    The Rectangle class represents a rectangle.
    """
    def __init__(self, width=0, height=0):
        """
        Initializes a new instance of the Rectangle class.
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """Property to retrieve the width of the rectangle."""
        return self._width

    @width.setter
    def width(self, value):
        """
        Property setter to set the width of the rectangle.
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self._width = value

    @property
    def height(self):
        """Property to retrieve the height of the rectangle."""
        return self._height

    @height.setter
    def height(self, value):
        """
        Property setter to set the height of the rectangle.
        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self._height = value

    def area(self):
        """Calculates and returns the area of the rectangle."""
        return self._width * self._height

    def perimeter(self):
        """Calculates and returns the perimeter of the rectangle."""
        return 2 * (self._width + self._height) if self._width > 0 and self._height > 0 else 0

    def __str__(self):
        """
        Returns a string representation of the rectangle for print().
        """
        if self._width == 0 or self._height == 0:
            return ""
        
        result = ""
        for _ in range(self._height):
            result += "#" * self._width + "\n"
        return result.rstrip()
