"""
Contains functions dealing with blackjack chips: displaying chip values, and converting money into chips.
Uses the colors.py module borrowed from https://www.geeksforgeeks.org/print-colors-python-terminal/ to display colored
chip symbols.
When running in Windows, uses colorama (with Fore.LIGHTMAGENTA_EX used for "pink", and Back.YELLOW + Fore.RED for
"orange").
"""
import sys
import math

# checking the platform:
if sys.platform.startswith('win'):
    # when running in Windows, use colorama for colored output:
    from colorama import init
    init()
    from colorama import Fore, Back, Style
    # colors for output formatting:
    PINK = Fore.LIGHTMAGENTA_EX
    RED = Fore.LIGHTRED_EX
    GREEN = Fore.GREEN
    ORANGE = Back.YELLOW + Fore.RED
    RESET = Style.RESET_ALL
else:
    # use the colors module:
    from colors import colors
    # colors for output formatting:
    PINK = colors.fg.pink
    RED = colors.fg.red
    GREEN = colors.fg.green
    ORANGE = colors.fg.orange
    RESET = colors.reset

# tuple containing all chip colors:
CHIP_COLORS = ('Orange', 'Green', 'Red', 'Pink', 'White')

# dictionary containing chip values:
CHIP_VALUES = {'White': 1, 'Pink': 2.5, 'Red': 5, 'Green': 25, 'Orange': 50}

# dictionary containing chip symbols (letters 'O' of corresponding color, black letter 'O'  for a 'White' chip):
CHIP_SYMBOLS = {'White': RESET + 'O', 'Pink': PINK + 'O', 'Red': RED + 'O',
                'Green': GREEN + 'O', 'Orange': ORANGE + 'O'}


def display_chip_values():
    """
    Displays all chip colors and corresponding monetary values
    """
    print('\nChip colors and values:')

    for color in CHIP_COLORS:
        print(f'{CHIP_SYMBOLS[color]} {color:<6} {CHIP_VALUES[color]:>19.2f}' + RESET)

def money_to_chips(amount_to_convert):
    """
    A function to convert money into chips
    :param amount_to_convert: monetary amount to be exchanged for chips
    :return: dictionary containing the number of chips of each color and their total value ('Amount')
    :rtype: dict
    """
    # checking if amount to convert is non-negative:
    if amount_to_convert < 0:
        raise ValueError('Amount to convert should be greater than zero')

    # initializing the dictionary containing the number of chips of each color and their total value ('Amount')
    chips = {'White': 0, 'Pink': 0, 'Red': 0, 'Green': 0, 'Orange': 0, 'Amount': 0}

    # fractional part of the amount to convert:
    fract_part = math.modf(amount_to_convert)[0]

    # rounding quarter-integer amounts down to half-integers:
    if fract_part in [0.25, 0.75]:
        discarded_amount = 0.25
        amount_to_convert -= discarded_amount
        fract_part -= discarded_amount

    # use a Pink chip to get rid of half-integer values:
    if fract_part == 0.5 and amount_to_convert >= 2.5:
        chips['Pink'] += 1
        chips['Amount'] += 2.5
        amount_to_convert -= 2.5

    # converting the remaining (integer) amount into integer-value chips:
    # for loop over all chip colors except Pink (because Pink has a half-integer value, 2.50):
    for color in ('Orange', 'Green', 'Red', 'White'):
        # divide the amount to convert by the value corresponding to current chip color and take the integer part:
        chips_added = int(amount_to_convert / CHIP_VALUES[color])
        # add corresponding number of chips of current color to the chips dictionary:
        chips[color] += chips_added
        # add corresponding amount to the chips total value ("Amount"):
        chips['Amount'] += chips_added * CHIP_VALUES[color]
        # and remove it from the amount to convert:
        amount_to_convert -= chips_added * CHIP_VALUES[color]

    return chips
