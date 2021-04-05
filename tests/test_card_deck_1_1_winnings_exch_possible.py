"""
Testing Card and Deck classes, add_winnings(self, payout, wager), clear_wager(self), and cheque_change_possible(self)
methods of HumanPlayer class with Unittest library
"""
import unittest
from card_related_classes import Card, Deck
from player_classes import HumanPlayer

class TestCardDeckHumanPlayer(unittest.TestCase):

    def test_card(self):
        """
        Testing the attributes of the Card class
        """
        #checking the value attribute depending on Card's Rank
        test = ('♥', 'Q')
        card = Card(test[0], test[1])
        result_value = card.value
        self.assertEqual(result_value, 10)

        #checking a string representation of a Card
        result_str = card.__str__()
        self.assertEqual(result_str, 'Q♥')

    def test_deck(self):
        """
        Testing the attributes of the Deck class
        """
        deck = Deck()

        #checking the string representation of the last Card in a newly created Deck
        result_str = deck.deck_cards[-1].__str__()
        self.assertEqual(result_str, 'A♠')

        #checking the number of cards in a Deck
        result_len = len(deck.deck_cards)
        self.assertEqual(result_len, 52)

        #checking the number of cards of a certain value in a Deck
        test = '10'
        number_of_cards = 0

        for card in deck.deck_cards:
            if card.rank == test:
                number_of_cards += 1

        self.assertEqual(number_of_cards, 4)

    def test_humanplayer_methods(self):
        """
        testing the add_winnings(self, payout, wager), clear_wager(self), and cheque_change_possible(self) methods of
        HumanPlayer class
        """
        player = HumanPlayer('Masha')
        test_chips = 1
        test_wager = 2
        test_total = 3.5
        test_wager_amount = 12
        player.chips = {'White': test_chips, 'Pink': test_chips, 'Red': 0, 'Green': 0, 'Orange': 0,
                        'Amount': test_total}
        player.wagers = {'Main Wager': {'White': test_wager, 'Pink': 0, 'Red': test_wager, 'Green': 0, 'Orange': 0,
                                        'Amount': test_wager_amount},
                         'Insurance': {'White': 0, 'Pink': 0, 'Red': 0, 'Green': 0, 'Orange': 0, 'Amount': 0},
                         'Split Wager 1': {'White': 0, 'Pink': 0, 'Red': 0, 'Green': 0, 'Orange': 0, 'Amount': 0},
                         'Split Wager 2': {'White': 0, 'Pink': 0, 'Red': 0, 'Green': 0, 'Orange': 0, 'Amount': 0},
                         'Split Wager 3': {'White': 0, 'Pink': 0, 'Red': 0, 'Green': 0, 'Orange': 0, 'Amount': 0}}

        #testing the add_winnings(self, payout, wager) method (adding the won chips to HumanPlayer's chip pile)
        player.add_winnings('1:1', 'Main Wager')
        result_chips = player.chips
        result_wager = player.wagers['Main Wager']
        self.assertEqual(result_chips, {'White': 5, 'Pink': 1, 'Red': 4, 'Green': 0, 'Orange': 0, 'Amount': 27.5})
        self.assertEqual(result_wager, {'White': 2, 'Pink': 0, 'Red': 2, 'Green': 0, 'Orange': 0, 'Amount': 12})

        #testing the clear_wager(self) method (sets the wager amount and number of chips in the wager to zero
        # after a finished hand)
        player.clear_wager()
        result_clr_wager = player.wagers['Main Wager']
        self.assertEqual(result_clr_wager, {'White': 0, 'Pink': 0, 'Red': 0, 'Green': 0, 'Orange': 0, 'Amount': 0})

        #testing the cheque_change_possible(self) method (checks if there are any high-value chips in Player's chip pile
        # and returns a boolean and a string containing the color of the highest-value chip in Player's pile)
        result_exchange_possible, result_high_value_color = player.cheque_change_possible()
        self.assertEqual(result_exchange_possible, False)
        self.assertEqual(result_high_value_color, 'None')

if __name__ == '__main__':
    unittest.main()


