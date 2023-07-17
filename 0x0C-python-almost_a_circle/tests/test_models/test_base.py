#!/usr/bin/bash
"""
Unit test cases for the Base class.

"""
import unittest
from models.base import Base
import sys
sys.path.append("../models")


class TestBase(unittest.TestCase):
    """Test Base"""

    def test_unique_id(self):
        """Assert unique Id"""

        b1 = Base()
        b2 = Base()
        b3 = Base()

        self.assertNotEqual(b1.id, b2.id)
        self.assertNotEqual(b2.id, b3.id)
        self.assertNotEqual(b3.id, b1.id)

    def test_custom_id(self):
        custom = 23
        b4 = Base(23)
        self.assertEqual(b4.id, custom)

    def test_auto_id(self):
        b5 = Base()
        b6 = Base()

        self.assertEqual(b5.id, 1)
        self.assertEqual(b6.id, 2)
