"""
Contains interactive functions (asking for input from player) for the blackjack surrender game
"""

def ask_players_name():
    """
    Asks player's name; if name is too long, asks to make it 14 symbols or less
    :return: player's name as a string
    """
    while True:
        players_name = input("Please enter Player's name: ")

        if len(players_name) > 14:
            print("Sorry, the name is too long! Please make it 14 characters or less")
        elif len(players_name) == 0:
            print("Sorry, I don't understand! Please try again")
        else:
            return players_name

def hit_or_stand():
    """
    Asks player to choose hit or stand
    :rtype: bool
    """
    # while loop asking for input until valid answer is entered:
    while True:
        choice = input('Please choose Hit or Stand (H/S): ').casefold()

        # checking the input:
        if choice not in ['h', 's']:
            print("Sorry, I don't understand! Please try again")
        # if choice is valid:
        elif choice == 'h':
            return True
        else:
            return False

def double_down_requested():
    """
    Asks if player wants to double down
    :rtype: bool
    """
    choice = 'None'

    # while loop asking for input until valid answer is entered:
    while choice.casefold() not in ['y', 'n']:
        choice = input('\nDo you want to double down? (Y or N): ')

        # checking the input:
        if choice.casefold() not in ['y', 'n']:
            print("Sorry, I don't understand! Please choose Y or N")

    # if choice is valid:
    return choice.casefold() == 'y'

def insurance_requested():
    """
    Asks if player wants to place an insurance bet
    :rtype: bool
    """
    choice = 'None'

    # while loop asking for input until valid answer is entered:
    while choice.casefold() not in ['y', 'n']:
        choice = input("Dealer's upcard is an ace. Do you want to place an insurance bet? (Y or N): ")

        # checking the input:
        if choice.casefold() not in ['y', 'n']:
            print("Sorry, I don't understand! Please choose Y or N")

    # if choice is valid:
    return choice.casefold() == 'y'

def split_requested():
    """
    Asks if player wants to split cards
    :rtype: bool
    """
    choice = 'None'

    # while loop asking for input until valid answer is entered:
    while choice.casefold() not in ['y', 'n']:
        choice = input('\nYou have 2 cards of same rank. Do you want to split the pair? (Y or N): ')

        # checking the input:
        if choice.casefold() not in ['y', 'n']:
            print("Sorry, I don't understand! Please choose Y or N")

    #if choice is valid:
    return choice.casefold() == 'y'

def surrender_requested():
    """
    Asks if player wants to surrender
    :rtype: bool
    """
    choice = 'None'

    # while loop asking for input until valid answer is entered:
    while choice.casefold() not in ['y', 'n']:
        choice = input("Do you want to surrender and get back half of your wager? (Y or N): ")

        # checking the input:
        if choice.casefold() not in ['y', 'n']:
            print("Sorry, I don't understand! Please choose Y or N")

    # if choice is valid:
    return choice.casefold() == 'y'

def replay():
    """
    Asks if player wants to replay
    :rtype: bool
    """
    choice = 'None'

    # while loop asking for input until valid answer is entered:
    while choice.casefold() not in ['y', 'n']:
        choice = input('Do you want to play again? (Y or N): ')

        # checking the input:
        if choice.casefold() not in ['y', 'n']:
            print("Sorry, I don't understand! Please choose Y or N")

    # if choice is valid:
    return choice.casefold() == 'y'

def more_chips_requested():
    """
    Asks if player wants to get more chips
    :rtype: bool
    """
    choice = 'None'

    # while loop asking for input until valid answer is entered:
    while choice.casefold() not in ['y', 'n']:
        choice = input('Do you want to get more chips? (Y or N): ')

        # checking the input:
        if choice.casefold() not in ['y', 'n']:
            print("Sorry, I don't understand! Please choose Y or N")

    # if choice is valid:
    return choice.casefold() == 'y'

def cheque_change_requested(color):
    """
    Asks if player wants a cheque-change
    :rtype: bool
    """
    choice = 'None'

    # determining which indefinite article to use in the question:
    if color == 'Orange':
        article = 'an'
    else:
        article = 'a'

    # while loop asking for input until valid answer is entered:
    while choice.casefold() not in ['y', 'n']:
        choice = input(f'Do you want to break {article} {color} chip into smaller-value chips? (Y or N): ')

        # checking the input:
        if choice.casefold() not in ['y', 'n']:
            print("Sorry, I don't understand! Please choose Y or N")

    # if choice is valid:
    return choice.casefold() == 'y'

def press_enter_to_continue():
    """
    Tells player to press Enter to continue
    """

    input('Press Enter to continue: ')
