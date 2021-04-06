"""
Contains Player class and HumanPlayer subclass for the blackjack surrender game
"""
from chip_funcs import display_chip_values, money_to_chips, CHIP_COLORS, CHIP_VALUES, CHIP_SYMBOLS
from card_related_classes import Hand, RESET

# "empty" dictionary containing zero chips of each color:
EMPTY = {'White': 0, 'Pink': 0, 'Red': 0, 'Green': 0, 'Orange': 0, 'Amount': 0}

# dictionary containing all possible payout coefficients:
PAYOUT_COEFFS = {'1:1': 1, '2:1': 2, '3:2': 1.5, 'Push': 0}

# dictionary containing pairs of split_hand_number attributes assigned to newly created split hands,  depending on which
# hand they come from.
# keys: split_hand_number attributes of hands being split
# values: pairs of split_hand_number attributes assigned to hands created by splitting
NEW_SPLIT_HAND_NUMBERS = {'0': ('1', '2'), '1': ('1.1', '1.2'), '2': ('2.1', '2.2')}


class Player:
    """
    An object representing a Player (both computer and human)
    """
    def __init__(self):
        """
        Constructor for instantiating a Player object
        """
        self.hand = None

    def start_hand(self):
        """
        Creates a new Hand for a player
        """
        self.hand = Hand('Normal')

class HumanPlayer(Player):
    """
    An object representing a human Player
    """

    def __init__(self, name):
        """
        Constructor for instantiating a HumanPlayer object
        :param name: player's name (str)
        """
        Player.__init__(self)
        # HumanPlayer's name:
        self.name = name
        # HumanPlayer's bankroll:
        self.bankroll = 100
        # List of HumanPlayer's split hands created by splitting pairs:
        # maximum length of the list: 6
        self.split_hands = []
        # Dictionary containing number of chips of each color in HumanPlayer's possession, and their total value:
        self.chips = {'White': 0, 'Pink': 0, 'Red': 0, 'Green': 0, 'Orange': 0, 'Amount': 0}
        # Dictionary containing all HumanPlayer's current wagers and corresponding monetary amounts::
        self.wagers = {'Main Wager': {'White': 0, 'Pink': 0, 'Red': 0, 'Green': 0, 'Orange': 0, 'Amount': 0},
                       'Insurance': {'White': 0, 'Pink': 0, 'Red': 0, 'Green': 0, 'Orange': 0, 'Amount': 0},
                       'Split Wager 1': {'White': 0, 'Pink': 0, 'Red': 0, 'Green': 0, 'Orange': 0, 'Amount': 0},
                       'Split Wager 2': {'White': 0, 'Pink': 0, 'Red': 0, 'Green': 0, 'Orange': 0, 'Amount': 0},
                       'Split Wager 3': {'White': 0, 'Pink': 0, 'Red': 0, 'Green': 0, 'Orange': 0, 'Amount': 0}}

    def start_split_hand(self, split_hand_number, split_wager_number):
        """
        Creates a split hand for HumanPlayer
        :param split_hand_number (str): number assigned to the new split hand ('1', '2', '1.1', '1.2', '2.1', '2.2')
        :param split_wager_number(int): number assigned to the corresponding Split Wager (0 for the Main Wager, 1, 2,
         or 3 for Split Wagers)
        """
        # adding the newly created Split Hand to HumanPlayer's split hand list:
        self.split_hands.append(Hand('Split Hand', split_hand_number, split_wager_number))

    def display_bankroll(self):
        """
        Displays human Player's bankroll
        """
        print(f"\n{self.name}'s bankroll: {self.bankroll:5.2f}\n")

    def display_chips(self, *args):
        """
        Displays chips in columns corresponding to HumanPlayer's "chip piles" ("chip piles" include HumanPlayer's chips
        and current wagers). Prints "No chips left!" in the corresponding column if HumanPlayer has run out of chips.
        :param '*args': the variable arguments are used for names of "chip piles" to display.
        :type arg: str
        "Chip piles" include HumanPlayer's Chips, HumanPlayer's Main Wager, HumanPlayer's Split Wagers, and
        HumanPlayers Insurance.
        Possible chip pile names: "Chips" (HumanPlayer's chips), "Main Wager", "Split Wager 1", "Split Wager 2",
        "Split Wager 3", "Insurance".
        """
        # creating two lists for "chip piles" and chip pile names to be displayed:
        displayed_chip_piles = []
        displayed_chip_pile_names = []

        for chip_pile_name in args:

            # if the "Chips" pile name is in args, "Chips" is added to the list of displayed "chip piles", regardless of
            # whether or not it is empty:
            if chip_pile_name == 'Chips':
                displayed_chip_piles.append(self.chips)
                displayed_chip_pile_names.append(chip_pile_name)
            else:
                # the wagers are added to the list of displayed "chip piles" only if they aren't empty:
                if self.wagers[chip_pile_name] != EMPTY:
                    displayed_chip_piles.append(self.wagers[chip_pile_name])
                    displayed_chip_pile_names.append(chip_pile_name)

        # printing the chip pile names at the top of each column:
        for pile_and_name in zip(displayed_chip_piles, displayed_chip_pile_names):

            # checking if the current chip pile is the HumanPlayer's "Chips" pile:
            if pile_and_name[1] == 'Chips':
                # print the HumanPlayer's "Chips" pile name regardless of whether there are any chips to display in this
                # column:
                print(f"{self.name}'s Chips:", end = '')

                # checking if HumanPlayer has run out of chips:
                if self.chips == EMPTY:
                    print (" No chips Left!", end = '')
                    # blank space up to column width:
                    space = (19 - len(self.name) - len(pile_and_name[1]) + 5) * ' '
                else:
                    # blank space up to column width:
                    space = ((34 - len(self.name) - len(pile_and_name[1]) + 5) * ' ')

            # for the rest of "chip piles" (i.e. those corresponding to wagers):
            else:
                # printing the chip pile name:
                print(f"{self.name}'s {pile_and_name[1]}:", end = '')
                # space left up to column width:
                space = (34 - len(self.name) - len(pile_and_name[1]) + 5) * ' '

            # insert blank space up to column width after each column name:
            print(space, end='')

        # go to next line:
        print('')

        # printing the chip symbols in columns corresponding to chip piles:
        # for loop over all chip colors:
        for color in CHIP_COLORS:

            # list of chips of current color left to display in each column(pile):
            chips_left_to_display = []
            # list of same length containing zeros only:
            zero_list = []

            # for loop over displayed chip piles:
            for pile in displayed_chip_piles:
                # adding the number of chips of current color in the current pile to the chips_left_to_display list:
                chips_left_to_display.append(pile[color])
                # adding a zero to the zero list:
                zero_list.append(0)

            # checking if there are any chips left to display:
            while chips_left_to_display != zero_list:

                # for loop over displayed chip piles:
                for index in range(len(displayed_chip_pile_names)):

                    # Only 30 chip symbols fit in a column. If there are more than 30 chips of any color in any pile,
                    # the remaining chip symbols (chips left to display) are carried over to next line:
                    if chips_left_to_display[index] > 30:
                        # number of chips displayed in current line:
                        displayed_chips_number = 30
                        # number of chips carried over to next line:
                        chips_left_to_display[index] -= 30
                    else:
                        # if all remaining chips fit in the column width, display them all in current line:
                        displayed_chips_number = chips_left_to_display[index]
                        # no chips are carried over to next line:
                        chips_left_to_display[index] = 0

                    # printing the chip symbols to be displayed in current line:
                    print(CHIP_SYMBOLS[color] * displayed_chips_number, end='')

                    # checking if we just finished displaying all chips of current color in current pile
                    # (and if there were any):
                    if displayed_chip_piles[index][color] > 0 and chips_left_to_display[index] == 0 and\
                            displayed_chips_number > 0:

                        # print the value corresponding to current chip color:
                        print(f' x {CHIP_VALUES[color]:5.2f}' + RESET, end='')
                        # space left up to column width:
                        space = (30 - displayed_chips_number + 5) * ' '

                    # if we have just printed 30 chip symbols and there still are chips of current color in current pile
                    # left to display:
                    elif chips_left_to_display[index] > 0:
                        # space left up to column width:
                        space = 13 * ' '
                    # if there aren't any chips of current color in current pile, or we had finished displaying them in
                    # one of previous cycles:
                    else:
                        # leave the line empty:
                        space = 43 * ' '

                    # insert the empty space up to the column width:
                    print(space, end='')
                # go to next line:
                print('')


    def get_chips(self):
        """
        Purchases chips for HumanPlayer; requires input from player
        """
        while True:
            print('\nPlease choose chips to purchase!')

            # a for loop over all chip colors and values:
            for color in CHIP_COLORS:

                # checking if there is enough money in HumanPlayer's bankroll to purchase at least 1 chip:
                if self.bankroll >= 1:

                    # checking if bankroll is sufficient to buy at least one chip of current color:
                    if CHIP_VALUES[color] <= self.bankroll:
                        # display HumanPlayer's bankroll:
                        self.display_bankroll()
                        # display all chip colors and values:
                        display_chip_values()

                        # a while loop asking for input until a valid number of chips to purchase is entered:
                        while True:

                            # asking for input and checking if it is an integer:
                            try:
                                choice = int(input(f'\nPlease enter the number of {color} chips: '))
                            except ValueError:
                                print("Sorry, I don't understand! Please try again")
                            else:

                                # checking for a negative number:
                                if choice < 0:
                                    print("Sorry, I don't understand! Please try again")
                                # checking if input exceeds the bankroll:
                                elif choice * CHIP_VALUES[color] > self.bankroll:
                                    print('Bankroll too low! Please try again')
                                else:
                                    # when input is valid:
                                    # adding the number of chips of current color entered by the player to HumanPlayer's
                                    # chip pile:
                                    self.chips[color] += choice
                                    # add the corresponding amount to the total value of HumanPlayer's chips:
                                    self.chips['Amount'] += choice * CHIP_VALUES[color]
                                    # remove the same amount from HumanPlayer's bankroll:
                                    self.bankroll -= choice * CHIP_VALUES[color]
                                    # clear screen:
                                    print('\n'*100)

                                    # checking if HumanPlayer has got any chips to display:
                                    if self.chips['Amount'] > 0:
                                        # display HumanPlayer's chips:
                                        self.display_chips('Chips')
                                    break

                # if not enough money in the bankroll to purchase at least 1 chip:
                else:
                    break

            # if no chips have been purchased:
            else:

                # checking if HumanPlayer has got any chips from previous purchases:
                if self.chips['Amount'] > 0:
                    break

            # if not enough money left in the bankroll to purchase at least 1 more chip:
            if self.bankroll < 1:
                break

        # display updated bankroll after purchasing chips:
        self.display_bankroll()

    def place_bet(self, bet):
        """
        Places a bet for HumanPlayer; requires input from player
        :param bet: specifies what kind of bet is being placed (either "Main Wager" or "Insurance")
        :type bet: str
        :return: none
        """
        if bet == 'Insurance':
            bet_name = ' Insurance'
        elif bet == 'Main Wager':
            bet_name = ''

        bet_amount = 0

        # while loop checking if bet has been placed:
        while bet_amount == 0:
            print(f'Please place your{bet_name} bet!')

            # for loop over all chip colors/values:
            for color in CHIP_COLORS:

                # checking if HumanPlayer has any chips of current color to display
                if self.chips[color] > 0:
                    # display HumanPlayer's chips:
                    self.display_chips('Chips')
                    print('\n')

                    # displaying chips in all HumanPlayer's wagers:
                    self.display_chips(*self.wagers.keys())

                    # while loop asking for input until valid number of chips of current color to bet with is received:
                    while True:

                        # asking for input and checking if it is an integer:
                        try:
                            choice = int(input(f'\nPlease enter the number of {color} chips to bet with: '))
                        except ValueError:
                            print("Sorry, I don't understand! Please try again")
                        else:

                            # checking for a negative number:
                            if choice < 0:
                                print("Sorry, I don't understand! Please try again")
                            # checking if input exceeds number of HumanPlayer's chips of current color:
                            elif choice > self.chips[color]:
                                print(f'Not enough {color} chips! Please try again')
                            # when input is a valid number of chips to bet with:
                            else:
                                # adding the number of chips of current color entered by the player to the wager:
                                self.wagers[bet][color] = choice
                                # adding the corresponding value to current bet amount:
                                bet_amount += choice * CHIP_VALUES[color]
                                # adding the same value to the wager amount:
                                self.wagers[bet]['Amount'] += choice * CHIP_VALUES[color]
                                # removing the number of chips entered by the player from HumanPlayer's chips:
                                self.chips[color] -= choice
                                # removing their value from total value of HumanPlayer's chips:
                                self.chips['Amount'] -= choice * CHIP_VALUES[color]

                                # clearing screen:
                                print('\n'*100)
                                break

                    # checking if HumanPlayer has any chips left:
                    if self.chips == EMPTY:
                        break

        # display remaining HumanPlayer's chips:
        self.display_chips('Chips')
        print('\n')
        # display chips in all HumanPlayer's wagers:
        self.display_chips(*self.wagers.keys())

    def double_wager(self, move, split_wager_number = 0, new_split_wager_number = 1):
        """
        Doubles HumanPlayer's wager for Double Down or Split
        :param move: specifies what move HumanPlayer is making (either "Double Down" or "Split")
        :param split_wager_number: number of the Split Wager corresponding to the Hand being played (0 for the Main
         Wager, 1, 2, or 3 for Split Wagers)
        :param new_split_wager_number: number assigned to new Split Wager created by Split (1, 2, or 3)
        :type move: str
        :type split_wager_number, new_split_wager_number: int
        :return: none
        """
        # Determining which wager is to be doubled or split:
        if split_wager_number == 0:
            # doubling or splitting the Main Wager:
            doubled_wager_name = 'Main Wager'
        else:
            # doubling or splitting a Split Wager:
            doubled_wager_name = f'Split Wager {split_wager_number}'

        # for loop over all chip colors/values:
        for color in CHIP_COLORS:

            # checking if HumanPlayer has at least same number of chips of current color as there are in in the wager:
            if self.chips[color] < self.wagers[doubled_wager_name][color]:
                enough_chips_of_each_color = False
                break

        # if HumanPlayer has at least same number of chips of each color as there are in the wager:
        else:
            enough_chips_of_each_color = True

        # subtracting the wager amount from total value of HumanPlayer's chips:
        self.chips['Amount'] -= self.wagers[doubled_wager_name]['Amount']

        # doubling the wager amount:
        if move == 'Double Down':
            self.wagers[doubled_wager_name]['Amount'] = self.wagers[doubled_wager_name]['Amount'] * 2
        # splitting the wager amount:
        elif move == 'Split':
            self.wagers[f'Split Wager {new_split_wager_number}']['Amount'] = self.wagers[doubled_wager_name]['Amount']

        # checking if HumanPlayer has enough chips of each color:
        if enough_chips_of_each_color:

            # for loop over all chip colors/values:
            for color in CHIP_COLORS:
                # remove the chips to be added to the wager from HumanPlayer's chip pile:
                self.chips[color] -= self.wagers[doubled_wager_name][color]

        # if there aren't enough chips of each color:
        else:
            # convert into chips the amount remaining after subtracting the wager amount from total value of
            # HumanPlayer's chips:
            self.chips = money_to_chips(self.chips['Amount'])

        # for loop over all chip colors/values:
        for color in CHIP_COLORS:

            # doubling down:
            if move == 'Double Down':
                # doubling the number of chips of each color in the main wager:
                self.wagers[doubled_wager_name][color] = 2 * self.wagers[doubled_wager_name][color]
            # splitting:
            elif move == 'Split':
                # creating a split wager containing same number of chips as the initial wager
                self.wagers[f'Split Wager {new_split_wager_number}'][color] = self.wagers[doubled_wager_name][color]

    def add_winnings(self, payout, bet):
        """
        Adds chips HumanPlayer has won to HumanPlayer's chips
        :param payout: payout on the winning wager. Possible values: "1:1", "3:2", "2:1", "Push".
        :type payout: str
        :param bet: HumanPlayer's winning wager name. Possible values: "Main Wager", "Split Wager 1", "Split Wager 2",
         "Split Wager 3", "Insurance".
        :type bet: str
        :return: none
        """
        # determining the amount won on top of the wager amount:
        # initializing the amount won as zero:
        amount_won = 0

       # for loop over all chip colors/values:
        for color in CHIP_COLORS:
            # adding the total value of chips of current color in the wager times the payout coefficient to the amount
            # won:
            amount_won += PAYOUT_COEFFS[payout] * self.wagers[bet][color] * CHIP_VALUES[color]

        # converting the amount won into chips:
        added_chips = money_to_chips(amount_won)

        # for loop over all chip colors/values:
        for color in CHIP_COLORS:
            # returning the chips from the wager to HumanPlayer's chips:
            self.chips[color] += self.wagers[bet][color]
            # adding the chips won on top of that:
            self.chips[color] += added_chips[color]

        # returning the wager amount to total value of HumanPlayer's chips:
        self.chips['Amount'] += self.wagers[bet]['Amount']
        # adding the value of the chips won on top of that:
        self.chips['Amount'] += added_chips['Amount']

    def surrender(self):
        """
        Returns half of the Main Wager to HumanPlayer's chips in case of Surrender
        :return: none
        """
        # checking if the number of chips of each color in the Main Wager is divisible by 2:
        for color in CHIP_COLORS:

            if self.wagers['Main Wager'][color] % 2 != 0:
                chips_divisible = False
                break

        else:
            chips_divisible = True

        if chips_divisible:

            # adding half the Main Wager amount to HumanPlayer's chips total value:
            self.chips['Amount'] += self.wagers['Main Wager']['Amount'] / 2
            # adding half of the chips of each color in Main Wager to HumanPlayer's chips:
            for color in CHIP_COLORS:
                self.chips[color] += self.wagers['Main Wager'][color] / 2

        else:
            # converting half of Main Wager amount into chips:
            chips_to_return = money_to_chips(self.wagers['Main Wager']['Amount'] / 2)

            # adding the result to HumanPlayer's chip pile:
            for key in self.chips:
                self.chips[key] += chips_to_return[key]


    def clear_wager(self):
        """
        Resets number of chips in all wagers and all wager amounts to zero after a finished hand
        """
        self.wagers = {'Main Wager': {'White': 0, 'Pink': 0, 'Red': 0, 'Green': 0, 'Orange': 0, 'Amount': 0},
                 'Insurance': {'White': 0, 'Pink':0, 'Red': 0, 'Green': 0, 'Orange': 0, 'Amount': 0},
                 'Split Wager 1': {'White': 0, 'Pink':0, 'Red': 0, 'Green': 0, 'Orange': 0, 'Amount': 0},
                 'Split Wager 2': {'White': 0, 'Pink':0, 'Red': 0, 'Green': 0, 'Orange': 0, 'Amount': 0},
                 'Split Wager 3': {'White': 0, 'Pink':0, 'Red': 0, 'Green': 0, 'Orange': 0, 'Amount': 0}}

    def cheque_change_possible(self):
        """
        Checks if HumanPlayer has any high-value chips (Orange or Green) that can be exchanged
        :return: tuple containing a boolean showing if there are any high value chips, and the color of
        the highest-value chip
        :rtype: bool, str
        """
        for color in ['Orange', 'Green']:

            if self.chips[color] > 0:
                return True, color

        return False, 'None'

    def cheque_change(self, color):
        """
        Breaks one highest-value (Orange or Green) chip in HumanPlayer's chip pile into 10 smaller-value (Red or Purple)
        chips and displays the result; requires input from player to approve of the exchange
        :param color: color of HumanPlayer's highest-value chip
        :return: none
        """
        # removing the high-value chip from HumanPlayer's chip pile:
        self.chips[color] -= 1

        # determining the color of 10 times smaller value chips:
        if color == 'Orange':
            new_color = 'Red'
        elif color == 'Green':
            new_color = 'Pink'

        # displaying the rest of HumanPlayer's chips:
        print('\n' * 100)
        self.display_chips('Chips')
        # displaying one high-value chip and 10 smaller-value chips it can be exchanged to:
        print(f"\nand {self.name}'s chip to exchange:")
        print(f'{CHIP_SYMBOLS[color]} x {CHIP_VALUES[color]:5.2f}' + RESET + '  =  ' +
              f'{CHIP_SYMBOLS[new_color]}' * 10 + f' x {CHIP_VALUES[new_color]:5.2f}\n' + RESET)

        choice = 'None'

        # while loop asking if player approves of the exchange until answer is valid:
        while choice.casefold() not in ['y', 'n']:
            choice = input('Do you approve of this exchange? (Y or N): ')

            # checking if input value is valid:
            if choice.casefold() not in ['y', 'n']:
                print("Sorry, I don't understand! Please choose Y or N")

        # determining if exchange is approved:
        approved = choice.casefold() == 'y'

        if approved:
            # adding 10 smaller-value chips to HumanPlayer's chip pile:
            self.chips[new_color] += 10
        else:
            # returning the high-value chip to HumanPlayer's chip pile:
            self.chips[color] += 1

        # displaying the result:
        print('\n' * 100)
        self.display_chips('Chips')
