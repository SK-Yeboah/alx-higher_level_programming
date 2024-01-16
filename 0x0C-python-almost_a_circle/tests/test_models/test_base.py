#!/usr/bin/python3

"""Unit tests for  Base Class"""

import unittest
from models.base import Base


class TestBase(unittest.TestCase):
    """Test Case For The Base Class"""

    def test_init_with_id(self):
        """Test if Base is initialized with a given id."""
        b = Base(5)
        self.assertEqual(b.id, 5)

    def test_init_without_id(self):
        """Test if Base is initialized with an auto-incremented id."""
        b1 = Base()
        b2 = Base()
        self.assertEqual(b1.id, 1)
        self.assertEqual(b2.id, 2)
        
    def test_init_mixed_ids(self):
        """Test if Base handles both given and auto-incremented ids."""
        b1 = Base(10)
        b2 = Base()
        self.assertEqual(b1.id, 10)
        self.assertEqual(b2.id, 3)  # Auto-incremented from the previous tests

