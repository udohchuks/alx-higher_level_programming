#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer


"""
Import max_integer
"""


class TestMaxInteger(unittest.TestCase):
    """
    Test max integer

    """
    def test_regular(self):
        """ regular test"""
        self.assertEqual(max_integer([1, 2, 3, 4]), 4)

    def test_reversed(self):
        """reversed test"""
        self.assertEqual(max_integer([4, 3, 2, 1]), 4)

    def test_unsorted_list(self):
        """unsorted list"""
        self.assertEqual(max_integer([1, 3, 4, 2]), 4)

    def test_empty_list(self):
        """empty list"""
        self.assertIsNone(max_integer([]))

    def test_negative_numbers(self):
        """negative test"""
        self.assertEqual(max_integer([-1, -2, -3, -4]), -1)

    def test_mixed_positive_negative(self):
        """mixed numbers test"""
        self.assertEqual(max_integer([-1, 2, -3, 4]), 4)
