import random
import math
from colors import colors
from msvcrt import getch

# tuple containing all chip colors:
chip_colors = ('Orange', 'Green', 'Red', 'Pink', 'White')

# dictionary containing chip values:
chip_values = {'White': 1, 'Pink': 2.5, 'Red': 5, 'Green': 25, 'Orange': 50}

#"empty" dictionary containing zero chips of each color:
empty = {'White': 0, 'Pink': 0, 'Red': 0, 'Green': 0, 'Orange': 0}

# dictionary containing chip symbols (letters 'O' of corresponding color, black letter 'O'  for a 'White' chip):
chip_symbols = {'White': colors.fg.black + 'O', 'Pink': colors.fg.pink + 'O', 'Red': colors.fg.red + 'O',
                'Green': colors.fg.green + 'O', 'Orange': colors.fg.orange + 'O'}

# tuples containing all card suits and ranks:
suits = ('♥', '♦', '♣', '♠')
ranks = ('2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A')

# dictionary containing card values depending on rank:
card_values = {'2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, '10': 10, 'J': 10, 'Q': 10, 'K': 10,
               'A': 11}

# dictionary containing line-by-line card image printing patterns:
patterns = {'top': ' ____ ', 'upper': '|    |', 'left': '| ', 'left_10': '|', 'right': ' |', 'bottom': '|____|',
            'space': ' '}
# dictionary containing line-by-line face-down card image printing patterns:
display_face_down = {1: ' ____ ', 2: '|////|', 3: '|////|', 4: '|̲/̲/̲/̲/|'}


class Chip:
    """
    An object representing a casino chip
    """

    def __init__(self, color):
        """
        Constructor for instantiating a Chip object
        """
        self.color = color
        self.value = chip_values[color]

    def __str__(self):
        """
        Represents a Chip as a symbol
        """
        return chip_symbols[self.color]


def display_chip_values():
    """
    Displays all chip colors and corresponding values
    """
    print('\nChip colors and values:')

    for color in chip_colors:
        print(f'{chip_symbols[color]} {color:<6} {chip_values[color]:>19.2f}')


class Card:
    """
    An object representing a French-suited playing card
    """

    def __init__(self, suit, rank):
        """
        Constructor for instantiating a Card object
        """
        self.suit = suit
        self.rank = rank
        self.value = card_values[rank]
        self.color = None

    def __str__(self):
        """
        Represents a Card object as a string
        """
        return f'{self.rank}{self.suit}'

    def display_patterns(self):
        """
        Returns a dictionary of patterns for line-by-line printing  of an image of a card
        """
        if self.suit in ['♣', '♠']:
            self.color = colors.fg.black
        else:
            self.color = colors.fg.red

        if self.rank == '10':
            left_border = patterns['left_10']
        else:
            left_border = patterns['left']

        return {1: (colors.fg.black + patterns['top'] + patterns['space']),
                2: (colors.fg.black + patterns['upper'] + patterns['space']),
                3: (colors.fg.black + left_border + self.color + self.__str__() + colors.fg.black +
                    patterns['right'] + patterns['space']),
                4: (colors.fg.black + patterns['bottom'] + patterns['space'])}


class Deck:
    """
    An object representing a 52-card deck
    """

    def __init__(self):
        """
        Constructor for instantiating a Deck object
        """
        self.deck_cards = []

        for suit in suits:

            for rank in ranks:
                self.deck_cards.append(Card(suit, rank))

    def shuffle(self):
        """
        Shuffles the Deck
        """
        random.shuffle(self.deck_cards)

    def deal_one(self):
        """
        Deals one Card from the Deck
        :return: a Card object
        """
        return self.deck_cards.pop()


class Hand:
    """
    An object representing a Blackjack hand
    """

    def __init__(self, hand_type, split_hand_number=None):
        """
        Constructor for instantiating a Hand object
        :param hand_type: "Normal" or "Split Hand"
        :param split_hand_number: number of a split hand (if hand_type == "Split"), None (if hand_type == "Normal")
        possible number of split hands: up to 6
        """
        self.type = hand_type
        self.split_hand_number = split_hand_number
        self.cards = []
        self.score = 0

    def add_card_from_deck(self, deck):
        """
        A method for hitting cards and adding them to Hand
        """
        new_card = deck.deal_one()
        self.cards.append(new_card)
        self.score += new_card.value

        # changing the Ace value from 11 to 1:
        if self.score > 21:

            for card in self.cards:

                if card.value == 11:
                    card.value = 1
                    self.score -= 10
                    break

    def display_face_up(self, players_name):
        """
        Displays cards in Hand face up
        """
        if self.type == 'Normal':
            print(f"\n\n{players_name}'s Cards:")
        else:
            print(f"\n\n{players_name}'s {self.type} {self.split_hand_number}:")

        for key in range(1, 5):
            pattern = ''

            for card in self.cards:
                pattern += card.display_patterns()[key]
            print(pattern)

    def display_one_face_down(self, player):
        """
        Displays two cards in Hand with one card face up and another card face down
        """
        print(f"\n\n{player}'s Cards:")

        for key in range(1, 5):
            print(self.cards[0].display_patterns()[key] + display_face_down[key])
            
    def split_pair(self):
        """
        Splits a two-card Hand into two Cards and returns them
        :return: tuple containing two Card objects
        """
        #checking if there are two cards in Hand:
        if len(self.cards) == 2:
            
            split_card1 = self.cards.pop()
            split_card2 = self.cards.pop()
            self.score = 0
            return split_card1, split_card2
        
        else:
            raise ValueError('Incorrect number of cards in Hand. Only a two-card Hand can be split')

    def add_card_from_split(self, split_card):
        """
        Adds a Card object returned by the split_pair(self) method to Hand
        :param split_card: a Card object
        """
        self.cards.append(split_card)

        #checking if the card added from split is an Ace:
        if split_card.rank == 'A':
            #an Ace initially counts as 11:
            self.score += 11
        else:
            self.score += split_card.value


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


def money_to_chips(amount_to_convert):
    """
    A function to convert money into chips
    :param amount_to_convert: monetary amount to be exchanged for chips
    :returns: tuple (updated amount (remainder not convertible into chips discarded), dictionary
    containing the number of chips of each color)
    """
    if amount_to_convert < 0:
        raise ValueError('Amount to convert should be greater than zero')

    chips = {'White': 0, 'Pink': 0, 'Red': 0, 'Green': 0, 'Orange': 0}
    chips_total = 0
    updated_amount = amount_to_convert

    fract_part = math.modf(amount_to_convert)[0]

    if fract_part == 0.25 or fract_part == 0.75:
        discarded_amount = 0.25
        updated_amount -= discarded_amount
        amount_to_convert = updated_amount
        fract_part -= discarded_amount


    if fract_part == 0.5 and amount_to_convert >= 2.5:
        chips['Pink'] += 1
        chips_total += 2.5
        amount_to_convert -= 2.5

    for color in ('Orange', 'Green', 'Red', 'White'):
        chips_added = int(amount_to_convert / chip_values[color])
        chips[color] += chips_added
        chips_total += chips_added * chip_values[color]
        amount_to_convert -= chips_added * chip_values[color]

    updated_amount -= amount_to_convert
    return updated_amount, chips


class HumanPlayer(Player):
    """
    An object representing a human Player
    """

    def __init__(self, name):
        """
        Constructor for instantiating a HumanPlayer object
        """
        Player.__init__(self)
        #HumanPlayer's name:
        self.name = name
        #HumanPlayer's bankroll:
        self.bankroll = 100
        #List of HumanPlayer's split hands created by splitting pairs:
        #maximum number of split hands: 6
        self.split_hands = []
        #Dictionary containing number of chips of each color in HumanPlayer's possession:
        self.chips = {'White': 0, 'Pink': 0, 'Red': 0, 'Green': 0, 'Orange': 0}
        #Dictionary containing number of chips of each color in current HumanPlayer's wager:
        self.wager = {'White': 0, 'Pink': 0, 'Red': 0, 'Green': 0, 'Orange': 0}
        #Dictionary containing number of chips of each color in current HumanPlayer's Insurance wager:
        self.insurance = {'White': 0, 'Pink': 0, 'Red': 0, 'Green': 0, 'Orange': 0}
        #List containing HumanPlayer's split wagers:
        self.split_wagers = []
        #Total value of HumanPlayer's chips:
        self.chips_total = 0
        #Current wager amount:
        self.wager_amount = 0
        # Current Insurance wager amount:
        self.insurance_amount = 0
        # List of current split wager amounts:
        self.split_wager_amounts = []

    def start_split_hand(self, split_hand_number):
        """
        Creates the First split hand for HumanPlayer
        :param split_hand_number: number of the split hand (from 1 to 6)
        """
        self.split_hands.append(Hand('Split Hand', split_hand_number))

    def display_bankroll(self):
        """
        Displays human Player's bankroll
        """
        print(f"\n{self.name}'s bankroll: {self.bankroll:5.2f}\n")

    def display_chips(self, *args):
        """
        Displays chips in columns corresponding to HumanPlayer's "chip piles". Prints "No chips left!" in the
        corresponding column if the "chip pile" of remaining HumanPlayer's chips is empty.
        :param '*args': the variable arguments are used for names of "chip piles" to display.
        :type arg: str
        "Chip piles" include HumanPlayer's Chips, HumanPlayer's Main Wager, HumanPlayer's Split Wager, and
        HumanPlayers Insurance.
        Possible chip pile names: "Chips" (HumanPlayer's chips), "Main Wager", "Split Wager", "Insurance".
        """
        #tuple containing names of chip piles to display:
        chip_pile_names = args
        #list of chip piles:
        chip_piles = []
        nonempty_chip_pile_names = []

        for chip_pile_name in chip_pile_names:

            if chip_pile_name == 'Main Wager':
                pile = self.wager
            elif chip_pile_name == 'Insurance':
                pile = self.insurance
            elif chip_pile_name[:-2] == 'Split Wager':

                if len(self.split_wagers) >= int(chip_pile_name[-1]):
                    pile = self.wager
                else:
                    pile = {'White': 0, 'Pink': 0, 'Red': 0, 'Green': 0, 'Orange': 0}

            elif chip_pile_name == 'Chips':
                pile = self.chips

            #adding HumanPlayer's Chips and other (non-empty) chip piles to the list of chip piles:
            if chip_pile_name == 'Chips' or pile != empty:
                chip_piles.append(pile)
                nonempty_chip_pile_names.append(chip_pile_name)

        #printing the chip pile names at the top of each column:
        for pile_and_name in zip(chip_piles, nonempty_chip_pile_names):

            #checking if the current chip pile is the HumanPlayer's Chips pile:
            if pile_and_name[1] == 'Chips':
                #print the HumanPlayer's Chips pile name regardless of whether there are any chips to display in this
                #pile:
                print(f"{self.name}'s Chips:", end = '')

                #checking if HumanPlayer has run out of chips:
                if self.chips == empty:
                    print (" No chips Left!", end = '')
                    # blank space up to column width:
                    space = (39 - len(self.name) - len(pile_and_name[1]) + 5) * ' '
                else:
                    #blank space up to column width:
                    space = ((54 - len(self.name) - len(pile_and_name[1]) + 5) * ' ')

            #for the rest of chip piles:
            else:
                #printing the chip pile name:
                print(f"{self.name}'s {pile_and_name[1]}:", end = '')
                #space left up to column width:
                space = (54 - len(self.name) - len(pile_and_name[1]) + 5) * ' '

            #insert blank space up to column width after each column name:
            print(space, end='')

        #go to next line:
        print('')

        #printing the chip symbols in columns corresponding to chip piles:
        for color in chip_colors:

            #list of chips of current color left to display in each column(pile):
            chips_left_to_display = []
            #list of same length containing zeros only:
            zero_list = []

            for pile in chip_piles:
                    #adding the number of chips of current color in the current pile to the list of chips of current
                    #color left to display
                    chips_left_to_display.append(pile[color])
                    #adding a zero to the list containing zeros only:
                    zero_list.append(0)

            #checking if there are any chips left to display:
            while chips_left_to_display != zero_list:

                #for loop over chip piles:
                for index in range(len(nonempty_chip_pile_names)):

                    #Only 50 chip symbols fit in a column. If there are more than 50 chips of any color in any pile,
                    #the remaining chip symbols (chips left to display) are carried over to next line
                    if chips_left_to_display[index] > 50:
                        #number of chips displayed in current line
                        displayed_chips_number = 50
                        #number of chips carried over to next line
                        chips_left_to_display[index] -= 50
                    else:
                        displayed_chips_number = chips_left_to_display[index]
                        chips_left_to_display[index] = 0

                    #printing the chip symbols to be displayed in current line:
                    print(chip_symbols[color] * displayed_chips_number, end='')

                    #checking if we just finished displaying all chips of current color in current pile
                    #(and if there were any):
                    if chip_piles[index][color] > 0 and chips_left_to_display[index] == 0 and\
                            displayed_chips_number > 0:

                        #print the value corresponding to current chip color:
                        print(f' x {chip_values[color]:5.2f}' + colors.fg.black, end='')
                        #space left up to column width:
                        space = (50 - displayed_chips_number + 5) * ' '

                    #if we have just printed 50 chip symbols and there still are chips of current color in current pile
                    #left to display:
                    elif chips_left_to_display[index] > 0:
                        space = 13 * ' '
                    #if there aren't any chips of current color in current pile, or we had finished displaying them in
                    #one of previous cycles:
                    else:
                        space = 63 * ' '

                    print(space, end='')
                #go to next line:
                print('')


    def get_chips(self):
        """
        Purchases chips for HumanPlayer; requires input from player
        """
        while True:
            print('\nPlease choose chips to purchase!')

            #a for loop over all chip colors and values:
            for color in chip_colors:

                #checking if there is enough money in HumanPlayer's bankroll to purchase at least 1 chip:
                if self.bankroll >= 1:

                    #checking if bankroll is sufficient to buy at least one chip of current color:
                    if chip_values[color] <= self.bankroll:
                        #display HumanPlayer's bankroll:
                        self.display_bankroll()
                        #display all chip colors and values:
                        display_chip_values()

                        #a while loop asking for input until a valid number of chips to purchase is entered:
                        while True:

                            #asking for input and checking if it is an integer:
                            try:
                                choice = int(input(f'\nPlease enter the number of {color} chips: '))
                            except ValueError:
                                print("Sorry, I don't understand! Please try again")
                            else:

                                #checking if input is a negative number:
                                if choice < 0:
                                    print("Sorry, I don't understand! Please try again")
                                #checking if input exceeds the bankroll:
                                elif choice * chip_values[color] > self.bankroll:
                                    print('Bankroll too low! Please try again')
                                else:
                                    #when input is valid:
                                    self.chips[color] += choice
                                    self.chips_total += choice * chip_values[color]
                                    self.bankroll -= choice * chip_values[color]
                                    print('\n'*100)

                                    #checking if HumanPlayer has got any chips to display:
                                    if self.chips_total > 0:
                                        self.display_chips('Chips')
                                    break

                # not enough money in the bankroll to purchase at least 1 chip
                else:
                    break

            #no chips have been purchased
            else:

                #checking if HumanPlayer has got any chips from previous purchases:
                if self.chips_total > 0:
                    break

            # not enough money in the bankroll to purchase at least 1 chip
            if self.bankroll < 1:
                break

        #display bankroll after purchasing chips:
        self.display_bankroll()

    def place_bet(self, bet):
        """
        Places a bet for HumanPlayer; requires input from player
        :param bet: specifies what kind of bet is being placed (either "Main Wager" or "Insurance")
        :type bet: str
        """
        if bet == 'Insurance':
            bet_type = ' Insurance'
        elif bet == 'Main Wager':
            bet_type = ''

        bet_amount = 0

        #while loop checking if there are any chips in the wager
        while bet_amount == 0:
            print(f'Please place your{bet_type} bet!')

            #for loop over all chip colors/values:
            for color in chip_colors:

                #checking if HumanPlayer has any chips of current color to display
                if self.chips[color] > 0:
                    self.display_chips('Chips')
                    print('\n')

                    #displaying chips in all HumanPlayer's wagers:
                    self.display_chips('Main Wager', 'Split Wager', 'Insurance')

                    #while loop asking for input until valid number of chips of current color to bet with is received:
                    while True:

                        #asking for input and checking if it is an integer:
                        try:
                            choice = int(input(f'\nPlease enter the number of {color} chips to bet with: '))
                        except ValueError:
                            print("Sorry, I don't understand! Please try again")
                        else:

                            #checking if input is a negative number:
                            if choice < 0:
                                print("Sorry, I don't understand! Please try again")
                            #checking if input exceeds number of HumanPlayer's chips of current color:
                            elif choice > self.chips[color]:
                                print(f'Not enough {color} chips! Please try again')
                            #when input is a valid number of chips to bet with:
                            else:

                                if bet == 'Main Wager':
                                    #adding the number of chips of current color entered by the player to main wager:
                                    self.wager[color] = choice
                                    #adding the corresponding value to current bet amount:
                                    bet_amount += self.wager[color]* chip_values[color]
                                    # adding the same value to main wager amount:
                                    self.wager_amount += self.wager[color]* chip_values[color]
                                    #removing the number of chips entered by the player from HumanPlayer's chips:
                                    self.chips[color] -= self.wager[color]
                                    #removing their value from total value of HumanPlayer's chips:
                                    self.chips_total -= self.wager[color] * chip_values[color]
                                elif bet == 'Insurance':
                                    # adding the number of chips of current color entered by the player to insurance
                                    # wager:
                                    self.insurance[color] = choice
                                    # adding the corresponding value to current bet amount:
                                    bet_amount += self.insurance[color] * chip_values[color]
                                    # adding the same value to insurance amount:
                                    self.insurance_amount += self.insurance[color] * chip_values[color]
                                    # removing the number of chips entered by the player from HumanPlayer's chips:
                                    self.chips[color] -= self.insurance[color]
                                    # removing their value from total value of HumanPlayer's chips:
                                    self.chips_total -= self.insurance[color] * chip_values[color]
                                #clearing screen:
                                print('\n'*100)
                                break

                    #checking if HumanPlayer has any chips left:
                    if self.chips == empty:
                        break

        #display remaining HumanPlayer's chips:
        self.display_chips('Chips')
        print('\n')
        #display chips in all HumanPlayer's wagers:
        self.display_chips('Main Wager', 'Split Wager', 'Insurance')

    def double_wager(self, move):
        """
        Doubles HumanPlayer's wager for Double Down or Split
        :param move: specifies what move HumanPlayer is making (either "Double Down" or "Split")
        :type move: str
        """
        #for loop over all chip colors/values:
        for color in chip_colors:

            #checking if HumanPlayer has at least same number of chips of current color as there are in in the wager:
            if self.chips[color] < self.wager[color]:
                enough_chips_of_each_color = False
                break

        #if HumanPlayer has at least same number of chips of each color as there are in the wager:
        else:
            enough_chips_of_each_color = True

        #subtracting additional wager amount from total value of HumanPlayer's chips:
        self.chips_total -= self.wager_amount

        #Doubling down:
        if move == 'Double Down':
            #doubling the Main Wager:
            self.wager_amount = self.wager_amount * 2
        #Splitting:
        if move == 'Split':
            self.split_wager_amounts.append(self.wager_amount)
            #creating an empty dictionary for the new split wager:
            new_wager = {}

        #checking if HumanPlayer has enough chips of each color:
        if enough_chips_of_each_color:

            #for loop ovewr all chip colors/values:
            for color in chip_colors:
                #remove the chips to be added to the wager from HumanPlayer's chip pile:
                self.chips[color] -= self.wager[color]

        #if there aren't enough chips of each color:
        else:
            #convert into chips the amount remaining after subtracting the wager amount from total value of
            #HumanPlayer's chips:
            self.chips_total, self.chips = money_to_chips(self.chips_total)

        #for loop over all chip colors/values:
        for color in chip_colors:

            #doubling down:
            if move == 'Double Down':
                #doubling the number of chips in the main wager
                self.wager[color] = self.wager[color] * 2
            #splitting:
            elif move == 'Split':
                #creating a split wager containing same number of chips as main wager
                new_wager[color] = self.wager[color]

        if move == 'Split':
            #adding the new wager to the list of split wagers
            self.split_wagers.append(new_wager)

        return self.wager_amount, self.wager, self.chips_total, self.chips, self.split_wager_amounts, self.split_wagers

    def add_winnings(self, payout, bet):
        """
        Adds chips HumanPlayer has won to Player's pile
        :param payout: payout on the winning wager. Possible values: "1:1", "3:2", "2:1", "Tie".
        :type payout: str
        :param bet: HumanPlayer's winning wager name. Possible values: "Main Wager", "Split Wager", "Insurance".
        :type bet: str

        """
        #determining the payout coefficient depending on payout type:
        if payout == '1:1':
            payout_coeff = 1
        elif payout == '3:2':
            payout_coeff = 1.5
        elif payout == 'Tie':
            payout_coeff = 0
        elif payout == '2:1':
            payout_coeff = 2

        #determining the wager amount and number of chips of each color in the wager by the wager name:
        if bet == 'Main Wager' or bet == 'Split Wager':
            wager = self.wager
            wager_amount = self.wager_amount
        elif bet == 'Insurance':
            wager = self.insurance
            wager_amount = self.insurance_amount

        #determining the amount won on top of the wager amount:
        #initializing the amount won as zero:
        amount_won = 0

       #for loop over all chip colors/values:
        for color in chip_colors:
            #adding the total value of chips of current color in the wager times the payout coefficient to the amount
            #won:
            amount_won += payout_coeff * wager[color] * chip_values[color]

        #converting the amount won into chips:
        added_amount, added_chips = money_to_chips(amount_won)

        #for loop over all chip colors/values:
        for color in chip_colors:
            #returning the chips from the wager to HumanPlayer's chips:
            self.chips[color] += wager[color]
            #adding the chips won on top of that:
            self.chips[color] += added_chips[color]

        #returning the wager amount to total value of HumanPlayer's chips:
        self.chips_total += wager_amount
        #adding the value of the chips won on top of that:
        self.chips_total += added_amount

        return self.chips_total, self.chips


    def clear_wager(self):
        """
        Resets number of chips in all wagers and all wager amounts to zero after a finished hand
        """
        self.wager = {'White': 0, 'Pink': 0, 'Red': 0, 'Green': 0, 'Orange': 0}
        self.wager_amount = 0
        self.split_wagers = []
        self.split_wager_amounts = []
        self.insurance = {'White': 0, 'Pink': 0, 'Red': 0, 'Green': 0, 'Orange': 0}
        self.insurance_amount = 0

    def cheque_change_possible(self):
        """
        Checks if Player has any high-value chips (Orange or Green) that can be exchanged
        :return: tuple (boolean showing if there are any high value chips, color of the highest-value chip as a string)
        """
        for color in ['Orange', 'Green']:

            if self.chips[color] > 0:
                return True, color

        else:
            return False, 'None'

    def cheque_change(self, color):
        """
        Breaks one highest-value (Orange or Green) chip in HumanPlayer's chip pile into 10 smaller-value (Red or Purple)
        chips and displays the result; requires input from player to approve of the exchange
        :param color: color of HumanPlayer's highest-value chip
        """
        #removing the high-value chip from HumanPlayer's chip pile:
        self.chips[color] -= 1

        #determining the color of 10 times smaller value chips:
        if color == 'Orange':
            new_color = 'Red'
        elif color == 'Green':
            new_color = 'Pink'

        # displaying the rest of HumanPlayer's chips:
        print('\n' * 100)
        self.display_chips('Chips')
        #displaying one high-value chip and 10 smaller-value chips it can be exchanged to:
        print(f"\nand {self.name}'s chip to exchange:")
        print(f'{chip_symbols[color]} ✕ {chip_values[color]:5.2f}  =  ' + f'{chip_symbols[new_color]}'*10 +
              f' ✕ {chip_values[new_color]:5.2f}\n' + colors.fg.black)

        choice = 'None'
        
        #while loop asking if player approves of the exchange until answer is valid:
        while choice.casefold() not in ['y', 'n']:
            choice = input(f'Do you approve of this exchange? (Y or N): ')
            
            #checking if input value is valid:
            if choice.casefold() not in ['y', 'n']:
                print("Sorry, I don't understand! Please choose Y or N")

        #determining if exchange is approved:
        if choice.casefold() == 'y':
            approved = True
        else:
            approved = False

        if approved:
            #adding 10 smaller-value chips to HumanPlayer's chip pile:
            self.chips[new_color] += 10
        else:
            #returning the high-value chip to HumanPlayer's chip pile:
            self.chips[color] += 1

        #displaying the result:
        print('\n' * 100)
        self.display_chips('Chips')


#functions interacting with player:

def ask_players_name():
    """
    Asks player's name; if name is too long, asks to make it 43 symbols or less
    :return: player's name as a string
    """
    while True:
        name = input("Please enter Player's name: ")

        if len(name) > 34:
            print("Sorry, the name is too long! Please make it 34 characters or less")
        else:
            return name


def hit_or_stand():
    """
    Asks player to choose hit or stand
    :rtype: bool
    """
    while True:
        choice = input('Please choose Hit or Stand (H/S): ').casefold()

        if choice not in ['h', 's']:
            print("Sorry, I don't understand! Please try again")
        elif choice == 'h':
            return True
        else:
            return False

def ready_to_play(action):
    """
    Asks if player is ready to play or continue playing
    :param action: either 'Play' or 'Continue'
    :type action: str
    :rtype: bool
    """
    choice_ready = 'None'

    #determining the question to ask player
    if action == 'Play':
        question = 'play?'
    elif action == 'Continue':
        question = 'continue?'

    #while loop asking for input until valid answer is entered:
    while choice_ready.casefold() != 'y':
        choice_ready = input(f'Are you ready to {question} (Y or N): ')

        #checking if input is a valid answer:
        if choice_ready.casefold() not in ['y', 'n']:
            print("Sorry, I don't understand! Please choose Y or N")
        #checking whether player has chosen 'y' or 'n':
        elif choice_ready.casefold() == 'y':
            return True
        else:
            #if player has chosen 'n', ask if player wants to finish the game:
            choice_finish = 'None'

            # while loop asking for input until valid answer is entered:
            while choice_finish.casefold() not in ['y', 'n']:
                choice_finish = input('Do you want to finish the game? (Y or N): ')

                # checking if input is a valid answer:
                if choice_finish.casefold() not in ['y', 'n']:
                    print("Sorry, I don't understand! Please choose Y or N")

            # checking whether player has chosen 'y' or 'n':
            if choice_finish.casefold() == 'y':
                return False
            else:
                # if player has chosen 'n', start a new cycle of the enclosing while
                # loop:
                continue


def double_down_requested():
    """
    Asks if player wants to double down
    :rtype: bool
    """
    choice = 'None'

    while choice.casefold() not in ['y', 'n']:
        choice = input('Do you want to double down? (Y or N): ')

        if choice.casefold() not in ['y', 'n']:
            print("Sorry, I don't understand! Please choose Y or N")

    if choice.casefold() == 'y':
        return True
    else:
        return False

def insurance_requested():
    """
    Asks if player wants to place an insurance bet
    :rtype: bool
    """
    choice = 'None'

    while choice.casefold() not in ['y', 'n']:
        choice = input("Dealer's upcard is an ace. Do you want to place an insurance bet? (Y or N): ")

        if choice.casefold() not in ['y', 'n']:
            print("Sorry, I don't understand! Please choose Y or N")

    if choice.casefold() == 'y':
        return True
    else:
        return False

def split_requested():
    """
    Asks if player wants to split cards
    :rtype: bool
    """
    choice = 'None'

    while choice.casefold() not in ['y', 'n']:
        choice = input('You have 2 cards of same rank. Do you want to split the pair? (Y or N): ')

        if choice.casefold() not in ['y', 'n']:
            print("Sorry, I don't understand! Please choose Y or N")

    if choice.casefold() == 'y':
        return True
    else:
        return False

def replay():
    """
    Asks if player wants to replay
    :rtype: bool
    """
    choice = 'None'

    while choice.casefold() not in ['y', 'n']:
        choice = input('Do you want to play again? (Y or N): ')

        if choice.casefold() not in ['y', 'n']:
            print("Sorry, I don't understand! Please choose Y or N")

    if choice.casefold() == 'y':
        return True
    else:
        return False

def more_chips_requested():
    """
    Asks if player wants to get more chips
    :rtype: bool
    """
    choice = 'None'

    while choice.casefold() not in ['y', 'n']:
        choice = input('Do you want to get more chips? (Y or N): ')

        if choice.casefold() not in ['y', 'n']:
            print("Sorry, I don't understand! Please choose Y or N")

    if choice.casefold() == 'y':
        return True
    else:
        return False

def cheque_change_requested(color):
    """
    Asks if player wants a cheque-change
    :rtype: bool
    """
    choice = 'None'

    if color == 'Orange':
        article = 'an'
    else:
        article = 'a'

    while choice.casefold() not in ['y', 'n']:
        choice = input(f'Do you want to break {article} {color} chip into smaller-value chips? (Y or N): ')

        if choice.casefold() not in ['y', 'n']:
            print("Sorry, I don't understand! Please choose Y or N")

    if choice.casefold() == 'y':
        return True
    else:
        return False


if __name__ == '__main__':

    #game setup:
    print('Welcome to the Blackjack Game!')
    name = ask_players_name()
    player = HumanPlayer(name)
    dealer = Player()

    play_again = True
    need_more_chips = True
    first_round = True

    #game cycle:
    while play_again:

        #preparing to play a new hand:
        if need_more_chips:

            if not first_round and player.chips_total == 0:
                print('\n'*100)
                print(f'\n{player.name} has no chips left!')
            else:
                print('\n'*100)

            player.get_chips()
            first_round = False
            ready = ready_to_play('Play')
        else:
            ready = True

        #shuffling the deck and placing a bet
        if ready:
            print('\n'*100)
            print('New round!')
            deck = Deck()
            deck.shuffle()
            player.place_bet('Main Wager')

            #creating a "Normal" Hand object for player:
            player.start_hand()

            #creating a "Normal" Hand object for dealer:
            dealer.start_hand()

            #dealing initial 2 cards to both player and dealer and displaying the cards
            player.hand.add_card_from_deck(deck)
            dealer.hand.add_card_from_deck(deck)

            player.hand.add_card_from_deck(deck)
            dealer.hand.add_card_from_deck(deck)

            dealer.hand.display_one_face_down('Dealer')
            player.hand.display_face_up(f'{player.name}')

            #game logic
            #natural Blackjack in player's hand:
            if player.hand.score == 21:
                print('\nBLACKJACK!')

                #clearing screeen and displaying all cards face up:
                print('\n' * 100)
                dealer.hand.display_face_up('Dealer')
                player.hand.display_face_up(f'{player.name}')

                #indicating that player has a Blackjack:
                print('\nBLACKJACK!')

                #checking if dealer has a natural Blackjack too:
                if dealer.hand.score == 21:
                    print('\nBut Dealer has a Blackjack too!')
                    print('TIE!')
                    player.add_winnings('Tie', 'Main Wager')

                #when dealer doesn't have a Blackjack:
                else:
                    print(f'\n{player.name} has won!')
                    player.add_winnings('3:2', 'Main Wager')
            else:
                #player's turn:
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
                        #doubling down:
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
                        print('\n'*100)
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
                            #player is allowed to hit only once after doubling down
                            hit = False

                    else:
                        pass

                else:

                    #dealer's turn
                    #offer Insurance bet to player if dealer's upcard is an Ace and player has any chips left:
                    if dealer.hand.cards[0].rank == 'A' and player.chips_total > 0 and insurance_requested():
                        print('\n')
                        player.place_bet('Insurance')
                        insurance_placed = True
                        ready = ready_to_play('Continue')
                    else:
                        insurance_placed = False
                        ready = True

                    if ready:
                        print('\n'*100)
                        dealer.hand.display_face_up('Dealer')
                        player.hand.display_face_up(f'{player.name}')
                    else:
                        break

                    # checking if dealer has a natural blackjack:
                    if dealer.hand.score == 21:
                        print('\nDEALER HAS A BLACKJACK!')
                        print('House has won!')

                        #checking if an Insurance bet has been placed:
                        if insurance_placed:
                            print('\nYour Insurance bet has won!')
                            #adding winnings on the Insurance bet:
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
                            print('\n'*100)
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


        else:
            break

        #cleanup after a finished hand:
        player.clear_wager()

        #checking if player's got any chips, or sufficient bankroll to purchase chips:
        player.display_chips('Chips')

        if player.chips_total == 0 and player.bankroll < 1:
            break
        else:
            #asking if player wants to play again
            play_again = replay()

            if play_again:
                #checking if cheque change is needed
                exchange_possible, high_value_color = player.cheque_change_possible()

                if exchange_possible:

                    if cheque_change_requested(high_value_color):
                        player.cheque_change(high_value_color)

                #checking if player needs more chips
                if player.chips_total == 0:
                    need_more_chips = True
                elif player.bankroll < 1:
                    need_more_chips = False
                else:
                    need_more_chips = more_chips_requested()

    #print(player.wager_amount)
    #print(player.wager)
    print(player.bankroll)
    print(player.chips_total)
    print(f"Game over! {player.name}'s bankroll: {(player.bankroll + player.chips_total):7.2f}")
