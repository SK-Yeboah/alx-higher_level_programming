#!/usr/bin/python3
"""Module defining the Rectangle class."""


from models.base import Base

class Rectangle(Base):

    """Rectangle class, inherits from Base."""
    def __init__(self,width, height, x = 0, y = 0, id=None):
        """Initialize a new instance of Rectangle.

        Args:
            width (int): Width of the rectangle.
            height (int): Height of the rectangle.
            x (int): X-coordinate of the rectangle.
            y (int): Y-coordinate of the rectangle.
            id (int): Identifier for the rectangle.

        Returns:
            None
        """
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y
    

    @property
    def width(self):
        """Getter for width"""
        return self.__width
    
    @width.setter
    def width(self, value):
        """Setter for width.

        Args:
            value (int): The new value for width.

        Returns:
            None
        """
        self.__validate_non_negative_int('width', value)
        self.__width = value

    @property
    def height(self):
        """Getter for height"""
        return self.__height
    
    @height.setter
    def height(self, value):
        """Setter for height.
        Args:
            value(int): The new value for height
        Reurn:
            None
        """
        self.__validate_non_negative_int('width', value)
        self.__height = value
    
    @property
    def x(self):
        """Getter for x."""
        return self.__x

    @x.setter
    def x(self, value):
        """Setter for x.

        Args:
            value (int): The new value for x.

        Returns:
            None
        """
        self.__validate_non_negative_int('x', value)
        self.__x = value
    
    @property
    def y(self):
        """Getter for y."""
        return self.__y

    @y.setter
    def y(self, value):
        """Setter for y.

        Args:
            value (int): The new value for y.

        Returns:
            None
        """
        self.__validate_non_negative_int('y', value)
        self.__y = value


    def area(self):
        """Calculate and return the area of the rectangle.

        Returns:
            int: The area of the rectangle.
        """
        return self.width * self.height
    
    def to_dictionary(self):
        """Return dictionary representation of the Rectangle.

        Returns:
            dict: Dictionary representation of the Rectangle.
        """
        return {
            'id': self.id,
            'width': self.width,
            'height': self.height,
            'x': self.x,
            'y': self.y
        }
    
    
    def display(self):
        """Display the Rectangle instance using the character #.

        Returns:
            None
        """
        for _ in range(self.y):
            print()
        for _ in range (self.height):
            print(" " * self.x + "#" * self.width)

    def __str__(self):
        """Return the string representation of the Rectangle.

        Returns:
            str: String representation of the Rectangle.
        """
        return f"[Rectangle] ({self.id}) {self.x}/{self.y} - {self.width}/{self.height}"
    
    def  update (self, *args, **kwargs):
        """Update attributes with positional arguments.

        Args:
            *args: Positional arguments to update attributes.
            **kwargs: Keyword arguments to update attributes.


        Returns:
            None
        """
        if args:
            attributes = ['id', 'width', 'height', 'x', 'y']
            for i, args in  enumerate(args):
                setattr(self, attributes[i], args)
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
        if not  isinstance(value, int):
            raise TypeError(f"{attribute} must be integer")
        if value < 0 :
            raise ValueError(f"{attribute} must be >= 0")



