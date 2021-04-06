"""
Creates an instance of HumanPlayer class representing the human player, an instance of Player class representing the
computer Dealer, and an instance of a Deck class representing a 52-card French-Suited deck. Starts a Hand for the player
and splits it, then splits again. Starts a Hand for Dealer and deals 2 cards to it. Runs the dealers_turn(dealer,
player, player_score_list, player_natural_list, deck) function which displays all player's and Dealer's cards.
Prints out the resulting hand score, and the boolean showing if Dealer has a Natural Blackjack.
"""
from card_related_classes import Card, Deck
from player_classes import Player, HumanPlayer
from gameplay import dealers_turn

# creating objects representing the human player, the computer Dealer, and the deck:
player = HumanPlayer('Masha')
dealer = Player()
deck = Deck()

deck.shuffle()
#adding multiple same-rank cards to the deck to make multiple Splits possible:
deck.deck_cards.extend([Card('♦', '5'), Card('♦', '5'), Card('♦', '6'), Card('♣', 'A'), Card('♦', '10'),
                        Card('♣', '2'), Card('♦', 'A'), Card('♣', 'A'), Card('♣', 'A')])

# setting nonzero player chips and wagers:
player.chips = {'White': 0, 'Pink': 0, 'Red': 6, 'Green': 0, 'Orange': 0, 'Amount': 30}
player.wagers = {'Main Wager': {'White': 1, 'Pink': 0, 'Red': 1, 'Green': 0, 'Orange': 0,
                                    'Amount': 6},
                     'Insurance': {'White': 0, 'Pink': 0, 'Red': 0, 'Green': 0, 'Orange': 0, 'Amount': 0},
                     'Split Wager 1': {'White': 0, 'Pink': 0, 'Red': 0, 'Green': 0, 'Orange': 0, 'Amount': 0},
                     'Split Wager 2': {'White': 0, 'Pink': 0, 'Red': 0, 'Green': 0, 'Orange': 0, 'Amount': 0},
                     'Split Wager 3': {'White': 0, 'Pink': 0, 'Red': 0, 'Green': 0, 'Orange': 0, 'Amount': 0}}

# creating Hand objects for both the player and the dealer:
player.start_hand()
dealer.start_hand()
player.hand.add_card_from_deck(deck)
dealer.hand.add_card_from_deck(deck)
player.hand.add_card_from_deck(deck)
dealer.hand.add_card_from_deck(deck)

# splitting the first pair:
player.start_split_hand('1', 0)
player.start_split_hand('2', 1)
split_pair = player.hand.split_pair()

# adding 1 card from split and 1 card from deck to new Split Hands:
player.split_hands[0].add_card_from_split(split_pair[0])
player.split_hands[0].add_card_from_deck(deck)
player.split_hands[1].add_card_from_split(split_pair[1])
player.split_hands[1].add_card_from_deck(deck)

# splitting the second pair:
player.start_split_hand('2.1', 1)
player.start_split_hand('2.2', 2)
split_pair1 = player.split_hands[1].split_pair()

# adding 1 card from split and 1 card from deck to new Split Hands:
player.split_hands[2].add_card_from_split(split_pair1[0])
player.split_hands[2].add_card_from_deck(deck)
player.split_hands[3].add_card_from_split(split_pair1[1])
player.split_hands[3].add_card_from_deck(deck)

#playing the Dealer's hand:
print(dealers_turn(dealer, player, [21, 17, 16], [True, False, False], deck))
