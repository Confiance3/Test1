import unittest

from bmi import calculate_bmi, bmi_category


class TestBMI(unittest.TestCase):
    def test_calculate_bmi_normal(self):
        # Exemple: 70 kg, 1.75 m => IMC ≈ 22.857
        bmi = calculate_bmi(70, 1.75)
        self.assertAlmostEqual(bmi, 70 / (1.75 * 1.75), places=6)

    def test_bmi_category(self):
        self.assertEqual(bmi_category(16), "Maigreur")
        self.assertEqual(bmi_category(22), "Normal")
        self.assertEqual(bmi_category(27), "Surpoids")
        self.assertEqual(bmi_category(32), "Obésité (classe I)")
        self.assertEqual(bmi_category(37), "Obésité (classe II)")
        self.assertEqual(bmi_category(45), "Obésité (classe III)")

    def test_invalid_inputs(self):
        with self.assertRaises(ValueError):
            calculate_bmi(0, 1.75)
        with self.assertRaises(ValueError):
            calculate_bmi(70, 0)


if __name__ == "__main__":
    unittest.main()
