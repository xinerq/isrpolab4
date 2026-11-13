import unittest

import square


class SquareTestCase(unittest.TestCase):

    def test_area_zero_side(self):
        self.assertEqual(square.area(0), 0)

    def test_area_unit_side(self):
        self.assertEqual(square.area(1), 1)

    def test_area_positive_side(self):
        self.assertEqual(square.area(7), 49)

    def test_area_fractional_side(self):
        self.assertAlmostEqual(square.area(2.5), 6.25)

    def test_area_large_side(self):
        self.assertEqual(square.area(100_000), 10_000_000_000)

    def test_perimeter_zero_side(self):
        self.assertEqual(square.perimeter(0), 0)

    def test_perimeter_unit_side(self):
        self.assertEqual(square.perimeter(1), 4)

    def test_perimeter_positive_side(self):
        self.assertEqual(square.perimeter(7), 28)

    def test_perimeter_fractional_side(self):
        self.assertAlmostEqual(square.perimeter(2.5), 10.0)

    def test_perimeter_large_side(self):
        self.assertEqual(square.perimeter(100_000), 400_000)

    def test_wrong_test(self):
        self.assertEqual(square.perimeter(100), 200)
