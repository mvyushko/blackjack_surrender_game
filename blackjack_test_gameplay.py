from blackjack_with_chips import Player, HumanPlayer, Deck, Card, insurance_requested, double_down_requested,\
    hit_or_stand, ready_to_play, press_any_key_to_continue
player = HumanPlayer('Masha')
dealer = Player()
deck = Deck()
player.chips = {'White': 0, 'Pink': 0, 'Red': 0, 'Green': 1, 'Orange': 1}
player.wager = {'White': 0, 'Pink': 0, 'Red': 0, 'Green': 0, 'Orange': 1}
player.chips_total = 75
player.wager_amount = 50
deck.deck_cards.extend([Card('♦', 'Q'), Card('♥', 'Q'), Card('♦', '5'), Card('♦', '6')])

player.start_hand()
dealer.start_hand()
player.hand.add_card_from_deck(deck)
player.hand.add_card_from_deck(deck)
dealer.hand.add_card_from_deck(deck)
dealer.hand.add_card_from_deck(deck)

dealer.hand.display_one_face_down('Dealer')
player.hand.display_face_up(f'{player.name}')

# game logic
# natural Blackjack in player's hand:
if player.hand.score == 21:
    print('\nBLACKJACK!')

    # clearing screeen and displaying all cards face up:
    print('\n' * 100)
    dealer.hand.display_face_up('Dealer')
    player.hand.display_face_up(f'{player.name}')

    # indicating that player has a Blackjack:
    print('\nBLACKJACK!')

    # checking if dealer has a natural Blackjack too:
    if dealer.hand.score == 21:
        print('\nBut Dealer has a Blackjack too!')
        print('TIE!')
        player.add_winnings('Tie', 'Main Wager')

    # when dealer doesn't have a Blackjack:
    else:
        print(f'\n{player.name} has won!')
        player.add_winnings('3:2', 'Main Wager')
else:
    # player's turn:
    print(f"\n{player.name}'s turn!")

    # checking if doubling down is possible:
    if player.hand.score == 10 or player.hand.score == 11:

        if player.chips_total >= player.wager_amount:
            # displaying all chips and cards and asking if player wants to double down:
            print('\n' * 100)
            player.display_chips('Chips')
            player.display_chips('Main Wager', 'Split Wager', 'Insurance')
            dealer.hand.display_one_face_down('Dealer')
            player.hand.display_face_up(f'{player.name}')
            dd_requested = double_down_requested()
        else:
            dd_requested = False

    else:
        dd_requested = False

    hit = True

    while player.hand.score < 21 and hit == True:

        if dd_requested:
            # doubling down:
            player.double_wager('Double Down')
            print('\n' * 100)
            dealer.hand.display_one_face_down('Dealer')
            player.hand.display_face_up(f'{player.name}')
            player.display_chips('Main Wager', 'Split Wager', 'Insurance')
        else:
            pass

        hit = hit_or_stand()
        if hit:
            player.hand.add_card_from_deck(deck)
            print('\n' * 100)
            dealer.hand.display_one_face_down('Dealer')
            player.hand.display_face_up(f'{player.name}')

            if player.hand.score == 21:
                pass
            elif player.hand.score > 21:
                print('\n' * 100)
                dealer.hand.display_face_up('Dealer')
                player.hand.display_face_up(f'{player.name}')
                print('\nBUST!')
                print('House has won!')
                break
            elif dd_requested:
                # player is allowed to hit only once after doubling down
                hit = False

        else:
            pass

    else:

        # dealer's turn
        # offer Insurance bet to player if dealer's upcard is an Ace and player has any chips left:
        if dealer.hand.cards[0].rank == 'A' and player.chips_total > 0 and insurance_requested():
            print('\n')
            player.place_bet('Insurance')
            insurance_placed = True
            ready = ready_to_play('Continue')
        else:
            insurance_placed = False
            ready = True

        if ready:
            print('\n' * 100)
            dealer.hand.display_face_up('Dealer')
            player.hand.display_face_up(f'{player.name}')
        else:
            pass

        # checking if dealer has a natural blackjack:
        if dealer.hand.score == 21:
            print('\nDEALER HAS A BLACKJACK!')
            print('House has won!')

            # checking if an Insurance bet has been placed:
            if insurance_placed:
                print('\nYour Insurance bet has won!')
                # adding winnings on the Insurance bet:
                player.add_winnings('2:1', 'Insurance')

        elif player.hand.score == 21:
            print(f'\n{player.name} has won!')
            player.add_winnings('1:1', 'Main Wager')
        elif dealer.hand.score > player.hand.score:
            print('\nHouse has won!')
        elif dealer.hand.score >= 17 and dealer.hand.score == player.hand.score:
            print('\nTIE!')
            player.add_winnings('Tie', 'Main Wager')
        else:

            while dealer.hand.score < 21:
                dealer.hand.add_card_from_deck(deck)
                print('\n' * 100)
                dealer.hand.display_face_up('Dealer')
                player.hand.display_face_up(f'{player.name}')

                if dealer.hand.score > 21:
                    print('\nDEALER HAS BUST!')
                    print(f'{player.name} has won!')
                    player.add_winnings('1:1', 'Main Wager')
                elif dealer.hand.score > player.hand.score:
                    print('\nHouse has won!')
                    break
                elif dealer.hand.score >= 17 and dealer.hand.score == player.hand.score:
                    print('\nTIE!')
                    player.add_winnings('Tie', 'Main Wager')
                    break

print(player.chips)
print(player.chips_total)