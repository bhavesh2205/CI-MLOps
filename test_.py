import unittest
from app import calculate_bmi


class TestBMICalculator(unittest.TestCase):
    def test_underweight(self):
        self.assertEqual(calculate_bmi(45, 1.75), (14.69, "Underweight"))

    def test_normal_weight(self):
        self.assertEqual(calculate_bmi(70, 1.75), (22.86, "Normal weight"))

    def test_overweight(self):
        self.assertEqual(calculate_bmi(85, 1.75), (27.76, "Overweight"))

    def test_obese(self):
        self.assertEqual(calculate_bmi(100, 1.75), (32.65, "Obese"))

    def test_invalid_input(self):
        with self.assertRaises(ValueError):
            calculate_bmi(-10, 1.75)


if __name__ == "__main__":
    unittest.main()
