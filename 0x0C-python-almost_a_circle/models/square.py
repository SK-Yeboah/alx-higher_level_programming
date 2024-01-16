#!/bin/usr/python3

"""Module defining the square class"""

from models.Rectangle import Rectangle



class Square(Rectangle):
    """Square class, inherit from the rectangle class"""
    
    def __init__(self, size,  x=0, y=0, id=None):
        """Initialize a new instance of  Square
            Args:
                size(int): size of the square
                x(int):  X-coordinate of the  square
                y(int): Y-coordinate of the square
                id(int): Identifier for the square
        """
        super().__init__(size, x, y, id)

    def __str__(self):
        """Return the string representation of the Square.

        Returns:
            str: String representation of the Square.
        """
        return f"[Square] ({self.id}) {self.x}/{self.y} - {self.width}"
    
    @property
    def size(self):
        """Getter for size."""
        return self.width
    

    @size.setter
    def size(self, value):
        """Setter for size.

        Args:
            value (int): The new value for size.

        Returns:
            None
        """
        self.__validate_non_negative_int('width', value)
        self.width = value
        self.height = value
    
    def to_dictionary(self):
        """Return dictionary representation of the Square.

        Returns:
            dict: Dictionary representation of the Square.
        """
        return {
            'id': self.id,
            'size': self.size,
            'x': self.x,
            'y': self.y
        }
    def update(self, *args, **kwargs):
        """Update attributes with positional and keyword arguments.

        Args:
            *args: Positional arguments to update attributes.
            **kwargs: Keyword arguments to update attributes.

        Returns:
            None
        """
        if args:
            attributes = ['id', 'size', 'x', 'y']
            for i, arg in enumerate(args):
                setattr(self, attributes[i], arg)
        elif kwargs:
            for key, value in kwargs.items():
                setattr(self, key, value)
    
    def __validate_non_negative_int(self, attribute, value):
        """Validate that the given value is a non-negative integer.

        Args:
            attribute (str): The attribute name.
            value (int): The value to be validated.

        Returns:
            None

        Raises:
            TypeError: If the value is not an integer.
            ValueError: If the value is negative.
        """
        if not isinstance(value, int):
            raise TypeError(f"{attribute} must be an integer")
        if value < 0:
            raise ValueError(f"{attribute} must be >= 0")