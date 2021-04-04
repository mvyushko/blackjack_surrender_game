"""
Text version of the 52-card Blackjack Late Surrender game for one human Player, and a computer Dealer.
Allows Splits, Doubling Down, Insurance and Surrender.
Dealer stands on soft 17. Blackjack pays 3:2.
To display cards, uses rectangles constructed of pipe operators and underscores.
To display chips, uses colored capital O letters.
"""

import random
import math
import sys

#checking the platform:
if sys.platform.startswith('win'):
    #when running in Windows, use colorama for colored output:
    from colorama import init
    init()
    from colorama import Fore, Back, Style
    #colors for output formatting:
    pink = Fore.LIGHTMAGENTA_EX
    red = Fore.LIGHTRED_EX
    green = Fore.GREEN
    orange = Back.YELLOW + Fore.RED
    reset = Style.RESET_ALL

else:
    #use the colors module:
    from colors import colors
    #colors for output formatting:
    pink = colors.fg.pink
    red = colors.fg.red
    green = colors.fg.green
    orange = colors.fg.orange
    reset = colors.reset

# tuple containing all chip colors:
chip_colors = ('Orange', 'Green', 'Red', 'Pink', 'White')

# dictionary containing chip values:
chip_values = {'White': 1, 'Pink': 2.5, 'Red': 5, 'Green': 25, 'Orange': 50}

#"empty" dictionary containing zero chips of each color:
empty = {'White': 0, 'Pink': 0, 'Red': 0, 'Green': 0, 'Orange': 0, 'Amount': 0}

# dictionary containing chip symbols (letters 'O' of corresponding color, black letter 'O'  for a 'White' chip):
chip_symbols = {'White': reset + 'O', 'Pink': pink + 'O', 'Red': red + 'O',
                'Green': green + 'O', 'Orange': orange + 'O'}

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
display_face_down = {1: ' ____ ', 2: '|____|', 3: '|____|', 4: '|____|'}

#dictionary containing all possible payout coefficients:
payout_coeffs = {'1:1': 1, '2:1': 2, '3:2': 1.5, 'Tie': 0}

#dictionary containing pairs of split_hand_number attributes assigned to newly created split hands,  depending on which
#hand they come from.
#keys: split_hand_number attributes of hands being split
#values: pairs of split_hand_number attributes assigned to hands created by splitting
new_split_hand_numbers = {'0': ('1', '2'), '1': ('1.1', '1.2'), '2': ('2.1', '2.2')}


def display_chip_values():
    """
    Displays all chip colors and corresponding monetary values
    """
    print('\nChip colors and values:')

    for color in chip_colors:
        print(f'{chip_symbols[color]} {color:<6} {chip_values[color]:>19.2f}' + reset)


class Card:
    """
    An object representing a French-suited playing card
    """

    def __init__(self, suit, rank):
        """
        Constructor for instantiating a Card object
        :param suit (str): French card suit (possible values: '♣', '♠', '♥', or '♦')
        :param rank (str): rank of the Card ((possible values: 'A', '2', '3',..., '10', 'J', 'Q', 'K'))
        """
        self.suit = suit
        self.rank = rank
        #Blackjack value of the Card (int):
        self.value = card_values[rank]

        #color used for displaying the Card:
        #black card suits use default color:
        if self.suit in ['♣', '♠']:
            self.color = reset
        #red card suits use red:
        else:
            self.color = red

    def __str__(self):
        """
        Represents a Card object as a string
        """
        return f'{self.rank}{self.suit}'

    def display_patterns(self):
        """
        Returns a dictionary of patterns for line-by-line displaying  of an image of a card, using the patterns
        dictionary:
        """
        #'10' is the only two-symbol card rank. it needs a special 'left_10' pattern on the left (with no space
        #between the left border of the card image and the card symbol)
        if self.rank == '10':
            left_border = patterns['left_10']
        else:
            left_border = patterns['left']

        #build the line-by-line representation of the card image from items of the "patterns" dictionary,
        # and colored string representation of the card:
        return {1: (reset + patterns['top'] + patterns['space']),
                2: (reset + patterns['upper'] + patterns['space']),
                3: (reset + left_border + self.color + self.__str__() + reset +
                    patterns['right'] + patterns['space']),
                4: (reset + patterns['bottom'] + patterns['space'])}


class Deck:
    """
    An object representing a 52-card deck
    """

    def __init__(self):
        """
        Constructor for instantiating a Deck object
        """
        #list of Card objects in the Deck:
        self.deck_cards = []

        #adding 1 Card object of each suit and each rank to the list of Cards:/';mnj
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

    def __init__(self, hand_type='Normal', split_hand_number='0', split_wager_number=0):
        """
        Constructor for instantiating a Hand object
        :param hand_type (str): type of the Hand (either "Normal" or "Split Hand")
        :param split_hand_number (str): number of a split hand. Possible values: '1', '2', '1.1', '1.2', '2.1', or '2.2'
        (if hand_type == "Split Hand"), '0' (if hand_type == "Normal")
        :param split_wager_number (int): number of the split wager corresponding to the Hand. Possible values: 0 (for
         the Main Wager), 1, 2, or 3.
        """
        self.type = hand_type
        self.split_hand_number = split_hand_number
        #list of Cards in the Hand:
        self.cards = []
        #total Blackjack value of the Hand:
        self.score = 0
        #number of corresponding split wager (0 for the Main Wager):
        self.split_wager_number = split_wager_number

    def add_card_from_deck(self, deck):
        """
        A method for taking cards from Deck and adding them to Hand
        :parameter deck: a Deck object
        """
        #taking a Card from Deck:
        new_card = deck.deal_one()
        #adding the Card to Hand:
        self.cards.append(new_card)
        #adding the Card value to the score:
        self.score += new_card.value

        # changing the Ace value from 11 to 1 and adjusting the score:
        if self.score > 21:

            for card in self.cards:

                if card.value == 11:
                    card.value = 1
                    self.score -= 10
                    break

    def display_face_up(self, players_name):
        """
        Displays all cards in Hand face up
        """
        #if there are no split hands, display the Hand as "player's cards":
        if self.type == 'Normal':
            print(f"\n\n{players_name}'s Cards:")
        #if there are split hands, specify the split hand number and corresponding wager:
        else:

            #if the Hand corresponds to Main Wager:
            if self.split_wager_number == 0:
                print(f"\n\n{players_name}'s {self.type} {self.split_hand_number} (Main Wager):")
            #if the hand corresponds to one of Split Wagers, specify the Split Wager number:
            else:
                print(f"\n\n{players_name}'s {self.type} {self.split_hand_number}"
                  f" (Split Wager {self.split_wager_number}):")

        #displaying all cards in Hand, from left to right, line-by-line:
        #for loop over line numbers from 1 to 4:
        for line_number in range(1, 5):
            #current line of the line-by-line image:
            pattern = ''

            #assembling the current line from corresponding lines of line-by-line images of each card:
            for card in self.cards:
                pattern += card.display_patterns()[line_number]
            #printing the resulting line:
            print(pattern)

    def display_one_face_down(self, player):
        """
        Displays two cards in Hand with one card face up and another card face down
        """
        if len(self.cards) != 2:
            raise ValueError('Incorrect number of cards in the Hand. Only a two-card Hand can be displayed one face'
                             ' down.')

        print(f"\n\n{player}'s Cards:")

        #for loop over line numbers from 1 to 4:
        for line_number in range(1, 5):
            #displaying the line assembled from corresponding line of the first card line-by-line image, and
            #corresponding line of the "card face down" line-by-line image
            print(self.cards[0].display_patterns()[line_number] + display_face_down[line_number])
            
    def split_pair(self):
        """
        Splits a two-card Hand into two Cards and returns them
        :return: tuple containing two Card objects
        """
        #checking if there are two cards in Hand:
        if len(self.cards) == 2:
            
            #removing both cards from Hand:
            split_card1 = self.cards.pop()
            split_card2 = self.cards.pop()
            #setting the Hand score to zero:
            self.score = 0
            #returning the two Cards:
            return split_card1, split_card2
        
        else:
            raise ValueError('Incorrect number of cards in Hand. Only a two-card Hand can be split')

    def add_card_from_split(self, split_card):
        """
        Adds a Card object obtained by splitting a pair to Hand
        :param split_card: a Card object
        """
        #checking if the card added from split is an Ace:
        if split_card.rank == 'A':
            #an Ace initially counts as 11:
            split_card.value = 11
            #adjusting the Hand score:
            self.score += 11
        else:
            #adding the card value to the Hand score:
            self.score += split_card.value

        #adding the Card to the list of Cards in Hand:
        self.cards.append(split_card)

    def play_for_dealer(self, deck):
        """
        Plays a Hand for Dealer. Adds cards from Deck until score hits soft 17 or more.
        :parameter deck: a Deck object
        :returns:  a tuple containing Dealer's final score, and a boolean showing if Dealer has a natural Blackjack
        :rtype: self.score: int, natural: bool
        """
        #checking for a Natural Blackjack:
        if self.score == 21:
            natural = True
        else:
            natural = False
            #adding Cards from Deck until the score of soft 17:
            while self.score < 17:
                self.add_card_from_deck(deck)

        return self.score, natural

def surrender_offered(hand, dealer_upcard):
    """
    Determines whether or not to offer Surrender, depending on the Hand score and Dealer's upcard
    :param hand: player's Hand
    :param dealer_upcard: rank of Dealer's upcard
    :rtype: bool
    """
    if hand.score in [14, 15, 16]:

        #checking if Dealer's upcard is a 10 or an Ace:
        if dealer_upcard in ['10', 'J', 'Q', 'K', 'A']:
            return True
        else:
            return False

    else:
        return False


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
    :return: dictionary containing the number of chips of each color and their total value ('Amount'))
    """
    #checking if amount to convert is non-negative:
    if amount_to_convert < 0:
        raise ValueError('Amount to convert should be greater than zero')

    #initializing the dictionary containing the number of chips of each color and their total value ('Amount')
    chips = {'White': 0, 'Pink': 0, 'Red': 0, 'Green': 0, 'Orange': 0, 'Amount': 0}

    #fractional part of the amount to convert:
    fract_part = math.modf(amount_to_convert)[0]

    #rounding quarter-integer amounts down to half-integers:
    if fract_part == 0.25 or fract_part == 0.75:
        discarded_amount = 0.25
        amount_to_convert -= discarded_amount
        fract_part -= discarded_amount

    #use a Pink chip to get rid of half-integer values:
    if fract_part == 0.5 and amount_to_convert >= 2.5:
        chips['Pink'] += 1
        chips['Amount'] += 2.5
        amount_to_convert -= 2.5

    #converting the remaining (integer) amount into integer-value chips:
    #for loop over all chip colors except Pink (because Pink has a half-integer value, 2.50):
    for color in ('Orange', 'Green', 'Red', 'White'):
        # divide the amount to convert by the value corresponding to current chip color and take the integer part:
        chips_added = int(amount_to_convert / chip_values[color])
        # add corresponding number of chips of current color to the chips dictionary:
        chips[color] += chips_added
        # add corresponding amount to the chips total value ("Amount"):
        chips['Amount'] += chips_added * chip_values[color]
        # and remove it from the amount to convert:
        amount_to_convert -= chips_added * chip_values[color]

    return chips


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
        #maximum length of the list: 6
        self.split_hands = []
        #Dictionary containing number of chips of each color in HumanPlayer's possession, and their total value:
        self.chips = {'White': 0, 'Pink': 0, 'Red': 0, 'Green': 0, 'Orange': 0, 'Amount': 0}
        #Dictionary containing all HumanPlayer's current wagers and corresponding monetary amounts::
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
        #adding the newly created Split Hand to HumanPlayer's split hand list:
        self.split_hands.append(Hand('Split Hand', split_hand_number, split_wager_number))

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
        "Chip piles" include HumanPlayer's Chips, HumanPlayer's Main Wager, HumanPlayer's Split Wagers, and
        HumanPlayers Insurance.
        Possible chip pile names: "Chips" (HumanPlayer's chips), "Main Wager", "Split Wager 1", "Split Wager 2",
        "Split Wager 3", "Insurance".
        """
        #initializing the lists of "chip piles" and chip pile names to be displayed:
        displayed_chip_piles = []
        displayed_chip_pile_names = []

        for chip_pile_name in args:

            #if the "Chips" pile name is in args, "Chips" is added to the list of displayed "chip piles", regardless of
            #whether or not it is empty:
            if chip_pile_name == 'Chips':
                displayed_chip_piles.append(self.chips)
                displayed_chip_pile_names.append(chip_pile_name)
            else:
                #the wagers are added to the list of displayed "chip piles" only if they aren't empty:
                if self.wagers[chip_pile_name] != empty:
                    displayed_chip_piles.append(self.wagers[chip_pile_name])
                    displayed_chip_pile_names.append(chip_pile_name)

        #printing the chip pile names at the top of each column:
        for pile_and_name in zip(displayed_chip_piles, displayed_chip_pile_names):

            #checking if the current chip pile is the HumanPlayer's "Chips" pile:
            if pile_and_name[1] == 'Chips':
                #print the HumanPlayer's "Chips" pile name regardless of whether there are any chips to display in this
                #column:
                print(f"{self.name}'s Chips:", end = '')

                #checking if HumanPlayer has run out of chips:
                if self.chips == empty:
                    print (" No chips Left!", end = '')
                    #blank space up to column width:
                    space = (19 - len(self.name) - len(pile_and_name[1]) + 5) * ' '
                else:
                    #blank space up to column width:
                    space = ((34 - len(self.name) - len(pile_and_name[1]) + 5) * ' ')

            #for the wager "Chip Piles":
            else:
                #printing the chip pile name:
                print(f"{self.name}'s {pile_and_name[1]}:", end = '')
                #space left up to column width:
                space = (34 - len(self.name) - len(pile_and_name[1]) + 5) * ' '

            #insert blank space up to column width after each column name:
            print(space, end='')

        #go to next line:
        print('')

        #printing the chip symbols in columns corresponding to chip piles:
        #for loop over all chip colors:
        for color in chip_colors:

            #list of chips of current color left to display in each column(pile):
            chips_left_to_display = []
            #list of same length containing zeros only:
            zero_list = []

            #for loop over displayed chip piles:
            for pile in displayed_chip_piles:
                    #adding the number of chips of current color in the current pile to the chips_left_to_display list:
                    chips_left_to_display.append(pile[color])
                    #adding a zero to the zero list:
                    zero_list.append(0)

            #checking if there are any chips left to display:
            while chips_left_to_display != zero_list:

                #for loop over displayed chip piles:
                for index in range(len(displayed_chip_pile_names)):

                    #Only 30 chip symbols fit in a column. If there are more than 30 chips of any color in any pile,
                    #the remaining chip symbols (chips left to display) are carried over to next line
                    if chips_left_to_display[index] > 30:
                        #number of chips displayed in current line
                        displayed_chips_number = 30
                        #number of chips carried over to next line
                        chips_left_to_display[index] -= 30
                    else:
                        #if all remaining chips fit in the column width, display them all in current line:
                        displayed_chips_number = chips_left_to_display[index]
                        #no chips are carried over to next line:
                        chips_left_to_display[index] = 0

                    #printing the chip symbols to be displayed in current line:
                    print(chip_symbols[color] * displayed_chips_number, end='')

                    #checking if we just finished displaying all chips of current color in current pile
                    #(and if there were any):
                    if displayed_chip_piles[index][color] > 0 and chips_left_to_display[index] == 0 and\
                            displayed_chips_number > 0:

                        #print the value corresponding to current chip color:
                        print(f' x {chip_values[color]:5.2f}' + reset, end='')
                        #space left up to column width:
                        space = (30 - displayed_chips_number + 5) * ' '

                    #if we have just printed 30 chip symbols and there still are chips of current color in current pile
                    #left to display:
                    elif chips_left_to_display[index] > 0:
                        #space left up to column width:
                        space = 13 * ' '
                    #if there aren't any chips of current color in current pile, or we had finished displaying them in
                    #one of previous cycles:
                    else:
                        #leave the line empty:
                        space = 43 * ' '

                    #insert the empty space up to the column width:
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

                                #checking for a negative number:
                                if choice < 0:
                                    print("Sorry, I don't understand! Please try again")
                                #checking if input exceeds the bankroll:
                                elif choice * chip_values[color] > self.bankroll:
                                    print('Bankroll too low! Please try again')
                                else:
                                    #when input is valid:
                                    #adding the number of chips of current color entered by the player to HumanPlayer's
                                    #chip pile:
                                    self.chips[color] += choice
                                    #add the corresponding amount to the total value of HumanPlayer's chips:
                                    self.chips['Amount'] += choice * chip_values[color]
                                    #remove the same amount from HumanPlayer's bankroll:
                                    self.bankroll -= choice * chip_values[color]
                                    #clear screen:
                                    print('\n'*100)

                                    #checking if HumanPlayer has got any chips to display:
                                    if self.chips['Amount'] > 0:
                                        #display HumanPlayer's chips:
                                        self.display_chips('Chips')
                                    break

                #if not enough money in the bankroll to purchase at least 1 chip:
                else:
                    break

            #if no chips have been purchased:
            else:

                #checking if HumanPlayer has got any chips from previous purchases:
                if self.chips['Amount'] > 0:
                    break

            #if not enough money left in the bankroll to purchase at least 1 more chip:
            if self.bankroll < 1:
                break

        #display updated bankroll after purchasing chips:
        self.display_bankroll()

    def place_bet(self, bet):
        """
        Places a bet for HumanPlayer; requires input from player
        :param bet: specifies what kind of bet is being placed (either "Main Wager" or "Insurance")
        :type bet: str
        """
        if bet == 'Insurance':
            bet_name = ' Insurance'
        elif bet == 'Main Wager':
            bet_name = ''

        bet_amount = 0

        #while loop checking if bet has been placed:
        while bet_amount == 0:
            print(f'Please place your{bet_name} bet!')

            #for loop over all chip colors/values:
            for color in chip_colors:

                #checking if HumanPlayer has any chips of current color to display
                if self.chips[color] > 0:
                    #display HumanPlayer's chips:
                    self.display_chips('Chips')
                    print('\n')

                    #displaying chips in all HumanPlayer's wagers:
                    self.display_chips(*self.wagers.keys())

                    #while loop asking for input until valid number of chips of current color to bet with is received:
                    while True:

                        #asking for input and checking if it is an integer:
                        try:
                            choice = int(input(f'\nPlease enter the number of {color} chips to bet with: '))
                        except ValueError:
                            print("Sorry, I don't understand! Please try again")
                        else:

                            #checking for a negative number:
                            if choice < 0:
                                print("Sorry, I don't understand! Please try again")
                            #checking if input exceeds number of HumanPlayer's chips of current color:
                            elif choice > self.chips[color]:
                                print(f'Not enough {color} chips! Please try again')
                            #when input is a valid number of chips to bet with:
                            else:
                                #adding the number of chips of current color entered by the player to the wager:
                                self.wagers[bet][color] = choice
                                #adding the corresponding value to current bet amount:
                                bet_amount += choice * chip_values[color]
                                # adding the same value to the wager amount:
                                self.wagers[bet]['Amount'] += choice * chip_values[color]
                                #removing the number of chips entered by the player from HumanPlayer's chips:
                                self.chips[color] -= choice
                                #removing their value from total value of HumanPlayer's chips:
                                self.chips['Amount'] -= choice * chip_values[color]

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
        :return: a tuple containing the updated HumanPlayer's wagers dictionary (self.wagers) and updated HumanPlayer's
         chips dictionary (self.chips)
         :rtype: self.wagers(dict), self.chips(dict)
        """
        #Determining which wager is to be doubled or split:
        if split_wager_number == 0:
            #doubling or splitting the Main Wager:
            doubled_wager_name = 'Main Wager'
        else:
            # doubling or splitting a Split Wager:
            doubled_wager_name = f'Split Wager {split_wager_number}'

        #for loop over all chip colors/values:
        for color in chip_colors:

            #checking if HumanPlayer has at least same number of chips of current color as there are in in the wager:
            if self.chips[color] < self.wagers[doubled_wager_name][color]:
                enough_chips_of_each_color = False
                break

        #if HumanPlayer has at least same number of chips of each color as there are in the wager:
        else:
            enough_chips_of_each_color = True

        #subtracting the wager amount from total value of HumanPlayer's chips:
        self.chips['Amount'] -= self.wagers[doubled_wager_name]['Amount']

        #doubling the wager amount:
        if move == 'Double Down':
            self.wagers[doubled_wager_name]['Amount'] = self.wagers[doubled_wager_name]['Amount'] * 2
        #splitting the wager amount:
        elif move == 'Split':
            self.wagers[f'Split Wager {new_split_wager_number}']['Amount'] = self.wagers[doubled_wager_name]['Amount']

        #checking if HumanPlayer has enough chips of each color:
        if enough_chips_of_each_color:

            #for loop over all chip colors/values:
            for color in chip_colors:
                #remove the chips to be added to the wager from HumanPlayer's chip pile:
                self.chips[color] -= self.wagers[doubled_wager_name][color]

        #if there aren't enough chips of each color:
        else:
            #convert into chips the amount remaining after subtracting the wager amount from total value of
            #HumanPlayer's chips:
            self.chips = money_to_chips(self.chips['Amount'])

        #for loop over all chip colors/values:
        for color in chip_colors:

            #doubling down:
            if move == 'Double Down':
                #doubling the number of chips of each color in the main wager:
                self.wagers[doubled_wager_name][color] = 2 * self.wagers[doubled_wager_name][color]
            #splitting:
            elif move == 'Split':
                #creating a split wager containing same number of chips as the initial wager
                self.wagers[f'Split Wager {new_split_wager_number}'][color] = self.wagers[doubled_wager_name][color]

        return self.wagers, self.chips

    def add_winnings(self, payout, bet):
        """
        Adds chips HumanPlayer has won to Player's pile
        :param payout: payout on the winning wager. Possible values: "1:1", "3:2", "2:1", "Tie".
        :type payout: str
        :param bet: HumanPlayer's winning wager name. Possible values: "Main Wager", "Split Wager 1", "Split Wager 2",
         "Split Wager 3", "Insurance".
        :type bet: str
        :return: the updated self.chips dictionary
        :rtype: dict
        """
        #determining the amount won on top of the wager amount:
        #initializing the amount won as zero:
        amount_won = 0

       #for loop over all chip colors/values:
        for color in chip_colors:
            #adding the total value of chips of current color in the wager times the payout coefficient to the amount
            #won:
            amount_won += payout_coeffs[payout] * self.wagers[bet][color] * chip_values[color]

        #converting the amount won into chips:
        added_chips = money_to_chips(amount_won)

        #for loop over all chip colors/values:
        for color in chip_colors:
            #returning the chips from the wager to HumanPlayer's chips:
            self.chips[color] += self.wagers[bet][color]
            #adding the chips won on top of that:
            self.chips[color] += added_chips[color]

        #returning the wager amount to total value of HumanPlayer's chips:
        self.chips['Amount'] += self.wagers[bet]['Amount']
        #adding the value of the chips won on top of that:
        self.chips['Amount'] += added_chips['Amount']

        return self.chips

    def surrender(self):
        """
        Returns half of the Main Wager to HumanPlayer's chip pile in case of Surrender
        :return: none
        """
        #checking if ne number of chips of each color in the Main Wager is divisible by 2:
        for color in chip_colors:

            if self.wagers['Main Wager'][color] % 2 != 0:
                chips_divisible = False
                break

        else:
            chips_divisible = True

        if chips_divisible:

            # adding half the Main Wager amount to HumanPlayer's chips total value:
            self.chips['Amount'] += self.wagers['Main Wager']['Amount'] / 2
            #adding half of the chips of each color in Main Wager to HumanPlayer's chips:
            for color in chip_colors:
                self.chips[color] += self.wagers['Main Wager'][color] / 2

        else:
            #converting half of Main Wager amount into chips:
            chips_to_return = money_to_chips(self.wagers['Main Wager']['Amount'] / 2)

            #adding the result to HumanPlayer's chip pile:
            for key in self.chips.keys():
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
        Checks if Player has any high-value chips (Orange or Green) that can be exchanged
        :return: tuple containing a boolean showing if there are any high value chips, and the color of
        the highest-value chip
        :rtype: bool, str
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
              f' ✕ {chip_values[new_color]:5.2f}\n' + reset)

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
    Asks player's name; if name is too long, asks to make it 14 symbols or less
    :return: player's name as a string
    """
    while True:
        name = input("Please enter Player's name: ")

        if len(name) > 14:
            print("Sorry, the name is too long! Please make it 14 characters or less")
        elif len(name) == 0:
            print("Sorry, I don't understand! Please try again")
        else:
            return name

def hit_or_stand():
    """
    Asks player to choose hit or stand
    :rtype: bool
    """
    # while loop asking for input until valid answer is entered:
    while True:
        choice = input('Please choose Hit or Stand (H/S): ').casefold()

        #checking the input:
        if choice not in ['h', 's']:
            print("Sorry, I don't understand! Please try again")
        #if choice is valid:
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

        #checking the input:
        if choice.casefold() not in ['y', 'n']:
            print("Sorry, I don't understand! Please choose Y or N")

    #if choice is valid:
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

    # while loop asking for input until valid answer is entered:
    while choice.casefold() not in ['y', 'n']:
        choice = input("Dealer's upcard is an ace. Do you want to place an insurance bet? (Y or N): ")

        # checking the input:
        if choice.casefold() not in ['y', 'n']:
            print("Sorry, I don't understand! Please choose Y or N")

    # if choice is valid:
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

    # while loop asking for input until valid answer is entered:
    while choice.casefold() not in ['y', 'n']:
        choice = input('\nYou have 2 cards of same rank. Do you want to split the pair? (Y or N): ')

        # checking the input:
        if choice.casefold() not in ['y', 'n']:
            print("Sorry, I don't understand! Please choose Y or N")

    #if choice is valid:
    if choice.casefold() == 'y':
        return True
    else:
        return False

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

    # while loop asking for input until valid answer is entered:
    while choice.casefold() not in ['y', 'n']:
        choice = input('Do you want to play again? (Y or N): ')

        #checking the input:
        if choice.casefold() not in ['y', 'n']:
            print("Sorry, I don't understand! Please choose Y or N")

    # if choice is valid:
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

    # while loop asking for input until valid answer is entered:
    while choice.casefold() not in ['y', 'n']:
        choice = input('Do you want to get more chips? (Y or N): ')

        #checking the input:
        if choice.casefold() not in ['y', 'n']:
            print("Sorry, I don't understand! Please choose Y or N")

    # if choice is valid:
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

    #determining which indefinite article to use in the question:
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
    if choice.casefold() == 'y':
        return True
    else:
        return False


def press_enter_to_continue():
    """
    Tells player to press Enter to continue
    """

    input('Press Enter to continue: ')


#gameplay functions:
def players_turn(player, dealer, deck):
    """
    Plays a Hand (and all Split Hands created by splitting it) for the human player. Requires input from player.
    :param player: a HumanPlayer object representing the human player.
    :param dealer: a Player object representing the computer Dealer.
    :param deck: a Deck object representing a 52-card French-suited deck.
    :return: a tuple containing 3 lists and a boolean: a list of integers representing final scores of all hands played;
     a list of booleans showing if there was a Natural Blackjack for each hand played; a list of names of
    corresponding wagers for each hand played; and a boolean showing if surrender has been requested.
    """
    #creating the list of all human player's Blackjack hands left to play:
    hand_list = [player.hand]
    #variable score_list will be used to store the list of final scores of all hands played:
    score_list = []
    #variable natural_list will be used to store the list of booleans showing if there was a Natural Blackjack for each
    #hand played:
    natural_list = []
    # variable natural_list will be used to store the list of names of corresponding wagers for each hand played:
    wager_list = []
    #variable sr_requested will be used to store the boolean showing whether or not surrender is requested
    sr_requested = False

    #while loop checking if there are any hands left to play:
    while len(hand_list) > 0:
        #removing a hand to be played from the list:
        hand = hand_list.pop(0)

        #clearing the screen:
        print('\n' * 100)
        #showing dealer's cards one face up, one face down:
        dealer.hand.display_one_face_down('Dealer')
        #showing human player's cards face up:
        hand.display_face_up(player.name)

        #determining which wager corresponds to the hand being played:
        if hand.split_wager_number == 0:
            wager_name = 'Main Wager'
        else:
            wager_name = f'Split Wager {hand.split_wager_number}'

        #checking for the natural Blackjack:
        if hand.score == 21:
            natural = True
            print('\nBLACKJACK!')
            press_enter_to_continue()
        else:
            natural = False

            #checking if surrender is possible on this hand:
            if hand.type == 'Normal' and dealer.hand.score != 21 and player.wagers[wager_name]['Amount'] > 1:

                #checking if player has been dealt a 14, 15, 16, or 17:
                if surrender_offered(hand, dealer.hand.cards[0].rank):
                    sr_requested = surrender_requested()

                    if sr_requested:
                        player.surrender()
                        break

            #checking if splitting is allowed for this hand:
            if hand.type == 'Normal' or hand.split_hand_number in ['1', '2']:

                #checking if there is a pair of same-rank cards and if human player has enough chips for a split:
                if hand.cards[0].rank == hand.cards[1].rank and player.chips['Amount'] >= \
                        player.wagers[wager_name]['Amount']:

                    #displaying all human player's chips and wagers:
                    print('\n')
                    player.display_chips('Chips')
                    print('\n')
                    player.display_chips(*player.wagers.keys())

                    #asking if human player wants to split the pair:
                    if split_requested():

                        #splitting:
                        #determining the new split wager numbers:
                        if hand.type == 'Normal':
                            new_split_wager_numbers = (0, 1)
                        elif hand.type == 'Split Hand' and hand.split_hand_number == '1':
                            new_split_wager_numbers = (0, 2)
                        elif hand.type == 'Split Hand' and hand.split_hand_number == '2':

                            if len(player.split_hands) == 2:
                                new_split_wager_numbers = (1, 2)
                            elif len(player.split_hands) == 4:
                                new_split_wager_numbers = (1, 3)

                        #splitting the wager:
                        player.double_wager('Split', *new_split_wager_numbers)
                        #creating two new split hands:
                        player.start_split_hand(new_split_hand_numbers[hand.split_hand_number][0],
                                                new_split_wager_numbers[0])
                        player.start_split_hand(new_split_hand_numbers[hand.split_hand_number][1],
                                                new_split_wager_numbers[1])
                        #splitting the pair:
                        split_card1, split_card2 = hand.split_pair()

                        #adding one of the split cards to each split hand:
                        player.split_hands[-2].add_card_from_split(split_card1)
                        player.split_hands[-1].add_card_from_split(split_card2)

                        #adding one card from deck to each split hand:
                        player.split_hands[-2].add_card_from_deck(deck)
                        player.split_hands[-1].add_card_from_deck(deck)
                        hand_list = [player.split_hands[-2], player.split_hands[-1]] + hand_list
                        #clearing the screen:
                        print('\n' * 100)
                        #displaying the updated human player's chips and wagers:
                        player.display_chips('Chips')
                        print('\n')
                        player.display_chips(*player.wagers.keys())
                        #asking the player to press enter to continue:
                        press_enter_to_continue()
                        continue

        #checking if doubling down is possible:
        if hand.score in [10, 11] and player.chips['Amount'] >= player.wagers[wager_name]['Amount']:
            #clearing the screen:
            print('\n' * 100)
            # showing dealer's cards one face up, one face down:
            dealer.hand.display_one_face_down('Dealer')
            # showing human player's cards face up:
            hand.display_face_up(player.name)
            print('\n')
            #displaying all human player's chips and wagers:
            player.display_chips('Chips')
            print('\n')
            player.display_chips(*player.wagers.keys())
            #asking if human player wants to double down:
            dd_requested = double_down_requested()

            #doubling down:
            if dd_requested:
                #doubling the wager:
                player.double_wager('Double Down', hand.split_wager_number)
                #clearing the screen:
                print('\n' * 100)
                #displaying the updated human player's chips and wagers:
                player.display_chips('Chips')
                print('\n')
                player.display_chips(*player.wagers.keys())
                #asking human player to press enter to continue:
                press_enter_to_continue()
                #clearing the screen:
                print('\n' * 100)
                # showing dealer's cards one face up, one face down:
                dealer.hand.display_one_face_down('Dealer')
                # showing human player's cards face up:
                hand.display_face_up(player.name)

        #doubling down not possible:
        else:
            dd_requested = False

        #checking if human player has split a pair of Aces:
        if hand.type == 'Split Hand' and hand.cards[0].rank == 'A':
            #the player is only allowed to draw one card on each split Ace:
            print("\nYou can't take any more cards to this hand (split Aces)")
            hit = False
            #asking human player to press enter to continue:
            press_enter_to_continue()
        #in all other cases, player is allowed to draw at least one more card:
        else:
            hit = True

        #while loop checking if the hand score is still less than 21, and human player is allowed and willing to hit one
        #more card:
        while hand.score < 21 and hit:
            #asking human player to choose hit or stand:
            hit = hit_or_stand()
            #hitting:
            if hit:
                #adding one card from deck to the hand:
                hand.add_card_from_deck(deck)
                #clearing the screen:
                print('\n' * 100)
                # showing dealer's cards one face up, one face down:
                dealer.hand.display_one_face_down('Dealer')
                # showing human player's cards face up:
                hand.display_face_up(player.name)

                #checking if there was a double down:
                if dd_requested and hand.score < 21:
                    ##the player is only allowed to draw one card after doubling down:
                    print("\nYou can't take any more cards to this hand (Double Down)")
                    hit = False
                    # asking human player to press enter to continue:
                    press_enter_to_continue()

                #checking for a bust:
                if hand.score > 21:
                    print('\nBUST!')
                    # asking human player to press enter to continue:
                    press_enter_to_continue()
                #checking for a 21:
                elif hand.score == 21:
                    print('\n'
                          'YOU HAVE A 21!')
                    # asking human player to press enter to continue:
                    press_enter_to_continue()

        #adding the final hand score to the score list:
        score_list.append(hand.score)
        #adding the boolean showing whether there was a natural Blackjack to the natural list:
        natural_list.append(natural)
        #adding the name of corresponding wager to the wager list:
        wager_list.append(wager_name)

    #after all hands have been played, return the score list and the natural list:
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
    #the initial dealer's Hand score:
    dlr_score = dealer.hand.score
    #checking if Dealer has a Blackjack:
    dlr_natural = dealer.hand.score == 21

    #checking if human player has played any hands without both a bust or a Natural Blackjack:
    for score, natural in zip(player_score_list, player_natural_list):

        if score <= 21 and not natural:
            insurance_possible = True
            break

    else:
        insurance_possible = False

    if insurance_possible:

        #checking if Dealer's upcard is an Ace and if human player has any chips left::
        if dealer.hand.cards[0].rank == 'A' and player.chips['Amount'] > 0:
            print('\n' * 100)
            # showing dealer's cards one face up, one face down:
            dealer.hand.display_one_face_down('Dealer')
            #showing human player's cards face up:

            #if there are no split hands:
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

            #asking if human player wants to place an Insurance bet:
            if insurance_requested():
                #placing the Insurance bet:
                print('\n')
                player.place_bet('Insurance')
                #clearing the screen:
                print('\n' * 100)
                # displaying the updated human player's chips and wagers:
                player.display_chips('Chips')
                print('\n')
                player.display_chips(*player.wagers.keys())
                # asking human player to press enter to continue:
                press_enter_to_continue()


        #playing Dealer's hand up to soft 17:
        dlr_score, dlr_natural = dealer.hand.play_for_dealer(deck)

    #clearing the screen:
    print('\n' * 100)
    # showing dealer's cards face up:
    dealer.hand.display_face_up('Dealer')
    # showing human player's cards face up:

    # if there are no split hands:
    if len(player.split_hands) == 0:
        player.hand.display_face_up(player.name)
    else:

        #showing all non-empty Split Hands:
        for hand in player.split_hands:

            if hand.score > 0:
                hand.display_face_up(player.name)

    print('\n')
    #returning Dealer's final score and a boolean showing if Dealer has a Blackjack:
    return dlr_score, dlr_natural

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

    #if there was no split and just one hand has been played:
    if len(player_score_list) == 1:

        #checking for human player's Blackjack:
        if player_natural_list[0] == True:

            #checking for Dealer's Blackjack:
            if dealer_natural == False:
                print (f'{player.name} has won 3:2!')
                player.add_winnings('3:2', 'Main Wager')
            else:
                print ('Dealer has a Blackjack too! TIE!')
                player.add_winnings('Tie', 'Main Wager')

        # checking for a bust:
        elif player_score_list[0] > 21:
            print('BUST! House has won!')
        #checking for Dealer's Blackjack:
        elif dealer_natural == True:
            print('Dealer has a Blackjack! House has won!')

            #checking if an Insurance bet has been placed:
            if player.wagers['Insurance'] != empty:
                print (f"{player.name}'s Insurance bet has won!")
                player.add_winnings('2:1', 'Insurance')

        #checking for a Dealer bust:
        elif dealer_score > 21:
            print (f'DEALER BUST! {player.name} has won!')
            player.add_winnings('1:1', 'Main Wager')
        #checking if human player's score is greater than dealer's score:
        elif player_score_list[0] > dealer_score:
            print(f'{player.name} has won!')
            player.add_winnings('1:1', 'Main Wager')
        #checking for a tie:
        elif player_score_list[0] == dealer_score:
            print('TIE!')
            player.add_winnings('Tie', 'Main Wager')
        #checking if dealer's score is greater than human player's score:
        elif player_score_list[0] < dealer_score:
            print('House has won!')

    #more than 1 hand has been played:
    else:

        if dealer_natural == True:
            print('Dealer has a Blackjack!')

            # checking if an Insurance bet has been placed:
            if player.wagers['Insurance'] != empty:
                print(f"{player.name}'s Insurance bet has won!")
                player.add_winnings('2:1', 'Insurance')

        elif dealer_score > 21:
            print('DEALER BUST!')

        for score, natural, wager in zip (player_score_list, player_natural_list, player_wager_list):
            # checking for human player's Blackjack:
            if natural == True:

                # checking for Dealer's Blackjack:
                if dealer_natural == False:
                    print(f"{player.name}'s {wager} has won 3:2!")
                    player.add_winnings('3:2', wager)
                else:
                    print(f"{player.name}'s {wager} has TIED!")
                    player.add_winnings('Tie', wager)

            # checking for Dealer's Blackjack:
            elif dealer_natural == True:
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
                print(f"{player.name}'s {wager} has TIED!")
                player.add_winnings('Tie', wager)
            # checking if dealer's score is greater than human player's score:
            elif score < dealer_score:
                print(f"House has won {player.name}'s {wager}!")


if __name__ == '__main__':

    #game setup:
    print('Welcome to the Blackjack Game!')
    name = ask_players_name()
    plr = HumanPlayer(name)
    dlr = Player()

    play_again = True
    need_more_chips = True
    first_round = True

    #game cycle:
    while play_again:

        #checking if player needs more chips:
        if need_more_chips:

            if not first_round and plr.chips['Amount'] == 0:
                print('\n'*100)
                print(f'\n{plr.name} has no chips left!')
            else:
                print('\n'*100)

            plr.get_chips()
            first_round = False
            press_enter_to_continue()
        else:
            pass

        #shuffling the deck and placing a bet:
        print('\n'*100)
        print('New round!')
        current_deck = Deck()
        current_deck.shuffle()
        plr.place_bet('Main Wager')
        # asking to press enter to continue:
        press_enter_to_continue()

        #creating a "Normal" Hand object for player:
        plr.start_hand()

        #creating a "Normal" Hand object for dealer:
        dlr.start_hand()

        #dealing initial 2 cards to both player and dealer and displaying the cards
        plr.hand.add_card_from_deck(current_deck)
        dlr.hand.add_card_from_deck(current_deck)

        plr.hand.add_card_from_deck(current_deck)
        dlr.hand.add_card_from_deck(current_deck)

        #playing a round:
        plr_scores, plr_naturals, plr_wagers, surrender = players_turn(plr, dlr, current_deck)

        #checking for surrender:
        if not surrender:
            #dealer's turn:
            dlr_score, dlr_natural = dealers_turn(dlr, plr, plr_scores, plr_naturals, current_deck)
            #checking the outcome and adding winnings:
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

        #cleanup after a finished round:
        plr.clear_wager()
        plr.split_hands = []

        #checking if player's got any chips, or sufficient bankroll to purchase chips:

        if plr.chips['Amount'] == 0 and plr.bankroll < 1:
            break
        else:
            #asking if player wants to play again
            play_again = replay()

            if play_again:
                #checking if cheque change is needed
                exchange_possible, high_value_color = plr.cheque_change_possible()

                if exchange_possible:

                    if cheque_change_requested(high_value_color):
                        plr.cheque_change(high_value_color)

                #checking if player needs more chips
                if plr.chips['Amount'] == 0:
                    need_more_chips = True
                elif plr.bankroll < 1:
                    need_more_chips = False
                else:
                    need_more_chips = more_chips_requested()

    print(f"Game over! {plr.name}'s bankroll: {(plr.bankroll + plr.chips['Amount']):7.2f}")
