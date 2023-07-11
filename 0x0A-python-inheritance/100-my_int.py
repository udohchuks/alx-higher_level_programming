#!/usr/bin/python3

"""
Myint
"""


class MyInt(int):
    """
    Int inversed
    """
    def __eq__(self, other):
        """Inverses equality """
        if self.real == other:
            return False
        return True

    def __ne__(self, other):
        """reverses not equal"""

        if self.real != other:
            return False
        return True
