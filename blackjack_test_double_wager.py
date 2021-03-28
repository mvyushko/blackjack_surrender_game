"""
Testing player.double_wager(self, move) method from blackjack_with_chips with Unittest library
"""
import unittest
from blackjack_with_chips import HumanPlayer

class TestCases(unittest.TestCase):

    def test_double_wager_2_1(self):
        """
        testing doubling down with 2 White and 2 Red chips in HumanPlayer's chip pile and 1 White and 1 Red in
         HumanPlayer's wager
        """
        player = HumanPlayer('Masha')
        test_chips = 2
        test_wager = 1
        test_total = 12
        player.chips = {'White': test_chips, 'Pink': 0, 'Red': test_chips, 'Green': 0, 'Orange': 0}
        player.wager = {'White': test_wager, 'Pink': 0, 'Red': test_wager, 'Green': 0, 'Orange': 0}
        player.wager_amount = 6
        player.chips_total = test_total

        #testing the double_wager(self,move) method
        result_amount, result_chips, result_chips_total, result_chips_left, result_split_amounts, result_splits =\
            player.double_wager('Double Down')
        self.assertEqual(result_amount, 12)
        self.assertEqual(result_chips, {'White': 2, 'Pink': 0, 'Red': 2, 'Green': 0, 'Orange': 0})
        self.assertEqual(result_chips_total, 6)
        self.assertEqual(result_chips_left, {'White': 1, 'Pink': 0, 'Red': 1, 'Green': 0, 'Orange': 0})
        self.assertEqual(result_split_amounts, [])
        self.assertEqual(result_splits, [])

    def test_double_wager_4red_1(self):
        """
        testing doubling down with 4 Red chips in HumanPlayer's chip pile and 1 White and 1 Red in
         HumanPlayer's wager
        """
        player = HumanPlayer('Masha')
        test_chips = 4
        test_wager = 1
        test_total = 20
        player.chips = {'White': 0, 'Pink': 0, 'Red': test_chips, 'Green': 0, 'Orange': 0}
        player.wager = {'White': test_wager, 'Pink': 0, 'Red': test_wager, 'Green': 0, 'Orange': 0}
        player.wager_amount = 6
        player.chips_total = test_total

        #testing the double_wager(self,move) method
        result_amount, result_chips, result_chips_total, result_chips_left, result_split_amounts, result_splits =\
            player.double_wager('Double Down')
        self.assertEqual(result_amount, 12)
        self.assertEqual(result_chips, {'White': 2, 'Pink': 0, 'Red': 2, 'Green': 0, 'Orange': 0})
        self.assertEqual(result_chips_total, 14)
        self.assertEqual(result_chips_left, {'White': 4, 'Pink': 0, 'Red': 2, 'Green': 0, 'Orange': 0})
        self.assertEqual(result_split_amounts, [])
        self.assertEqual(result_splits, [])

    def test_double_wager_2_1_split(self):
        """
        testing splitting with 2 White and 2 Red chips in HumanPlayer's chip pile and 1 White and 1 Red in
         HumanPlayer's wager
        """
        player = HumanPlayer('Masha')
        test_chips = 2
        test_wager = 1
        test_total = 12
        player.chips = {'White': test_chips, 'Pink': 0, 'Red': test_chips, 'Green': 0, 'Orange': 0}
        player.wager = {'White': test_wager, 'Pink': 0, 'Red': test_wager, 'Green': 0, 'Orange': 0}
        player.wager_amount = 6
        player.chips_total = test_total

        #testing the double_wager(self,move) method
        result_amount, result_chips, result_chips_total, result_chips_left, result_split_amounts, result_splits =\
            player.double_wager('Split')
        self.assertEqual(result_amount, 6)
        self.assertEqual(result_chips, {'White': 1, 'Pink': 0, 'Red': 1, 'Green': 0, 'Orange': 0})
        self.assertEqual(result_chips_total, 6)
        self.assertEqual(result_chips_left, {'White': 1, 'Pink': 0, 'Red': 1, 'Green': 0, 'Orange': 0})
        self.assertEqual(result_split_amounts, [6])
        self.assertEqual(result_splits, [{'White': 1, 'Pink': 0, 'Red': 1, 'Green': 0, 'Orange': 0}])

    def test_double_wager_4red_1_split(self):
        """
        testing splitting with 4 Red chips in HumanPlayer's chip pile and 1 White and 1 Red in
         HumanPlayer's wager
        """
        player = HumanPlayer('Masha')
        test_chips = 4
        test_wager = 1
        test_total = 20
        player.chips = {'White': 0, 'Pink': 0, 'Red': test_chips, 'Green': 0, 'Orange': 0}
        player.wager = {'White': test_wager, 'Pink': 0, 'Red': test_wager, 'Green': 0, 'Orange': 0}
        player.wager_amount = 6
        player.chips_total = test_total

        #testing the double_wager(self,move) method
        result_amount, result_chips, result_chips_total, result_chips_left, result_split_amounts, result_splits =\
            player.double_wager('Split')
        self.assertEqual(result_amount, 6)
        self.assertEqual(result_chips, {'White': 1, 'Pink': 0, 'Red': 1, 'Green': 0, 'Orange': 0})
        self.assertEqual(result_chips_total, 14)
        self.assertEqual(result_chips_left, {'White': 4, 'Pink': 0, 'Red': 2, 'Green': 0, 'Orange': 0})
        self.assertEqual(result_split_amounts, [6])
        self.assertEqual(result_splits, [{'White': 1, 'Pink': 0, 'Red': 1, 'Green': 0, 'Orange': 0}])

    def test_double_wager_4red_1_second_split(self):
        """
        testing splitting with 4 Red chips in HumanPlayer's chip pile, 1 White and 1 Red in
         HumanPlayer's wager, and 1 White and 1 Red in HumanPlayer's first split wager
        """
        player = HumanPlayer('Masha')
        test_chips = 4
        test_wager = 1
        test_total = 20
        player.chips = {'White': 0, 'Pink': 0, 'Red': test_chips, 'Green': 0, 'Orange': 0}
        player.wager = {'White': test_wager, 'Pink': 0, 'Red': test_wager, 'Green': 0, 'Orange': 0}
        player.split_wagers = [{'White': test_wager, 'Pink': 0, 'Red': test_wager, 'Green': 0, 'Orange': 0}]
        player.wager_amount = 6
        player.split_wager_amounts = [6]
        player.chips_total = test_total

        #testing the double_wager(self,move) method
        result_amount, result_chips, result_chips_total, result_chips_left, result_split_amounts, result_splits =\
            player.double_wager('Split')
        self.assertEqual(result_amount, 6)
        self.assertEqual(result_chips, {'White': 1, 'Pink': 0, 'Red': 1, 'Green': 0, 'Orange': 0})
        self.assertEqual(result_chips_total, 14)
        self.assertEqual(result_chips_left, {'White': 4, 'Pink': 0, 'Red': 2, 'Green': 0, 'Orange': 0})
        self.assertEqual(result_split_amounts, [6,6])
        self.assertEqual(result_splits, [{'White': 1, 'Pink': 0, 'Red': 1, 'Green': 0, 'Orange': 0},
                                         {'White': 1, 'Pink': 0, 'Red': 1, 'Green': 0, 'Orange': 0}])


if __name__ == '__main__':
    unittest.main()
