import unittest

import rectangle


class RectangleTestCase(unittest.TestCase):

    def test_area_positive_integer_sides(self):
        self.assertEqual(rectangle.area(4, 7), 28)

    def test_area_zero_first_side(self):
        self.assertEqual(rectangle.area(0, 7), 0)

    def test_area_zero_second_side(self):
        self.assertEqual(rectangle.area(7, 0), 0)

    def test_area_fractional_sides(self):
        self.assertAlmostEqual(rectangle.area(2.5, 1.2), 3.0)

    def test_area_large_sides(self):
        self.assertEqual(rectangle.area(1_000_000, 2_000_000), 2_000_000_000_000)

    def test_perimeter_positive_integer_sides(self):
        self.assertEqual(rectangle.perimeter(4, 7), 22)

    def test_perimeter_equal_sides(self):
        self.assertEqual(rectangle.perimeter(10, 10), 40)

    def test_perimeter_fractional_sides(self):
        self.assertAlmostEqual(rectangle.perimeter(1.5, 2.25), 7.5)

    def test_perimeter_zero_side(self):
        self.assertEqual(rectangle.perimeter(0, 7), 14)

    def test_perimeter_large_sides(self):
        self.assertEqual(rectangle.perimeter(1_000_000, 2_000_000), 6_000_000)
