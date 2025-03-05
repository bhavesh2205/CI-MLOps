import unittest
from app import calculate_bmi


class TestBMICalculator(unittest.TestCase):
    def test_underweight(self):
        bmi, category = calculate_bmi(50, 1.75)  # BMI = 16.33
        self.assertEqual(category, "Underweight")

    def test_normal_weight(self):
        bmi, category = calculate_bmi(68, 1.75)  # BMI = 22.2
        self.assertEqual(category, "Normal weight")

    def test_overweight(self):
        bmi, category = calculate_bmi(80, 1.75)  # BMI = 26.1
        self.assertEqual(category, "Overweight")

    def test_obese(self):
        bmi, category = calculate_bmi(100, 1.75)  # BMI = 32.65
        self.assertEqual(category, "Obese")

    def test_invalid_input(self):
        """Test invalid inputs (negative values)"""
        with self.assertRaises(ValueError):
            calculate_bmi(-10, 1.75)  # Negative weight

        with self.assertRaises(ValueError):
            calculate_bmi(70, -1.75)  # Negative height

        with self.assertRaises(ValueError):
            calculate_bmi(-70, -1.75)  # Both negative

    def test_zero_input(self):
        """Test zero values, which should also raise ValueError"""
        with self.assertRaises(ValueError):
            calculate_bmi(0, 1.75)  # Zero weight

        with self.assertRaises(ValueError):
            calculate_bmi(70, 0)  # Zero height


if __name__ == "__main__":
    unittest.main()
