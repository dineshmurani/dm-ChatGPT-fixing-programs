import unittest
from unittest.mock import patch
from io import StringIO
import convert  # the file containing the convert function


class TestKidSlide(unittest.TestCase):

    @patch("builtins.input", return_value="3 5")  # 3 feet 5 inches -> 1.035 m
    @patch("sys.stdout", new_callable=StringIO)
    def test_kid_can_use_slide(self, mock_stdout, mock_input):
        # simulate running the script
        result = convert.convert(mock_input())
        if result < 1:
            print("Kid is too small.")
        else:
            print("Kid can use the slide.")

        self.assertIn("Kid can use the slide.", mock_stdout.getvalue())

    @patch("builtins.input", return_value="2 6")  # 2 feet 6 inches -> 0.762 m
    @patch("sys.stdout", new_callable=StringIO)
    def test_kid_too_small(self, mock_stdout, mock_input):
        result = convert.convert(mock_input())
        if result < 1:
            print("Kid is too small.")
        else:
            print("Kid can use the slide.")

        self.assertIn("Kid is too small.", mock_stdout.getvalue())


if __name__ == "__main__":
    unittest.main()
