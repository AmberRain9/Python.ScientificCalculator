import unittest
from calculator import Calculator


class TestCalculator(unittest.TestCase):

    def test_add(self):
        c = Calculator()
        c.add(3)
        self.assertEqual(c.get_display(), "3")
        c.add(3)
        self.assertEqual(c.get_display(), "6")

    def test_subtract(self):
        c = Calculator()
        c.add(10)  # Start from 10
        c.subtract(4)
        self.assertEqual(c.get_display(), "6")

    def test_multiply(self):
        c = Calculator()
        c.add(5)
        c.multiply(3)
        self.assertEqual(c.get_display(), "15")

    def test_divide(self):
        c = Calculator()
        c.add(20)
        c.divide(4)
        self.assertEqual(c.get_display(), "5")

    def test_divide_by_zero(self):
        c = Calculator()
        c.add(10)
        c.divide(0)
        self.assertEqual(c.get_display(), "Err")

    def test_clear(self):
        c = Calculator()
        c.add(5)
        c.clear()
        self.assertEqual(c.get_display(), "0")

    def test_square_and_sqrt(self):
        c = Calculator()
        c.add(4)
        c.square()
        self.assertEqual(c.get_display(), "16")
        c.square_root()
        self.assertEqual(c.get_display(), "4.0")

    def test_power(self):
        c = Calculator()
        c.add(2)
        c.power(3)
        self.assertEqual(c.get_display(), "8")

    def test_inverse(self):
        c = Calculator()
        c.add(4)
        c.inverse()
        self.assertEqual(c.get_display(), "0.25")

    def test_invert_sign(self):
        c = Calculator()
        c.add(7)
        c.invert_sign()
        self.assertEqual(c.get_display(), "-7")


if __name__ == '__main__':
    unittest.main()