import math
import unittest

import circle


class CircleTestCase(unittest.TestCase):

    def test_area_zero_radius(self):
        self.assertEqual(circle.area(0), 0)

    def test_area_unit_radius(self):
        self.assertAlmostEqual(circle.area(1), math.pi)

    def test_area_fractional_radius(self):
        self.assertAlmostEqual(circle.area(2.5), 6.25 * math.pi)

    def test_area_large_radius(self):
        self.assertAlmostEqual(circle.area(1000), 1000_000 * math.pi)

    def test_perimeter_zero_radius(self):
        self.assertEqual(circle.perimeter(0), 0)

    def test_perimeter_unit_radius(self):
        self.assertAlmostEqual(circle.perimeter(1), 2 * math.pi)

    def test_perimeter_fractional_radius(self):
        self.assertAlmostEqual(circle.perimeter(2.5), 5 * math.pi)

    def test_perimeter_large_radius(self):
        self.assertAlmostEqual(circle.perimeter(1000), 2000 * math.pi)
