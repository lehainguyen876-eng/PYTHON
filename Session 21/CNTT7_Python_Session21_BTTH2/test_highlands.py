import unittest
from pos_logic import (
    add_item_to_order, calculate_total, 
    InvalidQuantityError, ItemNotFoundError
)

class TestHighlandsPOS(unittest.TestCase):

    def test_calculate_total(self) -> None:

        mock_order = [
            {"code": "P1", "price": 35000, "quantity": 2},
            {"code": "F1", "price": 55000, "quantity": 1}
        ]
        result = calculate_total(mock_order)
        self.assertEqual(result, 125000)

    def test_invalid_quantity(self) -> None:
        empty_order = []
        with self.assertRaises(InvalidQuantityError):
            add_item_to_order(empty_order, "T1", -1)


if __name__ == "__main__":
    unittest.main()