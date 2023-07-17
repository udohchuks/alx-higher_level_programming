#!/usr/bin/python3

"""Square Test"""
import unittest
from models.square import Square


class TestSquare(unittest.TestCase):
    """TestSquare"""
    def test_size_getter(self):
        """getter"""
        s = Square(5)
        self.assertEqual(s.size, 5)

    def test_size_setter(self):
        """setter"""
        s = Square(5)
        s.size = 10
        self.assertEqual(s.size, 10)
        self.assertEqual(s.width, 10)
        self.assertEqual(s.height, 10)

    def test_size_setter_with_string(self):
        """setter"""
        s = Square(5)
        with self.assertRaises(TypeError) as e:
            s.size = "9"
        self.assertEqual(str(e.exception), "width must be an integer")

    def test_update_with_args(self):
        """args"""
        s = Square(5)
        s.update(1, 10, 2, 3)
        self.assertEqual(s.id, 1)
        self.assertEqual(s.size, 10)
        self.assertEqual(s.x, 2)
        self.assertEqual(s.y, 3)

    def test_update_with_kwargs(self):
        """Kwargs"""
        s = Square(5)
        s.update(size=20, y=4)
        self.assertEqual(s.size, 20)
        self.assertEqual(s.y, 4)

if __name__ == '__main__':
    unittest.main()
