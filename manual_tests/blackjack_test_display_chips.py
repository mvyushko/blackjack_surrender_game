"""
Creates an instance of HumanPlayer class, puts some nonzero chip numbers in HumanPlayer's self.chips and self.wagers
dictionaries, and runs the display_chips(self, *args) method.
"""

from blackjack_surrender_game import HumanPlayer

player = HumanPlayer('Masha')
player.chips = {'White': 0, 'Pink': 0, 'Red': 1, 'Green': 0, 'Orange': 1, 'Amount': 55}
player.wagers = {'Main Wager': {'White': 1, 'Pink': 31, 'Red': 0, 'Green': 0, 'Orange': 1, 'Amount': 128.5},
                 'Insurance': {'White': 0, 'Pink':0, 'Red': 0, 'Green': 1, 'Orange': 1, 'Amount': 75},
                 'Split Wager 1': {'White': 1, 'Pink': 31, 'Red': 0, 'Green': 0, 'Orange': 1, 'Amount': 128.5},
                 'Split Wager 2': {'White': 1, 'Pink': 31, 'Red': 0, 'Green': 0, 'Orange': 0, 'Amount': 77.5},
                 'Split Wager 3': {'White': 0, 'Pink':0, 'Red': 5, 'Green': 0, 'Orange': 1, 'Amount': 55}}
player.display_chips(*player.wagers.keys())