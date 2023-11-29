#!/usr/bin/python3
"""Unittests for max_integer([..])."""


import unittest
max_integer = __import__('6-max_integer').max_integer

class TestMaxInteger(unittest.TestCase):
    def test_max_integer_basic(self):
        self.assertEqual(max_integer([1, 5, 3, 8, 2]), 8)

    def test_max_integer_negative(self):
        self.assertEqual(max_integer([-10, -5, -8, -2]), -2)

    def test_max_integer_empty_list(self):
        self.assertIsNone(max_integer([]))

    def test_max_integer_mixed_types(self):
        with self.assertRaises(TypeError):
            max_integer(["one", "two", "three"])

    def test_max_integer_duplicate_max(self):
        self.assertEqual(max_integer([2, 5, 2, 8, 2]), 8)

    def test_max_integer_single_element(self):
        self.assertEqual(max_integer([42]), 42)

    def test_max_integer_all_negative(self):
        self.assertEqual(max_integer([-10, -5, -8, -2]), -2)

if __name__ == '__main__':
    unittest.main()
