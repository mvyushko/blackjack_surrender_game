"""
Testing surrender_offered(hand, dealer_upcard) function from blackjack_with_chips with Unittest library
"""
import unittest
from card_related_classes import Hand, Card, surrender_offered

class TestSrOffered(unittest.TestCase):

    def test_sr_offered_17_10_7(self):
        """
        testing the surrender_offered(hand, dealer_upcard) function with a 10 and a 7 in hand and a 8 dealer upcard
        """
        test_hand = Hand()
        test_hand.cards.extend([Card('♥', '10'), Card('♦', '7')])
        test_hand.score = 17
        test_dlr_card = '8'
        result = surrender_offered(test_hand, test_dlr_card)
        self.assertEqual(result, False)

    def test_sr_offered_17_7_10(self):
        """
        testing the surrender_offered(hand, dealer_upcard) function with a 7 and a 10 in hand and a 5 dealer upcard
        """
        test_hand = Hand()
        test_hand.cards.extend([Card('♥', '7'), Card('♦', '10')])
        test_hand.score = 17
        test_dlr_card = '5'
        result = surrender_offered(test_hand, test_dlr_card)
        self.assertEqual(result, False)


    def test_sr_offered_17_7_q(self):
        """
        Testing the surrender_offered(hand, dealer_upcard) function with a 7 and a Queen in hand and a 5 dealer upcard
        """
        test_hand = Hand()
        test_hand.cards.extend([Card('♥', '7'), Card('♦', 'Q')])
        test_hand.score = 17
        test_dlr_card = '5'
        result = surrender_offered(test_hand, test_dlr_card)
        self.assertEqual(result, False)

    def test_sr_offered_16_dealers_10(self):
        """
        testing the surrender_offered(hand, dealer_upcard) function with two 8's in hand and a 10 dealer upcard
        """
        test_hand = Hand()
        test_hand.cards.extend([Card('♥', '8'), Card('♦', '8')])
        test_hand.score = 16
        test_dlr_card = '10'
        result = surrender_offered(test_hand, test_dlr_card)
        self.assertEqual(result, True)

    def test_sr_offered_15_dealers_A(self):
        """
        testing the surrender_offered(hand, dealer_upcard) function with a 7 and a 8 in hand and an Ace dealer upcard
        """
        test_hand = Hand()
        test_hand.cards.extend([Card('♥', '7'), Card('♦', '8')])
        test_hand.score = 15
        test_dlr_card = 'A'
        result = surrender_offered(test_hand, test_dlr_card)
        self.assertEqual(result, True)

    def test_sr_offered_14_dealers_9(self):
        """
        testing the surrender_offered(hand, dealer_upcard) function with two 7's in hand and a 9 dealer upcard
        """
        test_hand = Hand()
        test_hand.cards.extend([Card('♥', '7'), Card('♦', '7')])
        test_hand.score = 14
        test_dlr_card = '9'
        result = surrender_offered(test_hand, test_dlr_card)
        self.assertEqual(result, False)

    def test_sr_offered_18_dealers_10(self):
        """
        testing the surrender_offered(hand, dealer_upcard) function with two 9's in hand and a 10 dealer upcard
        """
        test_hand = Hand()
        test_hand.cards.extend([Card('♥', '9'), Card('♦', '9')])
        test_hand.score = 18
        test_dlr_card = '10'
        result = surrender_offered(test_hand, test_dlr_card)
        self.assertEqual(result, False)

    def test_sr_offered_15_dealers_Q(self):
        """
        testing the surrender_offered(hand, dealer_upcard) function with a 7 and an 8 in hand and a Q dealer upcard
        """
        test_hand = Hand()
        test_hand.cards.extend([Card('♥', '7'), Card('♦', '8')])
        test_hand.score = 15
        test_dlr_card = 'Q'
        result = surrender_offered(test_hand, test_dlr_card)
        self.assertEqual(result, True)

if __name__ == '__main__':
    unittest.main()
