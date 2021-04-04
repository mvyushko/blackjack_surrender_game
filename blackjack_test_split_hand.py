"""
Testing splitting of a Hand object from blackjack_with_chips with Unittest library
"""
import unittest
from blackjack_with_chips import Card, Hand, HumanPlayer

class TestCases(unittest.TestCase):


    def test_split_pair_J(self):
        """
        testing the split_pair(self) method of Hand class (splitting a pair of two Jacks)
        """
        test_hand = Hand('Normal')
        test_hand.cards.extend([Card('♥', 'J'), Card ('♦', 'J')])
        test_hand.score = 20
        split_pair = test_hand.split_pair()
        result = (split_pair[0].__str__(), split_pair[1].__str__())
        result_score = test_hand.score
        num_cards_left = len(test_hand.cards)

        self.assertEqual(result,('J♦', 'J♥'))
        self.assertEqual(num_cards_left, 0)
        self.assertEqual(result_score, 0)

    def test_add_card_from_split_J(self):
        """
        Testing the add_card_from_split(self, split_card) method of Hand class (splitting a pair of two Jacks)
        """
        test_hand = Hand('Normal')
        test_split_hand1 = Hand('Split')
        test_split_hand2 = Hand('Split')
        test_hand.cards.extend([Card('♥', 'J'), Card('♦', 'J')])
        split_pair = test_hand.split_pair()
        test_split_hand1.add_card_from_split(split_pair[0])
        test_split_hand2.add_card_from_split(split_pair[1])
        result1 = test_split_hand1.cards[0].__str__()
        result2 = test_split_hand2.cards[0].__str__()
        num_cards_split1 = len(test_split_hand1.cards)
        num_cards_split2 = len(test_split_hand2.cards)
        num_cards_left = len(test_hand.cards)
        result1_score = test_split_hand1.score
        result2_score = test_split_hand2.score

        self.assertEqual(result1, 'J♦')
        self.assertEqual(result2, 'J♥')
        self.assertEqual(num_cards_left, 0)
        self.assertEqual(num_cards_split1, 1)
        self.assertEqual(num_cards_split2, 1)
        self.assertEqual(result1_score, 10)
        self.assertEqual(result2_score, 10)

    def test_HumanPlayer_split_hand_J(self):
        """
        Testing the start_split_hand(self, split_hand_number, split_wager_number) method of HumanPlayer class (splitting
        a pair of two Jacks)
        """
        player = HumanPlayer('Masha')
        test_hand = Hand('Normal')
        player.start_split_hand('1', 0)
        player.start_split_hand('2', 1)
        test_hand.cards.extend([Card('♥', 'J'), Card('♦', 'J')])
        split_pair = test_hand.split_pair()
        player.split_hands[0].add_card_from_split(split_pair[0])
        player.split_hands[1].add_card_from_split(split_pair[1])
        result1 = player.split_hands[0].cards[0].__str__()
        result2 = player.split_hands[1].cards[0].__str__()
        num_cards_split1 = len(player.split_hands[0].cards)
        num_cards_split2 = len(player.split_hands[1].cards)
        num_cards_left = len(test_hand.cards)
        result1_score = player.split_hands[0].score
        result2_score = player.split_hands[1].score

        self.assertEqual(result1, 'J♦')
        self.assertEqual(result2, 'J♥')
        self.assertEqual(num_cards_left, 0)
        self.assertEqual(num_cards_split1, 1)
        self.assertEqual(num_cards_split2, 1)
        self.assertEqual(result1_score, 10)
        self.assertEqual(result2_score, 10)

    def test_split_pair_A(self):
        """
        testing the split_pair(self) method of Hand class (splitting a pair of two Aces)
        """
        test_hand = Hand('Normal')
        test_hand.cards.extend([Card('♥', 'A'), Card ('♦', 'A')])
        test_hand.score = 20
        split_pair = test_hand.split_pair()
        result = (split_pair[0].__str__(), split_pair[1].__str__())
        result_score = test_hand.score
        num_cards_left = len(test_hand.cards)

        self.assertEqual(result,('A♦', 'A♥'))
        self.assertEqual(num_cards_left, 0)
        self.assertEqual(result_score, 0)

    def test_add_card_from_split_A(self):
        """
        Testing the add_card_from_split(self, split_card) method of Hand class (splitting a pair of two Aces)
        """
        test_hand = Hand('Normal')
        test_split_hand1 = Hand('Split')
        test_split_hand2 = Hand('Split')
        test_hand.cards.extend([Card('♥', 'A'), Card('♦', 'A')])
        split_pair = test_hand.split_pair()
        test_split_hand1.add_card_from_split(split_pair[0])
        test_split_hand2.add_card_from_split(split_pair[1])
        result1 = test_split_hand1.cards[0].__str__()
        result2 = test_split_hand2.cards[0].__str__()
        num_cards_split1 = len(test_split_hand1.cards)
        num_cards_split2 = len(test_split_hand2.cards)
        num_cards_left = len(test_hand.cards)
        result1_score = test_split_hand1.score
        result2_score = test_split_hand2.score
        result1_value = test_split_hand1.cards[0].value
        result2_value = test_split_hand2.cards[0].value

        self.assertEqual(result1, 'A♦')
        self.assertEqual(result2, 'A♥')
        self.assertEqual(num_cards_left, 0)
        self.assertEqual(num_cards_split1, 1)
        self.assertEqual(num_cards_split2, 1)
        self.assertEqual(result1_score, 11)
        self.assertEqual(result2_score, 11)
        self.assertEqual(result1_value, 11)
        self.assertEqual(result2_value, 11)

    def test_HumanPlayer_split_hand_A(self):
        """
        Testing the start_split_hand(self, split_hand_number, split_wager_number) method of HumanPlayer class (splitting
         a pair of two Aces)
        """
        player = HumanPlayer('Masha')
        test_hand = Hand('Normal')
        player.start_split_hand('1', 0)
        player.start_split_hand('2', 1)
        test_hand.cards.extend([Card('♥', 'A'), Card('♦', 'A')])
        split_pair = test_hand.split_pair()
        player.split_hands[0].add_card_from_split(split_pair[0])
        player.split_hands[1].add_card_from_split(split_pair[1])
        result1 = player.split_hands[0].cards[0].__str__()
        result2 = player.split_hands[1].cards[0].__str__()
        num_cards_split1 = len(player.split_hands[0].cards)
        num_cards_split2 = len(player.split_hands[1].cards)
        num_cards_left = len(test_hand.cards)
        result1_score = player.split_hands[0].score
        result2_score = player.split_hands[1].score

        self.assertEqual(result1, 'A♦')
        self.assertEqual(result2, 'A♥')
        self.assertEqual(num_cards_left, 0)
        self.assertEqual(num_cards_split1, 1)
        self.assertEqual(num_cards_split2, 1)
        self.assertEqual(result1_score, 11)
        self.assertEqual(result2_score, 11)

if __name__ == '__main__':
    unittest.main()