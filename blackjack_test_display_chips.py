"""
Creates an instance of HumanPlayer class, puts some nonzero chip numbers in HumanPlayer's self.chips and self.wagers
dictionaries, and runs the display_chips(self, *args) method.
"""

from blackjack_with_chips import HumanPlayer

player = HumanPlayer('Masha')
player.chips = {'White': 0, 'Pink': 0, 'Red': 1, 'Green': 0, 'Orange': 0, 'Amount': 5}
player.wagers = {'Main Wager': {'White': 1, 'Pink': 51, 'Red': 0, 'Green': 0, 'Orange': 0, 'Amount': 128.5},
                 'Insurance': {'White': 0, 'Pink':0, 'Red': 0, 'Green': 0, 'Orange': 0, 'Amount': 0},
                 'Split Wager 1': {'White': 1, 'Pink': 51, 'Red': 0, 'Green': 0, 'Orange': 0, 'Amount': 128.5},
                 'Split Wager 2': {'White': 1, 'Pink': 51, 'Red': 0, 'Green': 0, 'Orange': 0, 'Amount': 128.5},
                 'Split Wager 3': {'White': 0, 'Pink':0, 'Red': 0, 'Green': 0, 'Orange': 0, 'Amount': 0}}
player.display_chips(*player.wagers.keys())