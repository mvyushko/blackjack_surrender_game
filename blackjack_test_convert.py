"""
Testing the money_to_chips(amount_to_convert) function from blackjack_with_chips with Unittest library
"""
import unittest
from blackjack_with_chips import money_to_chips

class TestCases(unittest.TestCase):

    def test_convert_chips_20_75(self):
        test_amount = 20.75
        convert_result = money_to_chips(test_amount)
        self.assertEqual({'White': 3, 'Pink': 1, 'Red': 3, 'Green': 0, 'Orange': 0, 'Amount': 20.5}, convert_result)

    def test_convert_chips_2_75(self):
        test_amount = 2.75
        convert_result = money_to_chips(test_amount)
        self.assertEqual({'White': 0, 'Pink': 1, 'Red': 0, 'Green': 0, 'Orange': 0, 'Amount': 2.5}, convert_result)

    def test_convert_chips_1_75(self):
        test_amount = 1.75
        convert_result = money_to_chips(test_amount)
        self.assertEqual({'White': 1, 'Pink': 0, 'Red': 0, 'Green': 0, 'Orange': 0, 'Amount': 1}, convert_result)

    def test_convert_chips_0_75(self):
        test_amount = 0.75
        convert_result = money_to_chips(test_amount)
        self.assertEqual({'White': 0, 'Pink': 0, 'Red': 0, 'Green': 0, 'Orange': 0, 'Amount': 0}, convert_result)

    def test_convert_chips_1_5(self):
        test_amount = 1.5
        convert_result = money_to_chips(test_amount)
        self.assertEqual({'White': 1, 'Pink': 0, 'Red': 0, 'Green': 0, 'Orange': 0, 'Amount': 1}, convert_result)

    def test_convert_chips_51_5(self):
        test_amount = 51.5
        convert_result = money_to_chips(test_amount)
        self.assertEqual({'White': 4, 'Pink': 1, 'Red': 4, 'Green': 1, 'Orange': 0, 'Amount': 51.5}, convert_result)

    def test_convert_chips_131_25(self):
        test_amount = 131.25
        convert_result = money_to_chips(test_amount)
        self.assertEqual({'White': 1, 'Pink': 0, 'Red': 1, 'Green': 1, 'Orange': 2, 'Amount': 131}, convert_result)

if __name__ == '__main__':
    unittest.main()