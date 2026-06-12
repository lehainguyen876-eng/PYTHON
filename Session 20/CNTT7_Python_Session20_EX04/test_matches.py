import unittest
from main import calculate_actual_pay

class TestTournamentMatches(unittest.TestCase):

    def test_calculate_actual_pay_active(self):
        active_player = {
            "player_id": "P01",
            "name": "Faker",
            "role": "Mid Lane",
            "salary": 5000.0,
            "status": "Active"
        }
        self.assertEqual(calculate_actual_pay(active_player), 5000.0)

    def test_calculate_actual_pay_benched(self):
        benched_player = {
            "player_id": "P03",
            "name": "Ruler",
            "role": "ADC",
            "salary": 6000.0,
            "status": "Benched"
        }
        self.assertEqual(calculate_actual_pay(benched_player), 3000.0)

if __name__ == "__main__":
    unittest.main()