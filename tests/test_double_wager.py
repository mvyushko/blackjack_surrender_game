"""
Testing double_wager(self, move, split_wager_number=0, new_split_wager_number=1) method of HumanPlayer class from
blackjack_with_chips with Unittest library
"""
import unittest
from player_classes import HumanPlayer

class TestDoubleWager(unittest.TestCase):

    def test_double_wager_2_1(self):
        """
        testing doubling down with 2 White and 2 Red chips in HumanPlayer's chip pile and 1 White and 1 Red in
        HumanPlayer's wager
        """
        player = HumanPlayer('Masha')
        test_chips = 2
        test_wager = 1
        test_total = 12
        player.chips = {'White': test_chips, 'Pink': 0, 'Red': test_chips, 'Green': 0, 'Orange': 0, 'Amount': test_total}
        player.wagers = {'Main Wager': {'White': test_wager, 'Pink': 0, 'Red': test_wager, 'Green': 0, 'Orange': 0,
                                        'Amount': 6},
                 'Insurance': {'White': 0, 'Pink':0, 'Red': 0, 'Green': 0, 'Orange': 0, 'Amount': 0},
                 'Split Wager 1': {'White': 0, 'Pink':0, 'Red': 0, 'Green': 0, 'Orange': 0, 'Amount': 0},
                 'Split Wager 2': {'White': 0, 'Pink':0, 'Red': 0, 'Green': 0, 'Orange': 0, 'Amount': 0},
                 'Split Wager 3': {'White': 0, 'Pink':0, 'Red': 0, 'Green': 0, 'Orange': 0, 'Amount': 0}}

        #testing the double_wager(self,move, split_wager_number=0, new_split_wager_number=1) method
        result_wagers, result_chips = player.double_wager('Double Down')
        self.assertEqual(result_wagers, {'Main Wager': {'White': 2, 'Pink': 0, 'Red': 2, 'Green': 0, 'Orange': 0,
                                                        'Amount': 12},
                 'Insurance': {'White': 0, 'Pink':0, 'Red': 0, 'Green': 0, 'Orange': 0, 'Amount': 0},
                 'Split Wager 1': {'White': 0, 'Pink':0, 'Red': 0, 'Green': 0, 'Orange': 0, 'Amount': 0},
                 'Split Wager 2': {'White': 0, 'Pink':0, 'Red': 0, 'Green': 0, 'Orange': 0, 'Amount': 0},
                 'Split Wager 3': {'White': 0, 'Pink':0, 'Red': 0, 'Green': 0, 'Orange': 0, 'Amount': 0}})
        self.assertEqual(result_chips, {'White': 1, 'Pink': 0, 'Red': 1, 'Green': 0, 'Orange': 0, 'Amount': 6})

    def test_double_wager_4red_1(self):
        """
        testing doubling down with 4 Red chips in HumanPlayer's chip pile and 1 White and 1 Red in
         HumanPlayer's wager
        """
        player = HumanPlayer('Masha')
        test_chips = 4
        test_wager = 1
        test_total = 20
        player.chips = {'White': 0, 'Pink': 0, 'Red': test_chips, 'Green': 0, 'Orange': 0, 'Amount': test_total}
        player.wagers = {'Main Wager': {'White': test_wager, 'Pink': 0, 'Red': test_wager, 'Green': 0, 'Orange': 0,
                                        'Amount': 6},
                         'Insurance': {'White': 0, 'Pink': 0, 'Red': 0, 'Green': 0, 'Orange': 0, 'Amount': 0},
                         'Split Wager 1': {'White': 0, 'Pink': 0, 'Red': 0, 'Green': 0, 'Orange': 0, 'Amount': 0},
                         'Split Wager 2': {'White': 0, 'Pink': 0, 'Red': 0, 'Green': 0, 'Orange': 0, 'Amount': 0},
                         'Split Wager 3': {'White': 0, 'Pink': 0, 'Red': 0, 'Green': 0, 'Orange': 0, 'Amount': 0}}

        #testing the double_wager(self,move, split_wager_number=0, new_split_wager_number=1) method
        result_wagers, result_chips_left = player.double_wager('Double Down')
        self.assertEqual(result_wagers, {'Main Wager': {'White': 2, 'Pink': 0, 'Red': 2, 'Green': 0, 'Orange': 0,
                                                        'Amount': 12},
                 'Insurance': {'White': 0, 'Pink':0, 'Red': 0, 'Green': 0, 'Orange': 0, 'Amount': 0},
                 'Split Wager 1': {'White': 0, 'Pink':0, 'Red': 0, 'Green': 0, 'Orange': 0, 'Amount': 0},
                 'Split Wager 2': {'White': 0, 'Pink':0, 'Red': 0, 'Green': 0, 'Orange': 0, 'Amount': 0},
                 'Split Wager 3': {'White': 0, 'Pink':0, 'Red': 0, 'Green': 0, 'Orange': 0, 'Amount': 0}})
        self.assertEqual(result_chips_left, {'White': 4, 'Pink': 0, 'Red': 2, 'Green': 0, 'Orange': 0, 'Amount': 14})

    def test_double_wager_2_1_split(self):
        """
        testing splitting with 2 White and 2 Red chips in HumanPlayer's chip pile and 1 White and 1 Red in
         HumanPlayer's wager
        """
        player = HumanPlayer('Masha')
        test_chips = 2
        test_wager = 1
        test_total = 12
        player.chips = {'White': test_chips, 'Pink': 0, 'Red': test_chips, 'Green': 0, 'Orange': 0,
                        'Amount': test_total}
        player.wagers = {'Main Wager': {'White': test_wager, 'Pink': 0, 'Red': test_wager, 'Green': 0, 'Orange': 0,
                                        'Amount': 6},
                         'Insurance': {'White': 0, 'Pink': 0, 'Red': 0, 'Green': 0, 'Orange': 0, 'Amount': 0},
                         'Split Wager 1': {'White': 0, 'Pink': 0, 'Red': 0, 'Green': 0, 'Orange': 0, 'Amount': 0},
                         'Split Wager 2': {'White': 0, 'Pink': 0, 'Red': 0, 'Green': 0, 'Orange': 0, 'Amount': 0},
                         'Split Wager 3': {'White': 0, 'Pink': 0, 'Red': 0, 'Green': 0, 'Orange': 0, 'Amount': 0}}

        #testing the double_wager(self,move, split_wager_number=0, new_split_wager_number=1) method
        result_wagers, result_chips_left = player.double_wager('Split')
        self.assertEqual(result_wagers, {'Main Wager': {'White': 1, 'Pink': 0, 'Red': 1, 'Green': 0, 'Orange': 0,
                                        'Amount': 6},
                         'Insurance': {'White': 0, 'Pink': 0, 'Red': 0, 'Green': 0, 'Orange': 0, 'Amount': 0},
                         'Split Wager 1': {'White': 1, 'Pink': 0, 'Red': 1, 'Green': 0, 'Orange': 0, 'Amount': 6},
                         'Split Wager 2': {'White': 0, 'Pink': 0, 'Red': 0, 'Green': 0, 'Orange': 0, 'Amount': 0},
                         'Split Wager 3': {'White': 0, 'Pink': 0, 'Red': 0, 'Green': 0, 'Orange': 0, 'Amount': 0}})
        self.assertEqual(result_chips_left, {'White': 1, 'Pink': 0, 'Red': 1, 'Green': 0, 'Orange': 0, 'Amount': 6})

    def test_double_wager_4red_1_split(self):
        """
        testing splitting with 4 Red chips in HumanPlayer's chip pile and 1 White and 1 Red in
         HumanPlayer's wager
        """
        player = HumanPlayer('Masha')
        test_chips = 4
        test_wager = 1
        test_total = 20
        player.chips = {'White': 0, 'Pink': 0, 'Red': test_chips, 'Green': 0, 'Orange': 0, 'Amount': test_total}
        player.wagers = {'Main Wager': {'White': test_wager, 'Pink': 0, 'Red': test_wager, 'Green': 0, 'Orange': 0,
                                        'Amount': 6},
                         'Insurance': {'White': 0, 'Pink': 0, 'Red': 0, 'Green': 0, 'Orange': 0, 'Amount': 0},
                         'Split Wager 1': {'White': 0, 'Pink': 0, 'Red': 0, 'Green': 0, 'Orange': 0,
                                           'Amount': 0},
                         'Split Wager 2': {'White': 0, 'Pink': 0, 'Red': 0, 'Green': 0, 'Orange': 0, 'Amount': 0},
                         'Split Wager 3': {'White': 0, 'Pink': 0, 'Red': 0, 'Green': 0, 'Orange': 0, 'Amount': 0}}

        #testing the double_wager(self,move, split_wager_number=0, new_split_wager_number=1) method
        result_wagers, result_chips_left = player.double_wager('Split')
        self.assertEqual(result_wagers, {'Main Wager': {'White': 1, 'Pink': 0, 'Red': 1, 'Green': 0, 'Orange': 0,
                                        'Amount': 6},
                         'Insurance': {'White': 0, 'Pink': 0, 'Red': 0, 'Green': 0, 'Orange': 0, 'Amount': 0},
                         'Split Wager 1': {'White': 1, 'Pink': 0, 'Red': 1, 'Green': 0, 'Orange': 0,
                                           'Amount': 6},
                         'Split Wager 2': {'White': 0, 'Pink': 0, 'Red': 0, 'Green': 0, 'Orange': 0, 'Amount': 0},
                         'Split Wager 3': {'White': 0, 'Pink': 0, 'Red': 0, 'Green': 0, 'Orange': 0, 'Amount': 0}})
        self.assertEqual(result_chips_left, {'White': 4, 'Pink': 0, 'Red': 2, 'Green': 0, 'Orange': 0, 'Amount': 14})

    def test_double_wager_4red_1_second_split(self):
        """
        testing splitting the Split Wager 1 with 4 Red chips in HumanPlayer's chip pile, 1 White and 1 Red in
         HumanPlayer's wager, and 1 White and 1 Red in HumanPlayer's Split Wager 1
        """
        player = HumanPlayer('Masha')
        test_chips = 4
        test_wager = 1
        test_total = 20
        player.chips = {'White': 0, 'Pink': 0, 'Red': test_chips, 'Green': 0, 'Orange': 0, 'Amount': test_total}
        player.wagers = {'Main Wager': {'White': test_wager, 'Pink': 0, 'Red': test_wager, 'Green': 0, 'Orange': 0,
                                        'Amount': 6},
                         'Insurance': {'White': 0, 'Pink': 0, 'Red': 0, 'Green': 0, 'Orange': 0, 'Amount': 0},
                         'Split Wager 1': {'White': test_wager, 'Pink': 0, 'Red': test_wager, 'Green': 0, 'Orange': 0,
                                           'Amount': 6},
                         'Split Wager 2': {'White': 0, 'Pink': 0, 'Red': 0, 'Green': 0, 'Orange': 0, 'Amount': 0},
                         'Split Wager 3': {'White': 0, 'Pink': 0, 'Red': 0, 'Green': 0, 'Orange': 0, 'Amount': 0}}

        #testing the double_wager(self,move, split_wager_number=0, new_split_wager_number=1) method
        result_wagers, result_chips_left = player.double_wager('Split', 1, 2)
        self.assertEqual(result_wagers, {'Main Wager': {'White': 1, 'Pink': 0, 'Red': 1, 'Green': 0, 'Orange': 0,
                                        'Amount': 6},
                         'Insurance': {'White': 0, 'Pink': 0, 'Red': 0, 'Green': 0, 'Orange': 0, 'Amount': 0},
                         'Split Wager 1': {'White': 1, 'Pink': 0, 'Red': 1, 'Green': 0, 'Orange': 0,
                                           'Amount': 6},
                         'Split Wager 2': {'White': 1, 'Pink': 0, 'Red': 1, 'Green': 0, 'Orange': 0, 'Amount': 6},
                         'Split Wager 3': {'White': 0, 'Pink': 0, 'Red': 0, 'Green': 0, 'Orange': 0, 'Amount': 0}})
        self.assertEqual(result_chips_left, {'White': 4, 'Pink': 0, 'Red': 2, 'Green': 0, 'Orange': 0, 'Amount': 14})


    def test_double_wager_4red_2_second_split_main(self):
        """
        testing splitting Main Wager with 4 Red chips in HumanPlayer's chip pile, 1 White and 1 Red in
         HumanPlayer's wager, and 1 White and 2 Red in HumanPlayer's first split wager
        """
        player = HumanPlayer('Masha')
        test_chips = 4
        test_wager = 1
        test_total = 20
        player.chips = {'White': 0, 'Pink': 0, 'Red': test_chips, 'Green': 0, 'Orange': 0, 'Amount': test_total}
        player.wagers = {'Main Wager': {'White': test_wager, 'Pink': 0, 'Red': test_wager, 'Green': 0, 'Orange': 0,
                                        'Amount': 6},
                         'Insurance': {'White': 0, 'Pink': 0, 'Red': 0, 'Green': 0, 'Orange': 0, 'Amount': 0},
                         'Split Wager 1': {'White': test_wager, 'Pink': 0, 'Red': test_wager * 2, 'Green': 0,
                                           'Orange': 0, 'Amount': 11},
                         'Split Wager 2': {'White': 0, 'Pink': 0, 'Red': 0, 'Green': 0, 'Orange': 0, 'Amount': 0},
                         'Split Wager 3': {'White': 0, 'Pink': 0, 'Red': 0, 'Green': 0, 'Orange': 0, 'Amount': 0}}

        #testing the double_wager(self,move, split_wager_number=0, new_split_wager_number=1) method
        result_wagers, result_chips_left = player.double_wager('Split', 0, 2)
        self.assertEqual(result_wagers, {'Main Wager': {'White': 1, 'Pink': 0, 'Red': 1, 'Green': 0, 'Orange': 0,
                                        'Amount': 6},
                         'Insurance': {'White': 0, 'Pink': 0, 'Red': 0, 'Green': 0, 'Orange': 0, 'Amount': 0},
                         'Split Wager 1': {'White': 1, 'Pink': 0, 'Red': 2, 'Green': 0, 'Orange': 0,
                                           'Amount': 11},
                         'Split Wager 2': {'White': 1, 'Pink': 0, 'Red': 1, 'Green': 0, 'Orange': 0, 'Amount': 6},
                         'Split Wager 3': {'White': 0, 'Pink': 0, 'Red': 0, 'Green': 0, 'Orange': 0, 'Amount': 0}})
        self.assertEqual(result_chips_left, {'White': 4, 'Pink': 0, 'Red': 2, 'Green': 0, 'Orange': 0, 'Amount': 14})

    def test_double_wager_4red_2_second_split(self):
        """
        testing splitting Split Wager 1 with 4 Red chips in HumanPlayer's chip pile, 1 White and 1 Red in
         HumanPlayer's wager, and 1 White and 2 Red in HumanPlayer's Split Wager 1
        """
        player = HumanPlayer('Masha')
        test_chips = 4
        test_wager = 1
        test_total = 20
        player.chips = {'White': 0, 'Pink': 0, 'Red': test_chips, 'Green': 0, 'Orange': 0, 'Amount': test_total}
        player.wagers = {'Main Wager': {'White': test_wager, 'Pink': 0, 'Red': test_wager, 'Green': 0, 'Orange': 0,
                                        'Amount': 6},
                         'Insurance': {'White': 0, 'Pink': 0, 'Red': 0, 'Green': 0, 'Orange': 0, 'Amount': 0},
                         'Split Wager 1': {'White': test_wager, 'Pink': 0, 'Red': test_wager * 2, 'Green': 0,
                                           'Orange': 0, 'Amount': 11},
                         'Split Wager 2': {'White': 0, 'Pink': 0, 'Red': 0, 'Green': 0, 'Orange': 0, 'Amount': 0},
                         'Split Wager 3': {'White': 0, 'Pink': 0, 'Red': 0, 'Green': 0, 'Orange': 0, 'Amount': 0}}

        #testing the double_wager(self,move, split_wager_number=0, new_split_wager_number=1) method
        result_wagers, result_chips_left = player.double_wager('Split', 1, 2)
        self.assertEqual(result_wagers, {'Main Wager': {'White': 1, 'Pink': 0, 'Red': 1, 'Green': 0, 'Orange': 0,
                                        'Amount': 6},
                         'Insurance': {'White': 0, 'Pink': 0, 'Red': 0, 'Green': 0, 'Orange': 0, 'Amount': 0},
                         'Split Wager 1': {'White': 1, 'Pink': 0, 'Red': 2, 'Green': 0, 'Orange': 0,
                                           'Amount': 11},
                         'Split Wager 2': {'White': 1, 'Pink': 0, 'Red': 2, 'Green': 0, 'Orange': 0, 'Amount': 11},
                         'Split Wager 3': {'White': 0, 'Pink': 0, 'Red': 0, 'Green': 0, 'Orange': 0, 'Amount': 0}})
        self.assertEqual(result_chips_left, {'White': 4, 'Pink': 0, 'Red': 1, 'Green': 0, 'Orange': 0, 'Amount': 9})

    def test_double_wager_4red_2_third_split(self):
        """
        testing splitting Split Wager 2 with 4 Red chips in HumanPlayer's chip pile, 1 White and 1 Red in
         HumanPlayer's wager, 1 White and 1 Red in HumanPlayer's Split Wager 1, and 1 White and 2 Red in HumanPlayer's
        Split Wager 2
        """
        player = HumanPlayer('Masha')
        test_chips = 4
        test_wager = 1
        test_total = 20
        player.chips = {'White': 0, 'Pink': 0, 'Red': test_chips, 'Green': 0, 'Orange': 0, 'Amount': test_total}
        player.wagers = {'Main Wager': {'White': test_wager, 'Pink': 0, 'Red': test_wager, 'Green': 0, 'Orange': 0,
                                        'Amount': 6},
                         'Insurance': {'White': 0, 'Pink': 0, 'Red': 0, 'Green': 0, 'Orange': 0, 'Amount': 0},
                         'Split Wager 1': {'White': test_wager, 'Pink': 0, 'Red': test_wager, 'Green': 0,
                                           'Orange': 0, 'Amount': 6},
                         'Split Wager 2': {'White': test_wager, 'Pink': 0, 'Red': test_wager * 2, 'Green': 0,
                                           'Orange': 0, 'Amount': 11},
                         'Split Wager 3': {'White': 0, 'Pink': 0, 'Red': 0, 'Green': 0, 'Orange': 0, 'Amount': 0}}

        #testing the double_wager(self,move, split_wager_number=0, new_split_wager_number=1) method
        result_wagers, result_chips_left = player.double_wager('Split', 2, 3)
        self.assertEqual(result_wagers, {'Main Wager': {'White': 1, 'Pink': 0, 'Red': 1, 'Green': 0, 'Orange': 0,
                                        'Amount': 6},
                         'Insurance': {'White': 0, 'Pink': 0, 'Red': 0, 'Green': 0, 'Orange': 0, 'Amount': 0},
                         'Split Wager 1': {'White': test_wager, 'Pink': 0, 'Red': test_wager, 'Green': 0,
                                           'Orange': 0, 'Amount': 6},
                         'Split Wager 2': {'White': 1, 'Pink': 0, 'Red': 2, 'Green': 0, 'Orange': 0, 'Amount': 11},
                         'Split Wager 3': {'White': 1, 'Pink': 0, 'Red': 2, 'Green': 0, 'Orange': 0, 'Amount': 11}})
        self.assertEqual(result_chips_left, {'White': 4, 'Pink': 0, 'Red': 1, 'Green': 0, 'Orange': 0, 'Amount': 9})


if __name__ == '__main__':
    unittest.main()

