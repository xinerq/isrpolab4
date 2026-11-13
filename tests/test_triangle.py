import unittest

import triangle


class TriangleTestCase(unittest.TestCase):

    def test_area_positive_base_and_height(self):
        self.assertEqual(triangle.area(6, 4), 12)

    def test_area_zero_height(self):
        self.assertEqual(triangle.area(6, 0), 0)

    def test_area_zero_base(self):
        self.assertEqual(triangle.area(0, 4), 0)

    def test_area_fractional_values(self):
        self.assertAlmostEqual(triangle.area(2.5, 1.2), 1.5)

    def test_area_large_values(self):
        self.assertEqual(triangle.area(1_000_000, 2_000_000), 1_000_000_000_000)

    def test_perimeter_three_four_five(self):
        self.assertEqual(triangle.perimeter(3, 4, 5), 12)

    def test_perimeter_equilateral(self):
        self.assertEqual(triangle.perimeter(5, 5, 5), 15)

    def test_perimeter_fractional_sides(self):
        self.assertAlmostEqual(triangle.perimeter(2.5, 3.5, 4.5), 10.5)

    def test_perimeter_zero_sides(self):
        self.assertEqual(triangle.perimeter(0, 0, 0), 0)

    def test_perimeter_large_sides(self):
        self.assertEqual(triangle.perimeter(3_000_000, 4_000_000, 5_000_000), 12_000_000)
