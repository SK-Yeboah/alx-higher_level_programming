#!/usr/bin/python3

"""Module for Testing the Rectangle Class"""

import unittest
from models.Rectangle import Rectangle

class TestRectangle(unittest.TestCase):
    """Test Case for the Rectangle Class"""

    def test_attributes(self):
        """Test if attributes are set correctly during instantiating"""
        r = Rectangle(10, 20, 2, 3, 1)
        self.assertEqual(r.width, 10)
        self.assertEqual(r.height, 20)
        self.assertEqual(r.x, 2)
        self.assertEqual(r.y, 3)
        self.assertEqual(r.id, 1)

    def test_area(self):
        """Test if the area is correctly calculates"""
        r = Rectangle(5, 5)
        self.assertEqual(r.area(), 25)

    def test_str_method(self):
        """Test if the __str__ method returns the correct string representation."""
        r = Rectangle(4, 5, 1, 2, 10)
        self.assertEqual(str(r), "[Rectangle] (10) 1/2 - 4/5")

    def test_display(self):
        """Test if the display method prints correctly."""
        r = Rectangle(3, 2)
        expected_output = "###\n###\n"
        with unittest.mock.patch('sys.stdout', new_callable=io.StringIO) as mock_stdout:
            r.display()
            self.assertEqual(mock_stdout.getvalue(), expected_output)

    def test_update_method(self):
        """Test if the update method updates attributes correctly."""
        r = Rectangle(1, 1, 0, 0, 1)
        r.update(2, 3, 4, 5, 6)
        self.assertEqual(r.id, 2)
        self.assertEqual(r.width, 3)
        self.assertEqual(r.height, 4)
        self.assertEqual(r.x, 5)
        self.assertEqual(r.y, 6)


    def test_update_method_with_kwargs(self):
        """Test if the update method with kwargs updates attributes correctly."""
        r = Rectangle(1, 1, 0, 0, 1)
        r.update(id=2, width=3, height=4, x=5, y=6)
        self.assertEqual(r.id, 2)
        self.assertEqual(r.width, 3)
        self.assertEqual(r.height, 4)
        self.assertEqual(r.x, 5)
        self.assertEqual(r.y, 6)

    if __name__ == '__main__':
        unittest.main()