import unittest
from logging_and_unittesting.more_tests.round_A import round_number_a
from logging_and_unittesting.more_tests.round_B import round_number_b


class TestReverse(unittest.TestCase):
    # Test for 'round_number_a'

    def test_answer(self):
        self.assertAlmostEqual(round_number_a(1.5), 2)
        self.assertAlmostEqual(round_number_a(1.2), 1)
        self.assertAlmostEqual(round_number_a(3.1415), 3)
        self.assertAlmostEqual(round_number_a(9.49308510843), 9)
        self.assertAlmostEqual(round_number_a(24.1), 24)
        self.assertAlmostEqual(round_number_a(25.7), 26)

    def test_exceptions(self):
        self.assertRaises(TypeError, round_number_a, "Hello")
        self.assertRaises(TypeError, round_number_a, [12, 16, 12])
        self.assertRaises(TypeError, round_number_a, (12, 54, 90))
        self.assertRaises(TypeError, round_number_a, True)
        self.assertRaises(TypeError, round_number_a, False)

    # Test for 'round_number_a'

    # def test_answer(self):
    #     self.assertAlmostEqual(round_number_b(1.5), 2)
    #     self.assertAlmostEqual(round_number_b(1.2), 1)
    #     self.assertAlmostEqual(round_number_b(3.1415), 3)
    #     self.assertAlmostEqual(round_number_b(9.49308510843), 9)
    #     self.assertAlmostEqual(round_number_b(24.1), 24)
    #     self.assertAlmostEqual(round_number_b(25.7), 26)
    #
    # def test_exceptions(self):
    #     self.assertRaises(TypeError, round_number_b, "Hello")
    #     self.assertRaises(TypeError, round_number_b, [12, 16, 12])
    #     self.assertRaises(TypeError, round_number_b, (12, 54, 90))
    #     self.assertRaises(TypeError, round_number_b, True)
    #     self.assertRaises(TypeError, round_number_b, False)

# In this example, 'round_number_a' will pass the method whereas 'round_number_b' will not pass the test
# This can be used in school assignments to test each student's functions and see if it is correct!


if __name__ == '__main__':
    unittest.main()
