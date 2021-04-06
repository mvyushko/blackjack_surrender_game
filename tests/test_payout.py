"""
Testing player.add_winnings(self, payout, bet) method from blackjack_with_chips with Unittest library
"""
import unittest
from player_classes import HumanPlayer

class TestPayout(unittest.TestCase):

    def test_payout_blackjack_1_1(self):
        """
        testing the Blackjack payout with 1 White and 1 pink chips in HumanPlayer's chip pile and 1 White and 1 Red in
         HumanPlayer's wager
        """
        player = HumanPlayer('Masha')
        test_chips = 1
        test_wager = 1
        test_total = 3.5
        test_wager_amount = 6
        player.chips = {'White': test_chips, 'Pink': test_chips, 'Red': 0, 'Green': 0, 'Orange': 0,
                        'Amount': test_total}
        player.wagers = {'Main Wager': {'White': test_wager, 'Pink': 0, 'Red': test_wager, 'Green': 0, 'Orange': 0,
                                        'Amount': test_wager_amount},
                 'Insurance': {'White': 0, 'Pink':0, 'Red': 0, 'Green': 0, 'Orange': 0, 'Amount': 0},
                 'Split Wager 1': {'White': 0, 'Pink':0, 'Red': 0, 'Green': 0, 'Orange': 0, 'Amount': 0},
                 'Split Wager 2': {'White': 0, 'Pink':0, 'Red': 0, 'Green': 0, 'Orange': 0, 'Amount': 0},
                 'Split Wager 3': {'White': 0, 'Pink':0, 'Red': 0, 'Green': 0, 'Orange': 0, 'Amount': 0}}

        #testing the add_winnings(self, payout, bet) method (adding the won chips to HumanPlayer's chips)
        player.add_winnings('3:2', 'Main Wager')
        result_chips = player.chips
        result_wager = player.wagers['Main Wager']
        self.assertEqual(result_chips, {'White': 6, 'Pink': 1, 'Red': 2, 'Green': 0, 'Orange': 0, 'Amount': 18.5})
        self.assertEqual(result_wager, {'White': 1, 'Pink': 0, 'Red': 1, 'Green': 0, 'Orange': 0, 'Amount': 6})

        #testing the clear_wager() method (sets the wager amount and number of chips in the wager to zero
        # after a finished hand)
        player.clear_wager()
        result_clr_wager = player.wagers['Main Wager']
        self.assertEqual(result_clr_wager, {'White': 0, 'Pink': 0, 'Red': 0, 'Green': 0, 'Orange': 0, 'Amount': 0})

    def test_payout_blackjack_1_2(self):
        """
        Testing the Blackjack payout with 1 White and 1 pink chips in HumanPlayer's chip pile and 2 White and 2 Red in
        HumanPlayer's wager
        """
        player = HumanPlayer('Masha')
        test_chips = 1
        test_wager = 2
        test_total = 3.5
        test_wager_amount = 6
        player.chips = {'White': test_chips, 'Pink': test_chips, 'Red': 0, 'Green': 0, 'Orange': 0,
                        'Amount': test_total}
        player.wagers = {'Main Wager': {'White': test_wager, 'Pink': 0, 'Red': test_wager, 'Green': 0, 'Orange': 0,
                                        'Amount': test_wager_amount * 2},
                 'Insurance': {'White': 0, 'Pink':0, 'Red': 0, 'Green': 0, 'Orange': 0, 'Amount': 0},
                 'Split Wager 1': {'White': 0, 'Pink':0, 'Red': 0, 'Green': 0, 'Orange': 0, 'Amount': 0},
                 'Split Wager 2': {'White': 0, 'Pink':0, 'Red': 0, 'Green': 0, 'Orange': 0, 'Amount': 0},
                 'Split Wager 3': {'White': 0, 'Pink':0, 'Red': 0, 'Green': 0, 'Orange': 0, 'Amount': 0}}

        # testing the add_winnings(self, payout, bet) method (adding the won chips to HumanPlayer's chips)
        player.add_winnings('3:2', 'Main Wager')
        result_chips = player.chips
        result_wager = player.wagers['Main Wager']
        self.assertEqual(result_chips, {'White': 6, 'Pink': 1, 'Red': 5, 'Green': 0, 'Orange': 0, 'Amount': 33.5})
        self.assertEqual(result_wager, {'White': 2, 'Pink': 0, 'Red': 2, 'Green': 0, 'Orange': 0, 'Amount': 12})

    def test_payout_normal_1_1(self):
        """
        testing the 1:1 payout with 1 White and 1 pink chips in HumanPlayer's chip pile and 1 White and 1 Red in
         HumanPlayer's wager
        """
        player = HumanPlayer('Masha')
        test_chips = 1
        test_wager = 1
        test_total = 3.5
        test_wager_amount = 6
        player.chips = {'White': test_chips, 'Pink': test_chips, 'Red': 0, 'Green': 0, 'Orange': 0,
                        'Amount': test_total}
        player.wagers = {'Main Wager': {'White': test_wager, 'Pink': 0, 'Red': test_wager, 'Green': 0, 'Orange': 0,
                                        'Amount': test_wager_amount},
                         'Insurance': {'White': 0, 'Pink': 0, 'Red': 0, 'Green': 0, 'Orange': 0, 'Amount': 0},
                         'Split Wager 1': {'White': 0, 'Pink': 0, 'Red': 0, 'Green': 0, 'Orange': 0, 'Amount': 0},
                         'Split Wager 2': {'White': 0, 'Pink': 0, 'Red': 0, 'Green': 0, 'Orange': 0, 'Amount': 0},
                         'Split Wager 3': {'White': 0, 'Pink': 0, 'Red': 0, 'Green': 0, 'Orange': 0, 'Amount': 0}}

        # testing the add_winnings(self, payout, bet) method (adding the won chips to HumanPlayer's chips):
        player.add_winnings('1:1', 'Main Wager')
        result_chips = player.chips
        result_wager = player.wagers['Main Wager']
        self.assertEqual(result_chips, {'White': 3, 'Pink': 1, 'Red': 2, 'Green': 0, 'Orange': 0, 'Amount': 15.5})
        self.assertEqual(result_wager, {'White': 1, 'Pink': 0, 'Red': 1, 'Green': 0, 'Orange': 0, 'Amount': 6})

        # testing the clear_wager() method (sets the wager amount and number of chips in the wager to zero
        # after a finished hand):
        player.clear_wager()
        result_clr_wager = player.wagers['Main Wager']
        self.assertEqual(result_clr_wager, {'White': 0, 'Pink': 0, 'Red': 0, 'Green': 0, 'Orange': 0, 'Amount': 0})

    def test_payout_normal_1_2(self):
        """
        Testing the 1:1 payout with 1 White and 1 pink chips in HumanPlayer's chip pile and 2 White and 2 Red in
        HumanPlayer's wager
        """
        player = HumanPlayer('Masha')
        test_chips = 1
        test_wager = 2
        test_total = 3.5
        test_wager_amount = 6
        player.chips = {'White': test_chips, 'Pink': test_chips, 'Red': 0, 'Green': 0, 'Orange': 0,
                        'Amount': test_total}
        player.wagers = {'Main Wager': {'White': test_wager, 'Pink': 0, 'Red': test_wager, 'Green': 0, 'Orange': 0,
                                        'Amount': test_wager_amount * 2},
                         'Insurance': {'White': 0, 'Pink': 0, 'Red': 0, 'Green': 0, 'Orange': 0, 'Amount': 0},
                         'Split Wager 1': {'White': 0, 'Pink': 0, 'Red': 0, 'Green': 0, 'Orange': 0, 'Amount': 0},
                         'Split Wager 2': {'White': 0, 'Pink': 0, 'Red': 0, 'Green': 0, 'Orange': 0, 'Amount': 0},
                         'Split Wager 3': {'White': 0, 'Pink': 0, 'Red': 0, 'Green': 0, 'Orange': 0, 'Amount': 0}}

        # testing the add_winnings(self, payout, bet) method (adding the won chips to HumanPlayer's chips):
        player.add_winnings('1:1', 'Main Wager')
        result_chips = player.chips
        result_wager = player.wagers['Main Wager']
        self.assertEqual(result_chips, {'White': 5, 'Pink': 1, 'Red': 4, 'Green': 0, 'Orange': 0, 'Amount': 27.5})
        self.assertEqual(result_wager, {'White': 2, 'Pink': 0, 'Red': 2, 'Green': 0, 'Orange': 0, 'Amount': 12})

    def test_payout_push_1_1(self):
        """
        testing the push payout with 1 White and 1 pink chips in HumanPlayer's chip pile and 1 White and 1 Red in
         HumanPlayer's wager
        """
        player = HumanPlayer('Masha')
        test_chips = 1
        test_wager = 1
        test_total = 3.5
        test_wager_amount = 6
        player.chips = {'White': test_chips, 'Pink': test_chips, 'Red': 0, 'Green': 0, 'Orange': 0,
                        'Amount': test_total}
        player.wagers = {'Main Wager': {'White': test_wager, 'Pink': 0, 'Red': test_wager, 'Green': 0, 'Orange': 0,
                                        'Amount': test_wager_amount},
                         'Insurance': {'White': 0, 'Pink': 0, 'Red': 0, 'Green': 0, 'Orange': 0, 'Amount': 0},
                         'Split Wager 1': {'White': 0, 'Pink': 0, 'Red': 0, 'Green': 0, 'Orange': 0, 'Amount': 0},
                         'Split Wager 2': {'White': 0, 'Pink': 0, 'Red': 0, 'Green': 0, 'Orange': 0, 'Amount': 0},
                         'Split Wager 3': {'White': 0, 'Pink': 0, 'Red': 0, 'Green': 0, 'Orange': 0, 'Amount': 0}}

        # testing the add_winnings(self, payout, bet) method (adding the won chips to HumanPlayer's chips):
        player.add_winnings('Push', 'Main Wager')
        result_chips = player.chips
        result_wager = player.wagers['Main Wager']
        self.assertEqual(result_chips, {'White': 2, 'Pink': 1, 'Red': 1, 'Green': 0, 'Orange': 0, 'Amount': 9.5})
        self.assertEqual(result_wager, {'White': 1, 'Pink': 0, 'Red': 1, 'Green': 0, 'Orange': 0, 'Amount': 6})

        # testing the clear_wager() method (sets the wager amount and number of chips in the wager to zero
        # after a finished hand):
        player.clear_wager()
        result_clr_wager = player.wagers['Main Wager']
        self.assertEqual(result_clr_wager, {'White': 0, 'Pink': 0, 'Red': 0, 'Green': 0, 'Orange': 0, 'Amount': 0})

    def test_payout_push_1_2(self):
        """
        Testing the push payout with 1 White and 1 pink chips in HumanPlayer's chip pile and 2 White and 2 Red in
        HumanPlayer's wager
        """
        player = HumanPlayer('Masha')
        test_chips = 1
        test_wager = 2
        test_total = 3.5
        test_wager_amount = 6
        player.chips = {'White': test_chips, 'Pink': test_chips, 'Red': 0, 'Green': 0, 'Orange': 0,
                        'Amount': test_total}
        player.wagers = {'Main Wager': {'White': test_wager, 'Pink': 0, 'Red': test_wager, 'Green': 0, 'Orange': 0,
                                        'Amount': test_wager_amount * 2},
                         'Insurance': {'White': 0, 'Pink': 0, 'Red': 0, 'Green': 0, 'Orange': 0, 'Amount': 0},
                         'Split Wager 1': {'White': 0, 'Pink': 0, 'Red': 0, 'Green': 0, 'Orange': 0, 'Amount': 0},
                         'Split Wager 2': {'White': 0, 'Pink': 0, 'Red': 0, 'Green': 0, 'Orange': 0, 'Amount': 0},
                         'Split Wager 3': {'White': 0, 'Pink': 0, 'Red': 0, 'Green': 0, 'Orange': 0, 'Amount': 0}}

        # testing the add_winnings(self, payout, bet) method (adding the won chips to HumanPlayer's chips):
        player.add_winnings('Push', 'Main Wager')
        result_chips = player.chips
        result_wager = player.wagers['Main Wager']
        self.assertEqual(result_chips, {'White': 3, 'Pink': 1, 'Red': 2, 'Green': 0, 'Orange': 0, 'Amount': 15.5})
        self.assertEqual(result_wager, {'White': 2, 'Pink': 0, 'Red': 2, 'Green': 0, 'Orange': 0, 'Amount': 12})

    def test_payout_insurance_1_1(self):
        """
        testing the 2:1 Insurance payout with 1 White and 1 pink chips in HumanPlayer's chip pile, 1 White and 1 Red in
         HumanPlayer's wager, and 1 White and 1 Red in HumanPlayer's Insurance bet
        """
        player = HumanPlayer('Masha')
        test_chips = 1
        test_wager = 1
        test_total = 3.5
        test_wager_amount = 6
        player.chips = {'White': test_chips, 'Pink': test_chips, 'Red': 0, 'Green': 0, 'Orange': 0,
                        'Amount': test_total}
        player.wagers = {'Main Wager': {'White': test_wager, 'Pink': 0, 'Red': test_wager, 'Green': 0, 'Orange': 0,
                                        'Amount': test_wager_amount},
                         'Insurance': {'White': test_wager, 'Pink': 0, 'Red': test_wager, 'Green': 0, 'Orange': 0,
                                       'Amount' : test_wager_amount},
                         'Split Wager 1': {'White': 0, 'Pink': 0, 'Red': 0, 'Green': 0, 'Orange': 0, 'Amount': 0},
                         'Split Wager 2': {'White': 0, 'Pink': 0, 'Red': 0, 'Green': 0, 'Orange': 0, 'Amount': 0},
                         'Split Wager 3': {'White': 0, 'Pink': 0, 'Red': 0, 'Green': 0, 'Orange': 0, 'Amount': 0}}

        # testing the add_winnings(self, payout, bet) method (adding the won chips to HumanPlayer's chips):
        player.add_winnings('2:1', 'Insurance')
        result_chips = player.chips
        result_wager = player.wagers['Insurance']
        self.assertEqual(result_chips, {'White': 4, 'Pink': 1, 'Red': 3, 'Green': 0, 'Orange': 0, 'Amount': 21.5})
        self.assertEqual(result_wager, {'White': 1, 'Pink': 0, 'Red': 1, 'Green': 0, 'Orange': 0, 'Amount': 6})

        # testing the clear_wager() method (sets all wager amounts and number of chips in all wagers to zero
        # after a finished hand)
        player.clear_wager()
        result_clr_main_wager = player.wagers['Main Wager']
        result_clr_insurance = player.wagers['Insurance']
        self.assertEqual(result_clr_main_wager, {'White': 0, 'Pink': 0, 'Red': 0, 'Green': 0, 'Orange': 0, 'Amount': 0})
        self.assertEqual(result_clr_insurance, {'White': 0, 'Pink': 0, 'Red': 0, 'Green': 0, 'Orange': 0, 'Amount': 0})

    def test_payout_insurance_1_2(self):
        """
        Testing the 2:1 Insurance payout with 1 White and 1 pink chips in HumanPlayer's chip pile, 1 White and 1 Red in
        HumanPlayer's Main wager, and 2 White and 2 Red in HumanPlayer's Insurance
        """
        player = HumanPlayer('Masha')
        test_chips = 1
        test_wager = 2
        test_total = 3.5
        test_wager_amount = 6
        player.chips = {'White': test_chips, 'Pink': test_chips, 'Red': 0, 'Green': 0, 'Orange': 0,
                        'Amount': test_total}
        player.wagers = {'Main Wager': {'White': test_wager/2, 'Pink': 0, 'Red': test_wager/2, 'Green': 0, 'Orange': 0,
                                        'Amount': test_wager_amount},
                         'Insurance': {'White': test_wager, 'Pink': 0, 'Red': test_wager, 'Green': 0, 'Orange': 0,
                                       'Amount': test_wager_amount * 2},
                         'Split Wager 1': {'White': 0, 'Pink': 0, 'Red': 0, 'Green': 0, 'Orange': 0, 'Amount': 0},
                         'Split Wager 2': {'White': 0, 'Pink': 0, 'Red': 0, 'Green': 0, 'Orange': 0, 'Amount': 0},
                         'Split Wager 3': {'White': 0, 'Pink': 0, 'Red': 0, 'Green': 0, 'Orange': 0, 'Amount': 0}}

        # testing the add_winnings(self, payout, bet) method (adding the won chips to HumanPlayer's chips):
        player.add_winnings('2:1', 'Insurance')
        result_chips = player.chips
        result_wager = player.wagers['Insurance']
        self.assertEqual(result_chips, {'White': 7, 'Pink': 1, 'Red': 6, 'Green': 0, 'Orange': 0, 'Amount': 39.5})
        self.assertEqual(result_wager, {'White': 2, 'Pink': 0, 'Red': 2, 'Green': 0, 'Orange': 0, 'Amount': 12})


    def test_payout_blackjack_1_1_split(self):
        """
        testing the Blackjack payout on Split Wager 1 with 1 White and 1 pink chips in HumanPlayer's chip pile, 1 White
         and 1 Red in HumanPlayer's Main wager, and 1 White and 1 Red in HumanPlayer's Split wager 1
        """
        player = HumanPlayer('Masha')
        test_chips = 1
        test_wager = 1
        test_total = 3.5
        test_wager_amount = 6
        player.chips = {'White': test_chips, 'Pink': test_chips, 'Red': 0, 'Green': 0, 'Orange': 0,
                        'Amount': test_total}
        player.wagers = {'Main Wager': {'White': test_wager, 'Pink': 0, 'Red': test_wager, 'Green': 0, 'Orange': 0,
                                        'Amount': test_wager_amount},
                         'Insurance': {'White': 0, 'Pink': 0, 'Red': 0, 'Green': 0, 'Orange': 0, 'Amount': 0},
                         'Split Wager 1': {'White': test_wager, 'Pink': 0, 'Red': test_wager, 'Green': 0, 'Orange': 0,
                                           'Amount': test_wager_amount},
                         'Split Wager 2': {'White': 0, 'Pink': 0, 'Red': 0, 'Green': 0, 'Orange': 0, 'Amount': 0},
                         'Split Wager 3': {'White': 0, 'Pink': 0, 'Red': 0, 'Green': 0, 'Orange': 0, 'Amount': 0}}

        # testing the add_winnings(self, payout, bet) method (adding the won chips to HumanPlayer's chips):
        player.add_winnings('3:2', 'Split Wager 1')
        result_chips = player.chips
        result_wager = player.wagers['Split Wager 1']
        self.assertEqual(result_chips, {'White': 6, 'Pink': 1, 'Red': 2, 'Green': 0, 'Orange': 0, 'Amount': 18.5})
        self.assertEqual(result_wager, {'White': 1, 'Pink': 0, 'Red': 1, 'Green': 0, 'Orange': 0, 'Amount': 6})

        #testing the clear_wager() method (sets all wager amounts and number of chips in all wagers to zero
        # after a finished hand)
        player.clear_wager()
        result_clr_main_wager = player.wagers['Main Wager']
        result_clr_split1 = player.wagers['Split Wager 1']
        self.assertEqual(result_clr_main_wager, {'White': 0, 'Pink': 0, 'Red': 0, 'Green': 0, 'Orange': 0, 'Amount': 0})
        self.assertEqual(result_clr_split1, {'White': 0, 'Pink': 0, 'Red': 0, 'Green': 0, 'Orange': 0, 'Amount': 0})

    def test_payout_blackjack_1_2_split(self):
        """
        Testing the Blackjack payout on Split Wager 2 with 1 White and 1 pink chips in HumanPlayer's chip pile, 1 White
        and 1 Red in HumanPlayer's Main wager, and 2 White and 2 Red in HumanPlayer's Split wager 2
        """
        player = HumanPlayer('Masha')
        test_chips = 1
        test_wager = 2
        test_total = 3.5
        test_wager_amount = 6
        player.chips = {'White': test_chips, 'Pink': test_chips, 'Red': 0, 'Green': 0, 'Orange': 0,
                        'Amount': test_total}
        player.wagers = {'Main Wager': {'White': test_wager/2, 'Pink': 0, 'Red': test_wager/2, 'Green': 0, 'Orange': 0,
                                        'Amount': test_wager_amount},
                         'Insurance': {'White': 0, 'Pink': 0, 'Red': 0, 'Green': 0, 'Orange': 0, 'Amount': 0},
                         'Split Wager 1': {'White': 0, 'Pink': 0, 'Red': 0, 'Green': 0, 'Orange': 0, 'Amount': 0},
                         'Split Wager 2': {'White': test_wager, 'Pink': 0, 'Red': test_wager, 'Green': 0, 'Orange': 0,
                                           'Amount': test_wager_amount * 2},
                         'Split Wager 3': {'White': 0, 'Pink': 0, 'Red': 0, 'Green': 0, 'Orange': 0, 'Amount': 0}}

        # testing the add_winnings(self, payout, bet) method (adding the won chips to HumanPlayer's chips):
        player.add_winnings('3:2', 'Split Wager 2')
        result_chips = player.chips
        result_wager = player.wagers['Split Wager 2']
        self.assertEqual(result_chips, {'White': 6, 'Pink': 1, 'Red': 5, 'Green': 0, 'Orange': 0, 'Amount': 33.5})
        self.assertEqual(result_wager, {'White': 2, 'Pink': 0, 'Red': 2, 'Green': 0, 'Orange': 0, 'Amount': 12})

    def test_payout_normal_1_1_split(self):
        """
        testing the 1:1 payout on Split Wager 3 with 1 White and 1 pink chips in HumanPlayer's chip pile, 1 White and 1
        Red in HumanPlayer's Main Wager, and 1 White and 1 Red in HumanPlayer's Split wager 3
        """
        player = HumanPlayer('Masha')
        test_chips = 1
        test_wager = 1
        test_total = 3.5
        test_wager_amount = 6
        player.chips = {'White': test_chips, 'Pink': test_chips, 'Red': 0, 'Green': 0, 'Orange': 0,
                        'Amount': test_total}
        player.wagers = {'Main Wager': {'White': test_wager, 'Pink': 0, 'Red': test_wager, 'Green': 0, 'Orange': 0,
                                        'Amount': test_wager_amount},
                         'Insurance': {'White': 0, 'Pink': 0, 'Red': 0, 'Green': 0, 'Orange': 0, 'Amount': 0},
                         'Split Wager 1': {'White': 0, 'Pink': 0, 'Red': 0, 'Green': 0, 'Orange': 0, 'Amount': 0},
                         'Split Wager 2': {'White': 0, 'Pink': 0, 'Red': 0, 'Green': 0, 'Orange': 0, 'Amount': 0},
                         'Split Wager 3': {'White': test_wager, 'Pink': 0, 'Red': test_wager, 'Green': 0, 'Orange': 0,
                                           'Amount': test_wager_amount}}

        # testing the add_winnings(self, payout, bet) method (adding the won chips to HumanPlayer's chips):
        player.add_winnings('1:1', 'Split Wager 3')
        result_chips = player.chips
        result_wager = player.wagers['Split Wager 3']
        self.assertEqual(result_chips, {'White': 3, 'Pink': 1, 'Red': 2, 'Green': 0, 'Orange': 0, 'Amount': 15.5})
        self.assertEqual(result_wager, {'White': 1, 'Pink': 0, 'Red': 1, 'Green': 0, 'Orange': 0, 'Amount': 6})

        # testing the clear_wager() method (sets all wager amounts and number of chips in all wagers to zero
        # after a finished hand)
        player.clear_wager()
        result_clr_main_wager = player.wagers['Main Wager']
        result_clr_split3 = player.wagers['Split Wager 3']
        self.assertEqual(result_clr_main_wager, {'White': 0, 'Pink': 0, 'Red': 0, 'Green': 0, 'Orange': 0, 'Amount': 0})
        self.assertEqual(result_clr_split3, {'White': 0, 'Pink': 0, 'Red': 0, 'Green': 0, 'Orange': 0, 'Amount': 0})

    def test_payout_normal_1_2_split(self):
        """
        Testing the 1:1 payout on Split Wager 1 with 1 White and 1 pink chips in HumanPlayer's chip pile, 1 White and 1
        Red in HumanPlayer's Main Wager, and 2 White and 2 Red in HumanPlayer's Split wager 1
        """
        player = HumanPlayer('Masha')
        test_chips = 1
        test_wager = 2
        test_total = 3.5
        test_wager_amount = 6
        player.chips = {'White': test_chips, 'Pink': test_chips, 'Red': 0, 'Green': 0, 'Orange': 0,
                        'Amount': test_total}
        player.wagers = {'Main Wager': {'White': test_wager / 2, 'Pink': 0, 'Red': test_wager / 2, 'Green': 0,
                                        'Orange': 0, 'Amount': test_wager_amount},
            'Insurance': {'White': 0, 'Pink': 0, 'Red': 0, 'Green': 0, 'Orange': 0, 'Amount': 0},
            'Split Wager 1': {'White': test_wager, 'Pink': 0, 'Red': test_wager, 'Green': 0, 'Orange': 0,
                              'Amount': test_wager_amount * 2},
            'Split Wager 2': {'White': 0, 'Pink': 0, 'Red': 0, 'Green': 0, 'Orange': 0, 'Amount': 0},
            'Split Wager 3': {'White': 0, 'Pink': 0, 'Red': 0, 'Green': 0, 'Orange': 0, 'Amount': 0}}

        # testing the add_winnings(self, payout, bet) method (adding the won chips to HumanPlayer's chips):
        player.add_winnings('1:1', 'Split Wager 1')
        result_chips = player.chips
        result_wager = player.wagers['Split Wager 1']
        self.assertEqual(result_chips, {'White': 5, 'Pink': 1, 'Red': 4, 'Green': 0, 'Orange': 0, 'Amount': 27.5})
        self.assertEqual(result_wager, {'White': 2, 'Pink': 0, 'Red': 2, 'Green': 0, 'Orange': 0, 'Amount': 12})

    def test_payout_push_1_1_split(self):
        """
        Testing the push payout on Split Wager 2 with 1 White and 1 pink chips in HumanPlayer's chip pile, 1 White and 1
        Red in HumanPlayer's Main wager, and 1 White and 1 Red in HumanPlayer's Split wager 2
        """
        player = HumanPlayer('Masha')
        test_chips = 1
        test_wager = 1
        test_total = 3.5
        test_wager_amount = 6
        player.chips = {'White': test_chips, 'Pink': test_chips, 'Red': 0, 'Green': 0, 'Orange': 0,
                        'Amount': test_total}
        player.wagers = {'Main Wager': {'White': test_wager, 'Pink': 0, 'Red': test_wager, 'Green': 0, 'Orange': 0,
                                        'Amount': test_wager_amount},
                         'Insurance': {'White': 0, 'Pink': 0, 'Red': 0, 'Green': 0, 'Orange': 0, 'Amount': 0},
                         'Split Wager 1': {'White': 0, 'Pink': 0, 'Red': 0, 'Green': 0, 'Orange': 0, 'Amount': 0},
                         'Split Wager 2': {'White': test_wager, 'Pink': 0, 'Red': test_wager, 'Green': 0, 'Orange': 0,
                                           'Amount': test_wager_amount},
                         'Split Wager 3': {'White': 0, 'Pink': 0, 'Red': 0, 'Green': 0, 'Orange': 0, 'Amount': 0}}

        # testing the add_winnings(self, payout, bet) method (adding the won chips to HumanPlayer's chips)
        player.add_winnings('Push', 'Split Wager 2')
        result_chips = player.chips
        result_wager = player.wagers['Split Wager 2']
        self.assertEqual(result_chips, {'White': 2, 'Pink': 1, 'Red': 1, 'Green': 0, 'Orange': 0, 'Amount': 9.5})
        self.assertEqual(result_wager, {'White': 1, 'Pink': 0, 'Red': 1, 'Green': 0, 'Orange': 0, 'Amount': 6})

        # testing the clear_wager() method (sets all wager amounts and number of chips in all wagers to zero
        # after a finished hand)
        player.clear_wager()
        result_clr_main_wager = player.wagers['Main Wager']
        result_clr_split2 = player.wagers['Split Wager 2']
        self.assertEqual(result_clr_main_wager, {'White': 0, 'Pink': 0, 'Red': 0, 'Green': 0, 'Orange': 0, 'Amount': 0})
        self.assertEqual(result_clr_split2, {'White': 0, 'Pink': 0, 'Red': 0, 'Green': 0, 'Orange': 0, 'Amount': 0})

    def test_payout_push_1_2_split(self):
        """
        Testing the push payout on Split wager 3 with 1 White and 1 pink chips in HumanPlayer's chip pile, 1 White and 1
        Red in HumanPlayer's Main wager, and 2 White and 2 Red in HumanPlayer's Split wager 3
        """
        player = HumanPlayer('Masha')
        test_chips = 1
        test_wager = 2
        test_total = 3.5
        test_wager_amount = 6
        player.chips = {'White': test_chips, 'Pink': test_chips, 'Red': 0, 'Green': 0, 'Orange': 0,
                        'Amount': test_total}
        player.wagers = {'Main Wager': {'White': test_wager / 2, 'Pink': 0, 'Red': test_wager / 2, 'Green': 0,
                                        'Orange': 0, 'Amount': test_wager_amount},
                         'Insurance': {'White': 0, 'Pink': 0, 'Red': 0, 'Green': 0, 'Orange': 0, 'Amount': 0},
                         'Split Wager 1': {'White': 0, 'Pink': 0, 'Red': 0, 'Green': 0, 'Orange': 0, 'Amount': 0},
                         'Split Wager 2': {'White': 0, 'Pink': 0, 'Red': 0, 'Green': 0, 'Orange': 0, 'Amount': 0},
                         'Split Wager 3': {'White': test_wager, 'Pink': 0, 'Red': test_wager, 'Green': 0, 'Orange': 0,
                                           'Amount': test_wager_amount * 2}}

        # testing the add_winnings(self, payout, bet) method (adding the won chips to HumanPlayer's chips):
        player.add_winnings('Push', 'Split Wager 3')
        result_chips = player.chips
        result_wager = player.wagers['Split Wager 3']
        self.assertEqual(result_chips, {'White': 3, 'Pink': 1, 'Red': 2, 'Green': 0, 'Orange': 0, 'Amount': 15.5})
        self.assertEqual(result_wager, {'White': 2, 'Pink': 0, 'Red': 2, 'Green': 0, 'Orange': 0, 'Amount': 12})

    def test_payout_blackjack_1_1pink(self):
        """
        testing the Blackjack payout with 1 White and 1 Pink chips in HumanPlayer's chip pile and 1 White and 1 Pink in
         HumanPlayer's Main Wager
        """
        player = HumanPlayer('Masha')
        test_chips = 1
        test_wager = 1
        test_total = 3.5
        test_wager_amount = 3.5
        player.chips = {'White': test_chips, 'Pink': test_chips, 'Red': 0, 'Green': 0, 'Orange': 0,
                        'Amount': test_total}
        player.wagers = {'Main Wager': {'White': test_wager, 'Pink': test_wager, 'Red': 0, 'Green': 0, 'Orange': 0,
                                        'Amount': test_wager_amount},
                         'Insurance': {'White': 0, 'Pink': 0, 'Red': 0, 'Green': 0, 'Orange': 0, 'Amount': 0},
                         'Split Wager 1': {'White': 0, 'Pink': 0, 'Red': 0, 'Green': 0, 'Orange': 0, 'Amount': 0},
                         'Split Wager 2': {'White': 0, 'Pink': 0, 'Red': 0, 'Green': 0, 'Orange': 0, 'Amount': 0},
                         'Split Wager 3': {'White': 0, 'Pink': 0, 'Red': 0, 'Green': 0, 'Orange': 0, 'Amount': 0}}

        # testing the add_winnings(self, payout, bet) method (adding the won chips to HumanPlayer's chips)
        player.add_winnings('3:2', 'Main Wager')
        result_chips = player.chips
        result_wager = player.wagers['Main Wager']
        self.assertEqual(result_chips, {'White': 2, 'Pink': 2, 'Red': 1, 'Green': 0, 'Orange': 0, 'Amount': 12})
        self.assertEqual(result_wager, {'White': 1, 'Pink': 1, 'Red': 0, 'Green': 0, 'Orange': 0, 'Amount': 3.5})

        # testing the clear_wager() method (sets the wager amount and number of chips in the wager to zero
        # after a finished hand)
        player.clear_wager()
        result_clr_wager = player.wagers['Main Wager']
        self.assertEqual(result_clr_wager, {'White': 0, 'Pink': 0, 'Red': 0, 'Green': 0, 'Orange': 0, 'Amount': 0})


if __name__ == '__main__':
    unittest.main()
