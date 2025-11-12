import unittest
from convert import convert

class TestConvert(unittest.TestCase):

    def test_only_feet(self):
        # 5 feet 0 inches -> 1.524 meters
        self.assertAlmostEqual(convert("5 0"), 1.524)

    def test_feet_and_inches(self):
        # 4 feet 6 inches -> 1.3716 meters
        self.assertAlmostEqual(convert("4 6"), 1.3716)

    def test_only_inches(self):
        # 0 feet 12 inches -> 0.3048 meters
        self.assertAlmostEqual(convert("0 12"), 0.3048)

    def test_zero_feet_inches(self):
        # 0 feet 0 inches -> 0 meters
        self.assertEqual(convert("0 0"), 0)

    def test_decimal_input(self):
        # 5.5 feet 2.3 inches -> 1.67642 meters
        self.assertAlmostEqual(convert("5.5 2.3"), 1.67642, places=5)

if __name__ == "__main__":
    unittest.main()
