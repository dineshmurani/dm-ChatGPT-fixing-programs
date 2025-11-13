import unittest
from unittest.mock import patch
from io import StringIO
import convert  # import your convert.py file

class TestConvertFunction(unittest.TestCase):
    """Tests for the convert(feet_inches) function."""

    def test_exact_conversion_values(self):
        self.assertAlmostEqual(convert.convert("5 0"), 1.524)
        self.assertAlmostEqual(convert.convert("4 6"), 1.3716)
        self.assertAlmostEqual(convert.convert("0 12"), 0.3048)
        self.assertAlmostEqual(convert.convert("0 0"), 0.0)
        self.assertAlmostEqual(convert.convert("6 2"), 1.8796)
        self.assertAlmostEqual(convert.convert("5.5 2.3"), 1.67642, places=5)

    def test_handles_large_values(self):
        # 10 feet 0 inches = 3.048 meters
        self.assertAlmostEqual(convert.convert("10 0"), 3.048)

    def test_handles_small_values(self):
        # 1 foot 0 inch = 0.3048 meters
        self.assertAlmostEqual(convert.convert("1 0"), 0.3048)

    def test_invalid_format_raises(self):
        with self.assertRaises(ValueError):
            convert.convert("five ten")
        with self.assertRaises(IndexError):
            convert.convert("5")  # missing inches part


class TestKidSlideOutput(unittest.TestCase):
    """Tests for the printed output logic using input and print mocking."""

    @patch("sys.stdout", new_callable=StringIO)
    @patch("builtins.input", return_value="3 5")  # 1.035 m
    def test_kid_can_use_slide(self, mock_input, mock_stdout):
        result = convert.convert(mock_input())
        if result < 1:
            print("Kid is too small.")
        else:
            print("Kid can use the slide.")
        output = mock_stdout.getvalue().strip()
        self.assertEqual(output, "Kid can use the slide.")

    @patch("sys.stdout", new_callable=StringIO)
    @patch("builtins.input", return_value="2 6")  # 0.762 m
    def test_kid_too_small(self, mock_input, mock_stdout):
        result = convert.convert(mock_input())
        if result < 1:
            print("Kid is too small.")
        else:
            print("Kid can use the slide.")
        output = mock_stdout.getvalue().strip()
        self.assertEqual(output, "Kid is too small.")

    @patch("sys.stdout", new_callable=StringIO)
    @patch("builtins.input", return_value="3 3")  # ~0.991 m (borderline)
    def test_kid_borderline_can_use_slide(self, mock_input, mock_stdout):
        result = convert.convert(mock_input())
        if result < 1:
            print("Kid is too small.")
        else:
            print("Kid can use the slide.")
        output = mock_stdout.getvalue().strip()
        self.assertEqual(output, "Kid can use the slide.")

    @patch("sys.stdout", new_callable=StringIO)
    @patch("builtins.input", return_value="0 11")  # 0.2794 m
    def test_tiny_kid_too_small(self, mock_input, mock_stdout):
        result = convert.convert(mock_input())
        if result < 1:
            print("Kid is too small.")
        else:
            print("Kid can use the slide.")
        output = mock_stdout.getvalue().strip()
        self.assertEqual(output, "Kid is too small.")

if __name__ == "__main__":
    unittest.main()
