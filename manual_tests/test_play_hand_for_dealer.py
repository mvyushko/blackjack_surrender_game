"""
Creates an instance of Player class representing a Dealer, and an instance of a Deck class. Starts a Hand for Dealer,
adds two cards from Deck. Plays the Hand for Dealer (up to soft 17). Prints out the resulting score and whether it was
a Blackjack.
"""
from card_related_classes import Deck, Card
from player_classes import Player

dealer = Player()
deck = Deck()
deck.deck_cards.extend([Card('♦', '3'), Card('♦', '8')])

dealer.start_hand()
dealer.hand.add_card_from_deck(deck)
dealer.hand.add_card_from_deck(deck)

score, dealers_natural = dealer.hand.play_for_dealer(deck)
dealer.hand.display_face_up('Dealer')

print('Dealer Hand Score:', score)
print('Dealer has a Blackjack:', dealers_natural)
