"""
Contains card-related classes for the blackjack surrender game (Card, Deck, and Hand), and a function evaluating Hand
objects for surrender. Uses colorama to display red card symbols.
"""
import random
from colorama import init
from colorama import Fore, Style

init()
# colors for output formatting:
RED = Fore.LIGHTRED_EX
RESET = Style.RESET_ALL

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
        # Blackjack value of the Card (int):
        self.value = card_values[rank]

        # color used for displaying the Card:
        # black card suits use default color:
        if self.suit in ['♣', '♠']:
            self.color = RESET
        # red card suits use red:
        else:
            self.color = RED

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
        # '10' is the only two-symbol card rank. it needs a special 'left_10' pattern on the left (with no space
        # between the left border of the card image and the card symbol)
        if self.rank == '10':
            left_border = patterns['left_10']
        else:
            left_border = patterns['left']

        # build the line-by-line representation of the card image from items of the "patterns" dictionary,
        # and colored string representation of the card:
        return {1: (RESET + patterns['top'] + patterns['space']),
                2: (RESET + patterns['upper'] + patterns['space']),
                3: (RESET + left_border + self.color + self.__str__() + RESET +
                    patterns['right'] + patterns['space']),
                4: (RESET + patterns['bottom'] + patterns['space'])}


class Deck:
    """
    An object representing a 52-card deck
    """

    def __init__(self):
        """
        Constructor for instantiating a Deck object
        """
        # list of Card objects in the Deck:
        self.deck_cards = []

        # adding 1 Card object of each suit and each rank to the list of Cards:/';mnj
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
        # list of Cards in the Hand:
        self.cards = []
        # total Blackjack value of the Hand:
        self.score = 0
        # number of corresponding split wager (0 for the Main Wager):
        self.split_wager_number = split_wager_number

    def add_card_from_deck(self, deck):
        """
        A method for taking cards from Deck and adding them to Hand
        :parameter deck: a Deck object
        """
        # taking a Card from Deck:
        new_card = deck.deal_one()
        # adding the Card to Hand:
        self.cards.append(new_card)
        # adding the Card value to the score:
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
        # if there are no split hands, display the Hand as "player's cards":
        if self.type == 'Normal':
            print(f"\n\n{players_name}'s Cards:")
        # if there are split hands, specify the split hand number and corresponding wager:
        else:

            # if the Hand corresponds to Main Wager:
            if self.split_wager_number == 0:
                print(f"\n\n{players_name}'s {self.type} {self.split_hand_number} (Main Wager):")
            # if the hand corresponds to one of Split Wagers, specify the Split Wager number:
            else:
                print(f"\n\n{players_name}'s {self.type} {self.split_hand_number}"
                  f" (Split Wager {self.split_wager_number}):")

        # displaying all cards in Hand, from left to right, line-by-line:
        # for loop over line numbers from 1 to 4:
        for line_number in range(1, 5):
            # current line of the line-by-line image:
            pattern = ''

            # constructing the line to be printed by concatenating corresponding lines of line-by-line images of each
            # card:
            for card in self.cards:
                pattern += card.display_patterns()[line_number]
            # printing the resulting line:
            print(pattern)

    def display_one_face_down(self, player):
        """
        Displays two cards in Hand with one card face up and another card face down
        """
        if len(self.cards) != 2:
            raise ValueError('Incorrect number of cards in the Hand. Only a two-card Hand can be displayed one face'
                             ' down.')

        print(f"\n\n{player}'s Cards:")

        # for loop over line numbers from 1 to 4:
        for line_number in range(1, 5):
            # displaying the line concatenated from corresponding line of the first card line-by-line image, and
            # corresponding line of the "card face down" line-by-line image
            print(self.cards[0].display_patterns()[line_number] + display_face_down[line_number])

    def split_pair(self):
        """
        Splits a two-card Hand into two Cards and returns them
        :return: tuple containing two Card objects
        """
        # checking if there are two cards in Hand:
        if len(self.cards) == 2:

            # removing both cards from Hand:
            split_card1 = self.cards.pop()
            split_card2 = self.cards.pop()
            # setting the Hand score to zero:
            self.score = 0
            # returning the two Cards:
            return split_card1, split_card2

        else:
            raise ValueError('Incorrect number of cards in Hand. Only a two-card Hand can be split')

    def add_card_from_split(self, split_card):
        """
        Adds a Card object obtained by splitting a pair to Hand
        :param split_card: a Card object
        """
        # checking if the card added from split is an Ace:
        if split_card.rank == 'A':
            # an Ace initially counts as 11:
            split_card.value = 11
            # adjusting the Hand score:
            self.score += 11
        else:
            # adding the card value to the Hand score:
            self.score += split_card.value

        # adding the Card to the list of Cards in Hand:
        self.cards.append(split_card)

    def play_for_dealer(self, deck):
        """
        Plays a Hand for Dealer. Adds cards from Deck until score hits soft 17 or more.
        :parameter deck: a Deck object
        :returns:  a tuple containing Dealer's final score, and a boolean showing if Dealer has a natural Blackjack
        :rtype: self.score: int, natural: bool
        """
        # checking for a Natural Blackjack:
        if self.score == 21:
            natural = True
        else:
            natural = False
            # adding Cards from Deck until the score of soft 17:
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

        # checking if Dealer's upcard is a 10 or an Ace:
        return dealer_upcard in ['10', 'J', 'Q', 'K', 'A']

    else:
        return False
