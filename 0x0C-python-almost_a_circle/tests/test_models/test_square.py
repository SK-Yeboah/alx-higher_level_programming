#!/usr/bin/python3
"""Module for testing Square class."""

import unittest
from models.square import Square

class TestSquare(unittest.TestCase):
    """Test cases for square class"""

    def test_attributes(self):
        """Test if attribute  are set correctly  during instanttiation"""
        square = Square(5, 2, 3, 1)
        self.assertEqual(square.size, 5)
        self.assertEqual(square.width, 5)
        self.assertEqual(square.height, 5)
        self.assertEqual(square.x, 2)
        self.assertEqual(square.y, 3)
        self.assertEqual(square.id, 1)


    def test_area(self):
        """Test if the area is calculated correctly."""
        square = Square(5, 2, 3, 1)
        self.assertEqual(square.area(), 25)

    def test_str_method(self):
        """Test if the __str__ method returns the correct string representation."""
        square = Square(5, 2, 3, 1)
        self.assertEqual(str(square), "[Square] (1) 2/3 - 5")
    
    def test_update_method(self):
        """Test if the update method updates attributes correctly."""
        square = Square(5, 2, 3, 1)
        square.update(2, 8, 4, 6)
        self.assertEqual(square.id, 2)
        self.assertEqual(square.size, 8)
        self.assertEqual(square.x, 4)
        self.assertEqual(square.y, 6)

    def test_update_method_with_kwargs(self):
        """Test if the update method with kwargs updates attributes correctly."""
        square = Square(5, 2, 3, 1)
        square.update(id=2, size=8, x=4, y=6)
        self.assertEqual(square.id, 2)
        self.assertEqual(square.size, 8)
        self.assertEqual(square.x, 4)
        self.assertEqual(square.y, 6)

    def test_to_dictionary_method(self):
        """Test if the to_dictionary method returns the correct dictionary."""
        square = Square(5, 2, 3, 1)
        expected_dict = {'id': 1, 'size': 5, 'x': 2, 'y': 3}
        self.assertEqual(square.to_dictionary(), expected_dict)
    
    if __name__ == '__main__':
        unittest.main()