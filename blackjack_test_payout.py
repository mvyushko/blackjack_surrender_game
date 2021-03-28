"""
Testing player.add_winnings(self, payout, bet) method from blackjack_with_chips with Unittest library
"""
import unittest
from blackjack_with_chips import HumanPlayer

class TestCases(unittest.TestCase):

    def test_payout_blackjack_1_1(self):
        """
        testing the Blackjack payout with 1 White and 1 pink chips in HumanPlayer's chip pile and 1 White and 1 Red in
         HumanPlayer's wager
        """
        player = HumanPlayer('Masha')
        test_chips = 1
        test_wager = 1
        test_total = 3.5
        player.chips = {'White': test_chips, 'Pink': test_chips, 'Red': 0, 'Green': 0, 'Orange': 0}
        player.wager = {'White': test_wager, 'Pink': 0, 'Red': test_wager, 'Green': 0, 'Orange': 0}
        player.wager_amount = 6
        #wager amount: 6
        player.chips_total = test_total

        #testing the add_winnings() method (adding the won chips to Player's chip pile and the wager amount to Player's
        # total)
        result_total, result_chips = player.add_winnings('3:2', 'Main Wager')
        result_wager = player.wager
        self.assertEqual(result_total, 18.5)
        self.assertEqual(result_chips, {'White': 6, 'Pink': 1, 'Red': 2, 'Green': 0, 'Orange': 0})
        self.assertEqual(result_wager, {'White': 1, 'Pink': 0, 'Red': 1, 'Green': 0, 'Orange': 0})

        #testing the clear_wager() method (sets the wager amount and number of chips in the wager to zero
        # after a finished hand)
        player.clear_wager()
        result_clr_wager = player.wager
        result_clr_wager_amount = player.wager_amount
        self.assertEqual(result_clr_wager_amount, 0)
        self.assertEqual(result_clr_wager, {'White': 0, 'Pink': 0, 'Red': 0, 'Green': 0, 'Orange': 0})

    def test_payout_blackjack_1_2(self):
        """
        Testing the Blackjack payout with 1 White and 1 pink chips in HumanPlayer's chip pile and 2 White and 2 Red in
        HumanPlayer's wager
        """
        player = HumanPlayer('Masha')
        test_chips = 1
        test_wager = 2
        test_total = 3.5
        player.chips = {'White': test_chips, 'Pink': test_chips, 'Red': 0, 'Green': 0, 'Orange': 0}
        player.wager = {'White': test_wager, 'Pink': 0, 'Red': test_wager, 'Green': 0, 'Orange': 0}
        player.wager_amount = 12
        #wager amount: 12
        player.chips_total = test_total

        #testing the add_winnings() method (adding the won chips to Player's chip pile and the wager amount to Player's
        # total)
        result_total, result_chips = player.add_winnings('3:2', 'Main Wager')
        result_wager = player.wager
        self.assertEqual(result_total, 33.5)
        self.assertEqual(result_chips, {'White': 6, 'Pink': 1, 'Red': 5, 'Green': 0, 'Orange': 0})
        self.assertEqual(result_wager, {'White': 2, 'Pink': 0, 'Red': 2, 'Green': 0, 'Orange': 0})

    def test_payout_normal_1_1(self):
        """
        testing the 1:1 payout with 1 White and 1 pink chips in HumanPlayer's chip pile and 1 White and 1 Red in
         HumanPlayer's wager
        """
        player = HumanPlayer('Masha')
        test_chips = 1
        test_wager = 1
        test_total = 3.5
        player.chips = {'White': test_chips, 'Pink': test_chips, 'Red': 0, 'Green': 0, 'Orange': 0}
        player.wager = {'White': test_wager, 'Pink': 0, 'Red': test_wager, 'Green': 0, 'Orange': 0}
        player.wager_amount = 6
        # wager amount: 6
        player.chips_total = test_total

        #testing the add_winnings() method (adding the won chips to Player's chip pile and the wager amount to Player's
        # total)
        result_total, result_chips = player.add_winnings('1:1', 'Main Wager')
        result_wager = player.wager
        self.assertEqual(result_total, 15.5)
        self.assertEqual(result_chips, {'White': 3, 'Pink': 1, 'Red': 2, 'Green': 0, 'Orange': 0})
        self.assertEqual(result_wager, {'White': 1, 'Pink': 0, 'Red': 1, 'Green': 0, 'Orange': 0})

        # testing the clear_wager() method (sets the wager amount and number of chips in the wager to zero
        # after a finished hand)
        player.clear_wager()
        result_clr_wager = player.wager
        result_clr_wager_amount = player.wager_amount
        self.assertEqual(result_clr_wager_amount, 0)
        self.assertEqual(result_clr_wager, {'White': 0, 'Pink': 0, 'Red': 0, 'Green': 0, 'Orange': 0})

    def test_payout_normal_1_2(self):
        """
        Testing the 1:1 payout with 1 White and 1 pink chips in HumanPlayer's chip pile and 2 White and 2 Red in
        HumanPlayer's wager
        """
        player = HumanPlayer('Masha')
        test_chips = 1
        test_wager = 2
        test_total = 3.5
        player.chips = {'White': test_chips, 'Pink': test_chips, 'Red': 0, 'Green': 0, 'Orange': 0}
        player.wager = {'White': test_wager, 'Pink': 0, 'Red': test_wager, 'Green': 0, 'Orange': 0}
        player.wager_amount = 12
        # wager amount: 12
        player.chips_total = test_total

        #testing the add_winnings() method (adding the won chips to Player's chip pile and the wager amount to Player's
        # total)
        result_total, result_chips = player.add_winnings('1:1', 'Main Wager')
        result_wager = player.wager
        self.assertEqual(result_total, 27.5)
        self.assertEqual(result_chips, {'White': 5, 'Pink': 1, 'Red': 4, 'Green': 0, 'Orange': 0})
        self.assertEqual(result_wager, {'White': 2, 'Pink': 0, 'Red': 2, 'Green': 0, 'Orange': 0})

    def test_payout_tie_1_1(self):
        """
        testing the tie payout with 1 White and 1 pink chips in HumanPlayer's chip pile and 1 White and 1 Red in
         HumanPlayer's wager
        """
        player = HumanPlayer('Masha')
        test_chips = 1
        test_wager = 1
        test_total = 3.5
        player.chips = {'White': test_chips, 'Pink': test_chips, 'Red': 0, 'Green': 0, 'Orange': 0}
        player.wager = {'White': test_wager, 'Pink': 0, 'Red': test_wager, 'Green': 0, 'Orange': 0}
        player.wager_amount = 6
        # wager amount: 6
        player.chips_total = test_total

        #testing the add_winnings() method (adding the won chips to Player's chip pile and the wager amount to Player's
        # total)
        result_total, result_chips = player.add_winnings('Tie', 'Main Wager')
        result_wager = player.wager
        self.assertEqual(result_total, 9.5)
        self.assertEqual(result_chips, {'White': 2, 'Pink': 1, 'Red': 1, 'Green': 0, 'Orange': 0})
        self.assertEqual(result_wager, {'White': 1, 'Pink': 0, 'Red': 1, 'Green': 0, 'Orange': 0})

        # testing the clear_wager() method (sets the wager amount and number of chips in the wager to zero
        # after a finished hand)
        player.clear_wager()
        result_clr_wager = player.wager
        result_clr_wager_amount = player.wager_amount
        self.assertEqual(result_clr_wager_amount, 0)
        self.assertEqual(result_clr_wager, {'White': 0, 'Pink': 0, 'Red': 0, 'Green': 0, 'Orange': 0})

    def test_payout_tie_1_2(self):
        """
        Testing the tie payout with 1 White and 1 pink chips in HumanPlayer's chip pile and 2 White and 2 Red in
        HumanPlayer's wager
        """
        player = HumanPlayer('Masha')
        test_chips = 1
        test_wager = 2
        test_total = 3.5
        player.chips = {'White': test_chips, 'Pink': test_chips, 'Red': 0, 'Green': 0, 'Orange': 0}
        player.wager = {'White': test_wager, 'Pink': 0, 'Red': test_wager, 'Green': 0, 'Orange': 0}
        player.wager_amount = 12
        # wager amount: 12
        player.chips_total = test_total

        #testing the add_winnings() method (adding the won chips to Player's chip pile and the wager amount to Player's
        # total)
        result_total, result_chips = player.add_winnings('Tie', 'Main Wager')
        result_wager = player.wager
        self.assertEqual(result_total, 15.5)
        self.assertEqual(result_chips, {'White': 3, 'Pink': 1, 'Red': 2, 'Green': 0, 'Orange': 0})
        self.assertEqual(result_wager, {'White': 2, 'Pink': 0, 'Red': 2, 'Green': 0, 'Orange': 0})

    def test_payout_insurance_1_1(self):
        """
        testing the 2:1 payout with 1 White and 1 pink chips in HumanPlayer's chip pile and 1 White and 1 Red in
         HumanPlayer's wager
        """
        player = HumanPlayer('Masha')
        test_chips = 1
        test_wager = 1
        test_total = 3.5
        player.chips = {'White': test_chips, 'Pink': test_chips, 'Red': 0, 'Green': 0, 'Orange': 0}
        player.insurance = {'White': test_wager, 'Pink': 0, 'Red': test_wager, 'Green': 0, 'Orange': 0}
        player.insurance_amount = 6
        # wager amount: 6
        player.chips_total = test_total

        #testing the add_winnings() method (adding the won chips to Player's chip pile and the wager amount to Player's
        # total)
        result_total, result_chips = player.add_winnings('2:1', 'Insurance')
        result_wager = player.insurance
        self.assertEqual(result_total, 21.5)
        self.assertEqual(result_chips, {'White': 4, 'Pink': 1, 'Red': 3, 'Green': 0, 'Orange': 0})
        self.assertEqual(result_wager, {'White': 1, 'Pink': 0, 'Red': 1, 'Green': 0, 'Orange': 0})

        # testing the clear_wager() method (sets the wager amount and number of chips in the wager to zero
        # after a finished hand)
        player.clear_wager()
        result_clr_wager = player.insurance
        result_clr_wager_amount = player.insurance_amount
        self.assertEqual(result_clr_wager_amount, 0)
        self.assertEqual(result_clr_wager, {'White': 0, 'Pink': 0, 'Red': 0, 'Green': 0, 'Orange': 0})

    def test_payout_insurance_1_2(self):
        """
        Testing the 2:1 payout with 1 White and 1 pink chips in HumanPlayer's chip pile and 2 White and 2 Red in
        HumanPlayer's wager
        """
        player = HumanPlayer('Masha')
        test_chips = 1
        test_wager = 2
        test_total = 3.5
        player.chips = {'White': test_chips, 'Pink': test_chips, 'Red': 0, 'Green': 0, 'Orange': 0}
        player.insurance = {'White': test_wager, 'Pink': 0, 'Red': test_wager, 'Green': 0, 'Orange': 0}
        player.insurance_amount = 12
        # wager amount: 12
        player.chips_total = test_total

        #testing the add_winnings() method (adding the won chips to Player's chip pile and the wager amount to Player's
        # total)
        result_total, result_chips = player.add_winnings('2:1', 'Insurance')
        result_wager = player.insurance
        self.assertEqual(result_total, 39.5)
        self.assertEqual(result_chips, {'White': 7, 'Pink': 1, 'Red': 6, 'Green': 0, 'Orange': 0})
        self.assertEqual(result_wager, {'White': 2, 'Pink': 0, 'Red': 2, 'Green': 0, 'Orange': 0})


    def test_payout_blackjack_1_1_split(self):
        """
        testing the Blackjack payout with 1 White and 1 pink chips in HumanPlayer's chip pile and 1 White and 1 Red in
         HumanPlayer's Split wager
        """
        player = HumanPlayer('Masha')
        test_chips = 1
        test_wager = 1
        test_total = 3.5
        player.chips = {'White': test_chips, 'Pink': test_chips, 'Red': 0, 'Green': 0, 'Orange': 0}
        player.split_wager = {'White': test_wager, 'Pink': 0, 'Red': test_wager, 'Green': 0, 'Orange': 0}
        player.split_wager_amount = 6
        #wager amount: 6
        player.chips_total = test_total

        #testing the add_winnings() method (adding the won chips to Player's chip pile and the wager amount to Player's
        # total)
        result_total, result_chips = player.add_winnings('3:2', 'Split Wager')
        result_wager = player.split_wager
        self.assertEqual(result_total, 18.5)
        self.assertEqual(result_chips, {'White': 6, 'Pink': 1, 'Red': 2, 'Green': 0, 'Orange': 0})
        self.assertEqual(result_wager, {'White': 1, 'Pink': 0, 'Red': 1, 'Green': 0, 'Orange': 0})

        #testing the clear_wager() method (sets the wager amount and number of chips in the wager to zero
        # after a finished hand)
        player.clear_wager()
        result_clr_wager = player.split_wager
        result_clr_wager_amount = player.split_wager_amount
        self.assertEqual(result_clr_wager_amount, 0)
        self.assertEqual(result_clr_wager, {'White': 0, 'Pink': 0, 'Red': 0, 'Green': 0, 'Orange': 0})

    def test_payout_blackjack_1_2_split(self):
        """
        Testing the Blackjack payout with 1 White and 1 pink chips in HumanPlayer's chip pile and 2 White and 2 Red in
        HumanPlayer's Split wager
        """
        player = HumanPlayer('Masha')
        test_chips = 1
        test_wager = 2
        test_total = 3.5
        player.chips = {'White': test_chips, 'Pink': test_chips, 'Red': 0, 'Green': 0, 'Orange': 0}
        player.split_wager = {'White': test_wager, 'Pink': 0, 'Red': test_wager, 'Green': 0, 'Orange': 0}
        player.split_wager_amount = 12
        #wager amount: 12
        player.chips_total = test_total

        #testing the add_winnings() method (adding the won chips to Player's chip pile and the wager amount to Player's
        # total)
        result_total, result_chips = player.add_winnings('3:2', 'Split Wager')
        result_wager = player.split_wager
        self.assertEqual(result_total, 33.5)
        self.assertEqual(result_chips, {'White': 6, 'Pink': 1, 'Red': 5, 'Green': 0, 'Orange': 0})
        self.assertEqual(result_wager, {'White': 2, 'Pink': 0, 'Red': 2, 'Green': 0, 'Orange': 0})

    def test_payout_normal_1_1_split(self):
        """
        testing the 1:1 payout with 1 White and 1 pink chips in HumanPlayer's chip pile and 1 White and 1 Red in
         HumanPlayer's Split wager
        """
        player = HumanPlayer('Masha')
        test_chips = 1
        test_wager = 1
        test_total = 3.5
        player.chips = {'White': test_chips, 'Pink': test_chips, 'Red': 0, 'Green': 0, 'Orange': 0}
        player.split_wager = {'White': test_wager, 'Pink': 0, 'Red': test_wager, 'Green': 0, 'Orange': 0}
        player.split_wager_amount = 6
        # wager amount: 6
        player.chips_total = test_total

        #testing the add_winnings() method (adding the won chips to Player's chip pile and the wager amount to Player's
        # total)
        result_total, result_chips = player.add_winnings('1:1', 'Split Wager')
        result_wager = player.split_wager
        self.assertEqual(result_total, 15.5)
        self.assertEqual(result_chips, {'White': 3, 'Pink': 1, 'Red': 2, 'Green': 0, 'Orange': 0})
        self.assertEqual(result_wager, {'White': 1, 'Pink': 0, 'Red': 1, 'Green': 0, 'Orange': 0})

        # testing the clear_wager() method (sets the wager amount and number of chips in the wager to zero
        # after a finished hand)
        player.clear_wager()
        result_clr_wager = player.split_wager
        result_clr_wager_amount = player.split_wager_amount
        self.assertEqual(result_clr_wager_amount, 0)
        self.assertEqual(result_clr_wager, {'White': 0, 'Pink': 0, 'Red': 0, 'Green': 0, 'Orange': 0})

    def test_payout_normal_1_2_split(self):
        """
        Testing the 1:1 payout with 1 White and 1 pink chips in HumanPlayer's chip pile and 2 White and 2 Red in
        HumanPlayer's Split wager
        """
        player = HumanPlayer('Masha')
        test_chips = 1
        test_wager = 2
        test_total = 3.5
        player.chips = {'White': test_chips, 'Pink': test_chips, 'Red': 0, 'Green': 0, 'Orange': 0}
        player.split_wager = {'White': test_wager, 'Pink': 0, 'Red': test_wager, 'Green': 0, 'Orange': 0}
        player.split_wager_amount = 12
        # wager amount: 12
        player.chips_total = test_total

        #testing the add_winnings() method (adding the won chips to Player's chip pile and the wager amount to Player's
        # total)
        result_total, result_chips = player.add_winnings('1:1', 'Split Wager')
        result_wager = player.split_wager
        self.assertEqual(result_total, 27.5)
        self.assertEqual(result_chips, {'White': 5, 'Pink': 1, 'Red': 4, 'Green': 0, 'Orange': 0})
        self.assertEqual(result_wager, {'White': 2, 'Pink': 0, 'Red': 2, 'Green': 0, 'Orange': 0})

    def test_payout_tie_1_1_split(self):
        """
        testing the tie payout with 1 White and 1 pink chips in HumanPlayer's chip pile and 1 White and 1 Red in
         HumanPlayer's Split wager
        """
        player = HumanPlayer('Masha')
        test_chips = 1
        test_wager = 1
        test_total = 3.5
        player.chips = {'White': test_chips, 'Pink': test_chips, 'Red': 0, 'Green': 0, 'Orange': 0}
        player.split_wager = {'White': test_wager, 'Pink': 0, 'Red': test_wager, 'Green': 0, 'Orange': 0}
        player.split_wager_amount = 6
        # wager amount: 6
        player.chips_total = test_total

        #testing the add_winnings() method (adding the won chips to Player's chip pile and the wager amount to Player's
        # total)
        result_total, result_chips = player.add_winnings('Tie', 'Split Wager')
        result_wager = player.split_wager
        self.assertEqual(result_total, 9.5)
        self.assertEqual(result_chips, {'White': 2, 'Pink': 1, 'Red': 1, 'Green': 0, 'Orange': 0})
        self.assertEqual(result_wager, {'White': 1, 'Pink': 0, 'Red': 1, 'Green': 0, 'Orange': 0})

        # testing the clear_wager() method (sets the wager amount and number of chips in the wager to zero
        # after a finished hand)
        player.clear_wager()
        result_clr_wager = player.split_wager
        result_clr_wager_amount = player.split_wager_amount
        self.assertEqual(result_clr_wager_amount, 0)
        self.assertEqual(result_clr_wager, {'White': 0, 'Pink': 0, 'Red': 0, 'Green': 0, 'Orange': 0})

    def test_payout_tie_1_2_split(self):
        """
        Testing the tie payout with 1 White and 1 pink chips in HumanPlayer's chip pile and 2 White and 2 Red in
        HumanPlayer's Split wager
        """
        player = HumanPlayer('Masha')
        test_chips = 1
        test_wager = 2
        test_total = 3.5
        player.chips = {'White': test_chips, 'Pink': test_chips, 'Red': 0, 'Green': 0, 'Orange': 0}
        player.split_wager = {'White': test_wager, 'Pink': 0, 'Red': test_wager, 'Green': 0, 'Orange': 0}
        player.split_wager_amount = 12
        # wager amount: 12
        player.chips_total = test_total

        #testing the add_winnings() method (adding the won chips to Player's chip pile and the wager amount to Player's
        # total)
        result_total, result_chips = player.add_winnings('Tie', 'Split Wager')
        result_wager = player.split_wager
        self.assertEqual(result_total, 15.5)
        self.assertEqual(result_chips, {'White': 3, 'Pink': 1, 'Red': 2, 'Green': 0, 'Orange': 0})
        self.assertEqual(result_wager, {'White': 2, 'Pink': 0, 'Red': 2, 'Green': 0, 'Orange': 0})


if __name__ == '__main__':
    unittest.main()

