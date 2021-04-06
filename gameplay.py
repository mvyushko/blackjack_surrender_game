"""
Text version of the 52-card Blackjack Late Surrender game for one human Player, and a computer Dealer.
Allows Splits, Doubling Down, Insurance and Surrender.
Dealer stands on soft 17. Blackjack pays 3:2.
To display cards, uses rectangles constructed of pipe operators and underscores.
To display chips, uses colored capital O letters.
"""
from interactive_functions import ask_players_name, hit_or_stand, split_requested, surrender_requested,\
    double_down_requested, insurance_requested, press_enter_to_continue, cheque_change_requested, more_chips_requested,\
    replay
from card_related_classes import Deck, surrender_offered
from player_classes import Player, HumanPlayer, EMPTY, NEW_SPLIT_HAND_NUMBERS

# gameplay functions:
def players_turn(player, dealer, deck):
    """
    Plays a Hand (and all Split Hands created by splitting it) for the human player. Requires input from player.
    :param player: a HumanPlayer object representing the human player.
    :param dealer: a Player object representing the computer Dealer.
    :param deck: a Deck object representing a 52-card French-suited deck.
    :return: a tuple containing 3 lists and a boolean: a list of integers representing final scores of all hands played;
     a list of booleans showing if there was a Natural Blackjack for each hand played; a list of names of
    corresponding wagers for each hand played; and a boolean showing if surrender has been requested.
    :rtype: score_list: list, natural_list: list, wager_list: list, sr_requested: bool
    """
    # creating the list of all human player's Blackjack hands left to play:
    hand_list = [player.hand]
    # variable score_list will be used to store the list of final scores of all hands played:
    score_list = []
    # variable natural_list will be used to store the list of booleans showing if there was a Natural Blackjack for each
    # hand played:
    natural_list = []
    # variable natural_list will be used to store the list of names of corresponding wagers for each hand played:
    wager_list = []
    # variable sr_requested will be used to store the boolean showing whether or not surrender is requested
    sr_requested = False

    # while loop checking if there are any hands left to play:
    while len(hand_list) > 0:
        # removing a hand to be played from the list:
        hand = hand_list.pop(0)

        # clearing the screen:
        print('\n' * 100)
        # showing dealer's cards one face up, one face down:
        dealer.hand.display_one_face_down('Dealer')
        # showing human player's cards face up:
        hand.display_face_up(player.name)

        # determining which wager corresponds to the hand being played:
        if hand.split_wager_number == 0:
            wager_name = 'Main Wager'
        else:
            wager_name = f'Split Wager {hand.split_wager_number}'

        # checking for the natural Blackjack:
        if hand.score == 21:
            natural = True
            print('\nBLACKJACK!')
            press_enter_to_continue()
        else:
            natural = False

            # checking if surrender is possible on this hand:
            if hand.type == 'Normal' and dealer.hand.score != 21 and player.wagers[wager_name]['Amount'] > 1:

                # checking if player has been dealt a 14, 15, 16, or 17:
                if surrender_offered(hand, dealer.hand.cards[0].rank):
                    sr_requested = surrender_requested()

                    if sr_requested:
                        player.surrender()
                        break

            # checking if splitting is allowed for this hand:
            if hand.type == 'Normal' or hand.split_hand_number in ['1', '2']:

                # checking if there is a pair of same-rank cards and if human player has enough chips for a split:
                if hand.cards[0].rank == hand.cards[1].rank and player.chips['Amount'] >= \
                        player.wagers[wager_name]['Amount']:

                    # displaying all human player's chips and wagers:
                    print('\n')
                    player.display_chips('Chips')
                    print('\n')
                    player.display_chips(*player.wagers.keys())

                    # asking if human player wants to split the pair:
                    if split_requested():

                        # splitting:
                        # determining the new split wager numbers:
                        if hand.type == 'Normal':
                            new_split_wager_numbers = (0, 1)
                        elif hand.type == 'Split Hand' and hand.split_hand_number == '1':
                            new_split_wager_numbers = (0, 2)
                        elif hand.type == 'Split Hand' and hand.split_hand_number == '2':

                            if len(player.split_hands) == 2:
                                new_split_wager_numbers = (1, 2)
                            elif len(player.split_hands) == 4:
                                new_split_wager_numbers = (1, 3)

                        # splitting the wager:
                        player.double_wager('Split', *new_split_wager_numbers)
                        # creating two new split hands:
                        player.start_split_hand(NEW_SPLIT_HAND_NUMBERS[hand.split_hand_number][0],
                                                new_split_wager_numbers[0])
                        player.start_split_hand(NEW_SPLIT_HAND_NUMBERS[hand.split_hand_number][1],
                                                new_split_wager_numbers[1])
                        # splitting the pair:
                        split_card1, split_card2 = hand.split_pair()

                        # adding one of the split cards to each split hand:
                        player.split_hands[-2].add_card_from_split(split_card1)
                        player.split_hands[-1].add_card_from_split(split_card2)

                        # adding one card from deck to each split hand:
                        player.split_hands[-2].add_card_from_deck(deck)
                        player.split_hands[-1].add_card_from_deck(deck)
                        hand_list = [player.split_hands[-2], player.split_hands[-1]] + hand_list
                        # clearing the screen:
                        print('\n' * 100)
                        # displaying the updated human player's chips and wagers:
                        player.display_chips('Chips')
                        print('\n')
                        player.display_chips(*player.wagers.keys())
                        # asking the player to press enter to continue:
                        press_enter_to_continue()
                        continue

        # checking if doubling down is possible:
        if hand.score in [10, 11] and player.chips['Amount'] >= player.wagers[wager_name]['Amount']:
            # clearing the screen:
            print('\n' * 100)
            # showing dealer's cards one face up, one face down:
            dealer.hand.display_one_face_down('Dealer')
            # showing human player's cards face up:
            hand.display_face_up(player.name)
            print('\n')
            # displaying all human player's chips and wagers:
            player.display_chips('Chips')
            print('\n')
            player.display_chips(*player.wagers.keys())
            # asking if human player wants to double down:
            dd_requested = double_down_requested()

            # doubling down:
            if dd_requested:
                # doubling the wager:
                player.double_wager('Double Down', hand.split_wager_number)
                # clearing the screen:
                print('\n' * 100)
                # displaying the updated human player's chips and wagers:
                player.display_chips('Chips')
                print('\n')
                player.display_chips(*player.wagers.keys())
                # asking human player to press enter to continue:
                press_enter_to_continue()
                # clearing the screen:
                print('\n' * 100)
                # showing dealer's cards one face up, one face down:
                dealer.hand.display_one_face_down('Dealer')
                # showing human player's cards face up:
                hand.display_face_up(player.name)

        # doubling down not possible:
        else:
            dd_requested = False

        # checking if human player has split a pair of Aces:
        if hand.type == 'Split Hand' and hand.cards[0].rank == 'A':
            # the player is only allowed to draw one card on each split Ace:
            print("\nYou can't take any more cards to this hand (split Aces)")
            hit = False
            # asking human player to press enter to continue:
            press_enter_to_continue()
        # in all other cases, player is allowed to draw at least one more card:
        else:
            hit = True

        # while loop checking if the hand score is still less than 21, and human player is allowed and willing to hit
        # one more card:
        while hand.score < 21 and hit:
            # asking human player to choose hit or stand:
            hit = hit_or_stand()
            # hitting:
            if hit:
                # adding one card from deck to the hand:
                hand.add_card_from_deck(deck)
                # clearing the screen:
                print('\n' * 100)
                # showing dealer's cards one face up, one face down:
                dealer.hand.display_one_face_down('Dealer')
                # showing human player's cards face up:
                hand.display_face_up(player.name)

                # checking if there was a double down:
                if dd_requested and hand.score < 21:
                    # the player is only allowed to draw one card after doubling down:
                    print("\nYou can't take any more cards to this hand (Double Down)")
                    hit = False
                    # asking human player to press enter to continue:
                    press_enter_to_continue()

                # checking for a bust:
                if hand.score > 21:
                    print('\nBUST!')
                    # asking human player to press enter to continue:
                    press_enter_to_continue()
                # checking for a 21:
                elif hand.score == 21:
                    print('\n'
                          'YOU HAVE A 21!')
                    # asking human player to press enter to continue:
                    press_enter_to_continue()

        # adding the final hand score to the score list:
        score_list.append(hand.score)
        # adding the boolean showing whether there was a natural Blackjack to the natural list:
        natural_list.append(natural)
        # adding the name of corresponding wager to the wager list:
        wager_list.append(wager_name)

    # after all hands have been played, return the score list, the natural list, the wager list, and the boolean
    # showing if Surrender has been requested:
    return score_list, natural_list, wager_list, sr_requested

def dealers_turn(dealer, player, player_score_list, player_natural_list, deck):
    """
    Offers human player an Insurance bet if Dealer's upcard is an Ace, and plays the Dealer's hand.
    :param player: a HumanPlayer object representing the human player.
    :param dealer: a Player object representing the computer Dealer.
    :param player_score_list: a list containing final scores of all HumanPlayer's Hands played in current round
    :param player_natural_list: a list containing booleans showing if there was a Natural Blackjack for each
    HumanPlayer's Hand played in current round
    :param deck: a Deck object representing a 52-card French-suited deck
    :returns:  a tuple containing Dealer's final score, and a boolean showing if Dealer has a natural Blackjack
    :rtype: self.score: int, natural: bool
    """
    # the initial dealer's Hand score:
    dealer_score = dealer.hand.score
    # checking if Dealer has a Blackjack:
    dealer_natural = dealer.hand.score == 21

    # checking if human player has played any hands without both a bust or a Natural Blackjack:
    for score, natural in zip(player_score_list, player_natural_list):

        if score <= 21 and not natural:
            insurance_possible = True
            break

    else:
        insurance_possible = False

    if insurance_possible:

        # checking if Dealer's upcard is an Ace and if human player has any chips left:
        if dealer.hand.cards[0].rank == 'A' and player.chips['Amount'] > 0:
            print('\n' * 100)
            # showing dealer's cards one face up, one face down:
            dealer.hand.display_one_face_down('Dealer')
            # showing human player's cards face up:

            # if there are no split hands:
            if len(player.split_hands) == 0:
                player.hand.display_face_up(player.name)
            else:

                # showing all non-empty Split Hands:
                for hand in player.split_hands:

                    if hand.score > 0:
                        hand.display_face_up(player.name)

            print('\n')
            # displaying all human player's chips and wagers:
            player.display_chips('Chips')
            print('\n')
            player.display_chips(*player.wagers.keys())

            # asking if human player wants to place an Insurance bet:
            if insurance_requested():
                # placing the Insurance bet:
                print('\n')
                player.place_bet('Insurance')
                # clearing the screen:
                print('\n' * 100)
                # displaying the updated human player's chips and wagers:
                player.display_chips('Chips')
                print('\n')
                player.display_chips(*player.wagers.keys())
                # asking human player to press enter to continue:
                press_enter_to_continue()


        # playing Dealer's hand up to soft 17:
        dealer_score, dealer_natural = dealer.hand.play_for_dealer(deck)

    # clearing the screen:
    print('\n' * 100)
    # showing dealer's cards face up:
    dealer.hand.display_face_up('Dealer')
    # showing human player's cards face up:

    # if there are no split hands:
    if len(player.split_hands) == 0:
        player.hand.display_face_up(player.name)
    else:

        # showing all non-empty Split Hands:
        for hand in player.split_hands:

            if hand.score > 0:
                hand.display_face_up(player.name)

    print('\n')
    # returning Dealer's final score and a boolean showing if Dealer has a Blackjack:
    return dealer_score, dealer_natural

def check_outcome_and_add_winnings(player, player_score_list, player_natural_list, player_wager_list, dealer_score,
                                   dealer_natural):
    """
    Checks the outcome of a round and adds winnings (if any) to HumanPlayer's chips
    :param player: a HumanPlayer object representing the human player
    :param player_score_list: a list containing final scores of all HumanPlayer's Hands played in current round
    :param player_natural_list: a list containing booleans showing if there was a Natural Blackjack for each
    HumanPlayer's Hand played in current round
    :param player_wager_list: a list of names of corresponding wagers for each hand played in current round
    :param dealer_score: dealer's final score
    :param dealer_natural: a boolean showing if dealer has a Natural Blackjack
    :return: none
    """

    # if there was no split and just one hand has been played:
    if len(player_score_list) == 1:

        # checking for human player's Blackjack:
        if player_natural_list[0]:

            # checking for Dealer's Blackjack:
            if not dealer_natural:
                print (f'{player.name} has won 3:2!')
                player.add_winnings('3:2', 'Main Wager')
            else:
                print ('Dealer has a Blackjack too! PUSH!')
                player.add_winnings('Push', 'Main Wager')

        # checking for a bust:
        elif player_score_list[0] > 21:
            print('BUST! House has won!')
        # checking for Dealer's Blackjack:
        elif dealer_natural:
            print('Dealer has a Blackjack! House has won!')

            # checking if an Insurance bet has been placed:
            if player.wagers['Insurance'] != EMPTY:
                print (f"{player.name}'s Insurance bet has won!")
                player.add_winnings('2:1', 'Insurance')

        # checking for a Dealer bust:
        elif dealer_score > 21:
            print (f'DEALER BUST! {player.name} has won!')
            player.add_winnings('1:1', 'Main Wager')
        # checking if human player's score is greater than dealer's score:
        elif player_score_list[0] > dealer_score:
            print(f'{player.name} has won!')
            player.add_winnings('1:1', 'Main Wager')
        # checking for a tie:
        elif player_score_list[0] == dealer_score:
            print('PUSH!')
            player.add_winnings('Push', 'Main Wager')
        # checking if dealer's score is greater than human player's score:
        elif player_score_list[0] < dealer_score:
            print('House has won!')

    # more than 1 hand has been played:
    else:

        if dealer_natural:
            print('Dealer has a Blackjack!')

            # checking if an Insurance bet has been placed:
            if player.wagers['Insurance'] != EMPTY:
                print(f"{player.name}'s Insurance bet has won!")
                player.add_winnings('2:1', 'Insurance')

        elif dealer_score > 21:
            print('DEALER BUST!')

        for score, natural, wager in zip (player_score_list, player_natural_list, player_wager_list):
            # checking for human player's Blackjack:
            if natural:

                # checking for Dealer's Blackjack:
                if not dealer_natural:
                    print(f"{player.name}'s {wager} has won 3:2!")
                    player.add_winnings('3:2', wager)
                else:
                    print(f"PUSH on {player.name}'s {wager}!")
                    player.add_winnings('Push', wager)

            # checking for Dealer's Blackjack:
            elif dealer_natural:
                print(f"House has won {player.name}'s {wager}!")

            # checking for a bust:
            elif score > 21:
                print(f"BUST on {player.name}'s {wager}!")
            # checking for a Dealer bust:
            elif dealer_score > 21:
                print (f"{player.name}'s {wager} has won!")
                player.add_winnings('1:1', wager)
            # checking if human player's score is greater than dealer's score:
            elif score > dealer_score:
                print(f"{player.name}'s {wager} has won!")
                player.add_winnings('1:1', wager)
            # checking for a tie:
            elif score == dealer_score:
                print(f"PUSH on {player.name}'s {wager}!")
                player.add_winnings('Push', wager)
            # checking if dealer's score is greater than human player's score:
            elif score < dealer_score:
                print(f"House has won {player.name}'s {wager}!")


if __name__ == '__main__':

    # game setup:
    print('Welcome to the Blackjack Game!')
    # asking player's name:
    plr_name = ask_players_name()
    # creating a HumanPlayer object representing the player:
    plr = HumanPlayer(plr_name)
    # creating a Player object representing the dealer:
    dlr = Player()

    play_again = True
    need_more_chips = True
    first_round = True

    # game cycle:
    while play_again:

        # checking if player needs more chips:
        if need_more_chips:

            if not first_round and plr.chips == EMPTY:
                print('\n'*100)
                print(f'\n{plr.name} has no chips left!')
            else:
                print('\n'*100)

            #asking player to purchase chips:
            plr.get_chips()
            first_round = False
            #asking to press enter to continue:
            press_enter_to_continue()
        else:
            pass

        # shuffling the deck and placing a bet:
        print('\n'*100)
        print('New round!')
        playing_deck = Deck()
        playing_deck.shuffle()
        plr.place_bet('Main Wager')
        # asking to press enter to continue:
        press_enter_to_continue()

        # creating a "Normal" Hand object for player:
        plr.start_hand()

        # creating a "Normal" Hand object for dealer:
        dlr.start_hand()

        # dealing initial 2 cards to both player and dealer:
        plr.hand.add_card_from_deck(playing_deck)
        dlr.hand.add_card_from_deck(playing_deck)

        plr.hand.add_card_from_deck(playing_deck)
        dlr.hand.add_card_from_deck(playing_deck)

        # playing a round:

        #player's turn:
        plr_scores, plr_naturals, plr_wagers, surrender = players_turn(plr, dlr, playing_deck)

        # checking for surrender:
        if not surrender:
            # dealer's turn:
            dlr_score, dlr_natural = dealers_turn(dlr, plr, plr_scores, plr_naturals, playing_deck)
            # checking the outcome and adding winnings:
            check_outcome_and_add_winnings(plr, plr_scores, plr_naturals, plr_wagers, dlr_score, dlr_natural)
        else:
            # clearing the screen:
            print('\n' * 100)
            # showing dealer's cards face up:
            dlr.hand.display_face_up('Dealer')
            # showing human player's cards face up:
            plr.hand.display_face_up(plr.name)
            print('HAND SURRENDERED!')

        print('\n')
        # displaying the updated human player's chips:
        plr.display_chips('Chips')

        # cleanup after a finished round:
        plr.clear_wager()
        plr.split_hands = []

        # checking if player's got any chips, or sufficient bankroll to purchase chips:
        if plr.chips == EMPTY and plr.bankroll < 1:
            break
        else:
            # asking if player wants to play again:
            play_again = replay()

            if play_again:
                # checking if cheque change is needed:
                exchange_possible, high_value_color = plr.cheque_change_possible()

                if exchange_possible:

                    if cheque_change_requested(high_value_color):
                        plr.cheque_change(high_value_color)

                # checking if player needs more chips:
                if plr.chips == EMPTY:
                    need_more_chips = True
                elif plr.bankroll < 1:
                    need_more_chips = False
                else:
                    need_more_chips = more_chips_requested()

    #if the player has run out of both chips and bankroll, or doesn't want to replay:
    print(f"Game over! {plr.name}'s bankroll: {(plr.bankroll + plr.chips['Amount']):7.2f}")
