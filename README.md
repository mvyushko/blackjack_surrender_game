# blackjack_game

A Python 3 text version of 52-card Blackjack Surrender game for one human Player and a computer Dealer.

* Allowed moves include Splits, Doubling Down, placing Insurance bets, and Surrendering.
* After a Split, only one more Split is allowed on each split hand. Doubling Down after a Split is allowed.
* After splitting a pair of Aces, only one more card can be drawn on each split Ace. 
* Player may draw only one more card after Doubling Down.
* Late Surrender (after Dealer checks for Blackjack but before any other move is made). After surrendering a hand, player gets back half of the bet.
* Dealer stands on soft 17. Natural Blackjack pays 3:2. Insurance pays 2:1.

Cards are represented by rectangles constructed from pipe operators and underscores (look best with 1.0 line spacing, Consolas font).
Chips are represented by the capital "O" letters of corresponding color (with default color used for "White" chips).

For colored output, uses the colors module borrowed from https://www.geeksforgeeks.org/print-colors-python-terminal/.
When running in Windows, uses colorama (with Fore.LIGHTMAGENTA_EX used for "pink", and Back.YELLOW + Fore.RED for "orange").

