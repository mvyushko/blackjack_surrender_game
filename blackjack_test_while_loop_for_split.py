from blackjack_with_chips import HumanPlayer, Deck, Card

player = HumanPlayer('Masha')
deck = Deck()
deck.deck_cards.extend([Card('♥','A'), Card('♥','K'), Card('♦','A'), Card('♣','A')])
player.start_hand()

player.hand.add_card_from_deck(deck)
player.hand.add_card_from_deck(deck)

hand_list = [player.hand]
score_list = []

while len(hand_list) > 0:
    hand = hand_list.pop(0)
    hand.display_face_up('Player')
    print('\nHand score:', hand.score)

    if hand.type == 'Normal' or hand.split_hand_number <= 2:

        if hand.cards[0].rank == hand.cards[1].rank:
            choice = input('Split?: Y or N ')

            if choice == 'y':
                player.start_split_hand(len(player.split_hands) + 1)
                player.start_split_hand(len(player.split_hands) + 1)
                split_card1, split_card2 = hand.split_pair()

                player.split_hands[-2].add_card_from_split(split_card1)
                player.split_hands[-1].add_card_from_split(split_card2)

                player.split_hands[-2].add_card_from_deck(deck)
                player.split_hands[-1].add_card_from_deck(deck)
                hand_list = [player.split_hands[-2], player.split_hands[-1]] + hand_list
                continue

    print('This hand has been played!')
    score_list.append(hand.score)

print(score_list)




