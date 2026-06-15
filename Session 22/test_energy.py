import unittest
from main import calculate_energy_financials

class TestEnergy(unittest.TestCase):
    def test_empty_devices_list(self):
        self.assertEqual(calculate_energy_financials([]), (0.0, 0.0, 0.0))

    def test_financials_with_discount(self):
        devices = [{'old_index': 0, 'new_index': 60000}]
        usage, pct, cost = calculate_energy_financials(devices)
        self.assertEqual(pct, 3.0)
        self.assertEqual(cost, 60000 * 3000 * 0.97)

    def test_financials_no_discount(self):
        devices = [{'old_index': 0, 'new_index': 1000}]
        usage, pct, cost = calculate_energy_financials(devices)
        self.assertEqual(pct, 0.0)

if __name__ == "__main__":
    unittest.main()