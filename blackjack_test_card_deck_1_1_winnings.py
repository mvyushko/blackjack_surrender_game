"""
Testing blackjack_with_chips with Unittest library
"""
import unittest
from blackjack_with_chips import Card, Deck, HumanPlayer

class TestCases(unittest.TestCase):
    def test_card(self):

        #checking the value attribute depending on Card's Rank
        test = ('♥', 'Q')
        card = Card(test[0], test[1])
        result_value = card.value
        self.assertEqual(result_value, 10)

        #checking a string representation of a Card
        result_str = card.__str__()
        self.assertEqual(result_str, 'Q♥')

    def test_deck(self):
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

    def test_player(self):
        player = HumanPlayer('Masha')
        test_chips = 1
        test_wager = 2
        test_total = 3.5
        test_wager_amount = 12
        player.chips = {'White': test_chips, 'Pink': test_chips, 'Red': 0, 'Green': 0, 'Orange': 0}
        player.wager = {'White': test_wager, 'Pink': 0, 'Red': test_wager, 'Green': 0, 'Orange': 0}
        player.chips_total = test_total
        player.wager_amount = test_wager_amount

        #testing the add_winnings(payout, wager) method (adding the won chips to Player's chip pile and the wager
        # amount to Player's total)
        player.add_winnings('1:1', 'Main Wager')
        result_chips = player.chips
        result_total = player.chips_total
        result_wager = player.wager
        self.assertEqual(result_total, 27.5)
        self.assertEqual(result_chips, {'White': 5, 'Pink': 1, 'Red': 4, 'Green': 0, 'Orange': 0})
        self.assertEqual(result_wager, {'White': 2, 'Pink': 0, 'Red': 2, 'Green': 0, 'Orange': 0})

        #testing the clear_wager() method (sets the wager amount and number of chips in the wager to zero
        # after a finished hand)
        player.clear_wager()
        result_clr_wager = player.wager
        result_clr_wager_amount = player.wager_amount
        self.assertEqual(result_clr_wager_amount, 0)
        self.assertEqual(result_clr_wager, {'White': 0, 'Pink': 0, 'Red': 0, 'Green': 0, 'Orange': 0})

        #testing the exchange_possible() method (checks if there are any high-value chips in Player's chip pile
        # and returns a boolean and a string containing the color of the highest-value chip in Player's pile)
        result_exchange_possible, result_high_value_color = player.cheque_change_possible()
        self.assertEqual(result_exchange_possible, False)
        self.assertEqual(result_high_value_color, 'None')

if __name__ == '__main__':
    unittest.main()

