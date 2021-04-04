"""
Creates an instance of HumanPlayer class representing the human player, an instance of Player class representing the
computer Dealer, and an instance of a Deck class representing a 52-card French-Suited deck. Starts a Hand for Dealer
and deals 2 cards to it. Runs the dealers_turn(dealer, player, player_score_list, player_natural_list, deck) function.
Prints out the resulting hand score, and the boolean showing if Dealer has a Natural Blackjack.
"""
from blackjack_with_chips import Player, HumanPlayer, Deck, Card, dealers_turn

player = HumanPlayer('Masha')
dealer = Player()
deck = Deck()

deck.shuffle()
deck.deck_cards.extend([Card('♦', '5'), Card('♦', '5'), Card('♦', '6'), Card('♣', 'A'), Card('♦', '10'),
                        Card('♣', '2'), Card('♦', 'A'), Card('♣', 'A'), Card('♣', 'A')])

player.chips = {'White': 0, 'Pink': 0, 'Red': 6, 'Green': 0, 'Orange': 0, 'Amount': 30}
player.wagers = {'Main Wager': {'White': 1, 'Pink': 0, 'Red': 1, 'Green': 0, 'Orange': 0,
                                    'Amount': 6},
                     'Insurance': {'White': 0, 'Pink': 0, 'Red': 0, 'Green': 0, 'Orange': 0, 'Amount': 0},
                     'Split Wager 1': {'White': 0, 'Pink': 0, 'Red': 0, 'Green': 0, 'Orange': 0, 'Amount': 0},
                     'Split Wager 2': {'White': 0, 'Pink': 0, 'Red': 0, 'Green': 0, 'Orange': 0, 'Amount': 0},
                     'Split Wager 3': {'White': 0, 'Pink': 0, 'Red': 0, 'Green': 0, 'Orange': 0, 'Amount': 0}}

player.start_hand()
dealer.start_hand()
player.hand.add_card_from_deck(deck)
dealer.hand.add_card_from_deck(deck)
player.hand.add_card_from_deck(deck)
dealer.hand.add_card_from_deck(deck)

player.start_split_hand('1', 0)
player.start_split_hand('2', 1)
split_pair = player.hand.split_pair()
player.split_hands[0].add_card_from_split(split_pair[0])
player.split_hands[0].add_card_from_deck(deck)

player.split_hands[1].add_card_from_split(split_pair[1])
player.split_hands[1].add_card_from_deck(deck)

player.start_split_hand('2.1', 1)
player.start_split_hand('2.2', 2)
split_pair1 = player.split_hands[1].split_pair()

player.split_hands[2].add_card_from_split(split_pair1[0])
player.split_hands[2].add_card_from_deck(deck)

player.split_hands[3].add_card_from_split(split_pair1[1])
player.split_hands[3].add_card_from_deck(deck)

print(dealers_turn(dealer, player, [21, 17, 16], [True, False, False], deck))