"""
Creates an instance of HumanPlayer class representing the human player, an instance of Player class representing the
computer Dealer, and an instance of a Deck class representing a 52-card French-Suited deck. Starts Hands for both
HumanPlayer and Dealer, sets a nonzero number of chips in HumanPlayers chip pile and wagers.
Plays a Hand (and all Split Hands created by splitting it) for the human player. Prints out the resulting hand score
list, natural Blackjack list, and the updated HumanPlayer's chips and wagers dictionaries.
"""

from blackjack_surrender_game import Player, HumanPlayer, Deck, Card, players_turn

#dictionary containing pairs of split_hand_number attributes assigned to newly created split hands,  depending on which
#hand they come from.
#keys: split_hand_number attributes of hands being split
#values: pairs of split_hand_number attributes assigned to hands created by splitting
new_split_hand_numbers = {'0': ('1', '2'), '1': ('1.1', '1.2'), '2': ('2.1', '2.2')}
#"empty" dictionary containing zero chips of each color:
empty = {'White': 0, 'Pink': 0, 'Red': 0, 'Green': 0, 'Orange': 0, 'Amount': 0}


if __name__ == '__main__':

    player = HumanPlayer('Masha')
    dealer = Player()
    player.chips = {'White': 0, 'Pink': 0, 'Red': 6, 'Green': 0, 'Orange': 0, 'Amount': 30}
    player.wagers = {'Main Wager': {'White': 1, 'Pink': 0, 'Red': 1, 'Green': 0, 'Orange': 0,
                                    'Amount': 6},
                     'Insurance': {'White': 8, 'Pink': 0, 'Red': 0, 'Green': 0, 'Orange': 0, 'Amount': 0},
                     'Split Wager 1': {'White': 0, 'Pink': 0, 'Red': 0, 'Green': 0, 'Orange': 0, 'Amount': 0},
                     'Split Wager 2': {'White': 0, 'Pink': 0, 'Red': 0, 'Green': 0, 'Orange': 0, 'Amount': 0},
                     'Split Wager 3': {'White': 0, 'Pink': 0, 'Red': 0, 'Green': 0, 'Orange': 0, 'Amount': 0}}
    deck = Deck()
    deck.shuffle()
    deck.deck_cards.extend([Card('♦','5'), Card('♦','5'), Card('♦','5'), Card('♣','5'), Card('♦','5'),
                            Card('♣','6'), Card('♦','5'), Card('♣','6'), Card('♣','5')])
    player.start_hand()
    dealer.start_hand()

    player.hand.add_card_from_deck(deck)
    dealer.hand.add_card_from_deck(deck)

    player.hand.add_card_from_deck(deck)
    dealer.hand.add_card_from_deck(deck)

    print(players_turn(player, dealer, deck))

    for key, value in player.wagers.items():
        if value != empty:
            print(key, ':', value)

    print('Players chips:', player.chips)


