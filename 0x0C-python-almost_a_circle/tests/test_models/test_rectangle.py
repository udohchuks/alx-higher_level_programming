#!/usr/bin/python3
"""
Test for Rectangle class
"""
import sys
sys.path.append("../models")
import unittest
from models.rectangle import Rectangle


class TestRectangle(unittest.TestCase):
    """tests"""
    def test_valid_inputs(self):
        """
        valid input"""
        r1 = Rectangle(10, 20, 1, 2, 100)
        self.assertEqual(r1.width, 10)
        self.assertEqual(r1.height, 20)
        self.assertEqual(r1.x, 1)
        self.assertEqual(r1.y, 2)
        self.assertEqual(r1.id, 100)

        r2 = Rectangle(5, 5)
        self.assertEqual(r2.width, 5)
        self.assertEqual(r2.height, 5)
        self.assertEqual(r2.x, 0)
        self.assertEqual(r2.y, 0)
        self.assertIsNotNone(r2.id)

    def test_invalid_width(self):
        """Test invalid width"""
        with self.assertRaises(ValueError) as cm:
            Rectangle(0, 10)
        self.assertEqual(str(cm.exception), "width must be > 0")

        with self.assertRaises(TypeError) as cm:
            Rectangle("invalid", 10)
        self.assertEqual(str(cm.exception), "width must be an integer")

    def test_invalid_height(self):
        """Test invalid height"""
        with self.assertRaises(ValueError) as cm:
            Rectangle(10, -5)
        self.assertEqual(str(cm.exception), "height must be > 0")

        with self.assertRaises(TypeError) as cm:
            Rectangle(10, "invalid")
        self.assertEqual(str(cm.exception), "height must be an integer")

    def test_invalid_x(self):
        """Test invalid x"""
        with self.assertRaises(ValueError) as cm:
            Rectangle(10, 20, -1)
        self.assertEqual(str(cm.exception), "x must be >= 0")

        with self.assertRaises(TypeError) as cm:
            Rectangle(10, 20, "invalid")
        self.assertEqual(str(cm.exception), "x must be an integer")

    def test_invalid_y(self):
        """Test invalid y"""
        with self.assertRaises(ValueError) as cm:
            Rectangle(10, 20, 1, -2)
        self.assertEqual(str(cm.exception), "y must be >= 0")

        with self.assertRaises(TypeError) as cm:
            Rectangle(10, 20, 1, "invalid")
        self.assertEqual(str(cm.exception), "y must be an integer")


if __name__ == "__main__":
    unittest.main()

