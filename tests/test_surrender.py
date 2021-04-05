"""
Testing surrender(self) method of HumanPlayer class from blackjack_with_chips with Unittest library
"""
import unittest
from player_classes import HumanPlayer

class TestSurrender(unittest.TestCase):

    def test_surrender_1_2(self):
        """
        testing doubling down with 1 White and 1 Red chips in HumanPlayer's chip pile and 2 White and 2 Red in
        HumanPlayer's wager
        """
        player = HumanPlayer('Masha')
        test_chips = 1
        test_wager = 2
        test_total = 6
        player.chips = {'White': test_chips, 'Pink': 0, 'Red': test_chips, 'Green': 0, 'Orange': 0,
                        'Amount': test_total}
        player.wagers = {'Main Wager': {'White': test_wager, 'Pink': 0, 'Red': test_wager, 'Green': 0, 'Orange': 0,
                                        'Amount': 12},
                 'Insurance': {'White': 0, 'Pink':0, 'Red': 0, 'Green': 0, 'Orange': 0, 'Amount': 0},
                 'Split Wager 1': {'White': 0, 'Pink':0, 'Red': 0, 'Green': 0, 'Orange': 0, 'Amount': 0},
                 'Split Wager 2': {'White': 0, 'Pink':0, 'Red': 0, 'Green': 0, 'Orange': 0, 'Amount': 0},
                 'Split Wager 3': {'White': 0, 'Pink':0, 'Red': 0, 'Green': 0, 'Orange': 0, 'Amount': 0}}

        #testing the double_wager(self,move, split_wager_number=0, new_split_wager_number=1) method
        player.surrender()
        result_chips = player.chips
        self.assertEqual(result_chips, {'White': 2, 'Pink': 0, 'Red': 2, 'Green': 0, 'Orange': 0,
                                                        'Amount': 12})

    def test_surrender_1_1(self):
        """
        testing doubling down with 1 White and 1 Red chips in HumanPlayer's chip pile and 1 White and 1 Red in
        HumanPlayer's wager
        """
        player = HumanPlayer('Masha')
        test_chips = 1
        test_wager = 1
        test_total = 6
        player.chips = {'White': test_chips, 'Pink': 0, 'Red': test_chips, 'Green': 0, 'Orange': 0,
                        'Amount': test_total}
        player.wagers = {'Main Wager': {'White': test_wager, 'Pink': 0, 'Red': test_wager, 'Green': 0, 'Orange': 0,
                                        'Amount': 6},
                 'Insurance': {'White': 0, 'Pink':0, 'Red': 0, 'Green': 0, 'Orange': 0, 'Amount': 0},
                 'Split Wager 1': {'White': 0, 'Pink':0, 'Red': 0, 'Green': 0, 'Orange': 0, 'Amount': 0},
                 'Split Wager 2': {'White': 0, 'Pink':0, 'Red': 0, 'Green': 0, 'Orange': 0, 'Amount': 0},
                 'Split Wager 3': {'White': 0, 'Pink':0, 'Red': 0, 'Green': 0, 'Orange': 0, 'Amount': 0}}

        #testing the double_wager(self,move, split_wager_number=0, new_split_wager_number=1) method
        player.surrender()
        result_chips = player.chips
        self.assertEqual(result_chips, {'White': 4, 'Pink': 0, 'Red': 1, 'Green': 0, 'Orange': 0,
                                                        'Amount': 9})

    def test_surrender_1_1pink(self):
        """
        testing doubling down with 1 White and 1 Red chips in HumanPlayer's chip pile and 1 White and 1 Pink in
        HumanPlayer's wager
        """
        player = HumanPlayer('Masha')
        test_chips = 1
        test_wager = 1
        test_total = 6
        player.chips = {'White': test_chips, 'Pink': 0, 'Red': test_chips, 'Green': 0, 'Orange': 0,
                        'Amount': test_total}
        player.wagers = {'Main Wager': {'White': test_wager, 'Pink': test_wager, 'Red': 0, 'Green': 0, 'Orange': 0,
                                        'Amount': 3.5},
                 'Insurance': {'White': 0, 'Pink':0, 'Red': 0, 'Green': 0, 'Orange': 0, 'Amount': 0},
                 'Split Wager 1': {'White': 0, 'Pink':0, 'Red': 0, 'Green': 0, 'Orange': 0, 'Amount': 0},
                 'Split Wager 2': {'White': 0, 'Pink':0, 'Red': 0, 'Green': 0, 'Orange': 0, 'Amount': 0},
                 'Split Wager 3': {'White': 0, 'Pink':0, 'Red': 0, 'Green': 0, 'Orange': 0, 'Amount': 0}}

        #testing the double_wager(self,move, split_wager_number=0, new_split_wager_number=1) method
        player.surrender()
        result_chips = player.chips
        self.assertEqual(result_chips, {'White': 2, 'Pink': 0, 'Red': 1, 'Green': 0, 'Orange': 0,
                                                        'Amount': 7})

if __name__ == '__main__':
    unittest.main()
