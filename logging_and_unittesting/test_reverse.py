import unittest
from logging_and_unittesting.basic_logging import reverse


class TestReverse(unittest.TestCase):
    def test_answer(self):
        self.assertAlmostEqual(reverse(4), -4)
        self.assertAlmostEqual(reverse(1), -1)
        self.assertAlmostEqual(reverse(4.354), -4.354)
        self.assertAlmostEqual(reverse(5325.572940), -5325.572940)
        self.assertAlmostEqual(reverse(-5325.572940), 5325.572940)
        self.assertAlmostEqual(reverse(0), 0)

    def test_exceptions(self):
        self.assertRaises(TypeError, reverse, "Hello")
        self.assertRaises(TypeError, reverse, [12, 16, 12])
        self.assertRaises(TypeError, reverse, (12, 54, 90))
        self.assertRaises(TypeError, reverse, True)
        self.assertRaises(TypeError, reverse, False)


if __name__ == '__main__':
    unittest.main()
