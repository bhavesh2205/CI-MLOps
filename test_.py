import unittest
from app import calculate_bmi


class TestBMICalculator(unittest.TestCase):
    def test_bmi_category(self):
        """Test different BMI categories"""
        self.assertEqual(calculate_bmi(50, 1.75)[1], "Underweight")  # BMI ~16.3
        self.assertEqual(calculate_bmi(68, 1.75)[1], "Normal weight")  # BMI ~22.2
        self.assertEqual(calculate_bmi(80, 1.75)[1], "Overweight")  # BMI ~26.1
        self.assertEqual(calculate_bmi(100, 1.75)[1], "Obese")  # BMI ~32.7

    def test_invalid_input(self):
        """Test negative and zero values"""
        with self.assertRaises(ValueError):
            calculate_bmi(-10, 1.75)  # Negative weight
        with self.assertRaises(ValueError):
            calculate_bmi(70, 0)  # Zero height


if __name__ == "__main__":
    unittest.main()
