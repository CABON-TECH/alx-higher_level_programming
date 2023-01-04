import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    def test_type(self):
        self.assertRaises(TypeError, max_integer, True)
    def test_max(self):
        self.assertEqual(max_integer([]), None)
        self.assertEqual(max_integer([1, 3, 2]), 3)
        self.assertEqual(max_integer([-1, -3, -2]), -1)
        self.assertEqual(max_integer([9]), 9)
        self.assertEqual(max_integer([1, 3, 7]), 7)
