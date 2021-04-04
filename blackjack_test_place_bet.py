"""
Creates an instance of HumanPlayer class and runs the place_bet(self, bet) method of this class.
"""
from blackjack_with_chips import HumanPlayer

player = HumanPlayer('Masha')

player.chips = {'White': 0, 'Pink': 0, 'Red': 2, 'Green': 2, 'Orange': 0, 'Amount': 60}
player.wagers = {'Main Wager': {'White': 0, 'Pink':0, 'Red': 2, 'Green': 0, 'Orange': 0, 'Amount': 10},
                 'Insurance': {'White': 0, 'Pink': 0, 'Red': 0, 'Green': 0, 'Orange': 0, 'Amount': 0},
                 'Split Wager 1': {'White': 0, 'Pink':0, 'Red': 2, 'Green': 0, 'Orange': 0, 'Amount': 10},
                 'Split Wager 2': {'White': 0, 'Pink':0, 'Red': 0, 'Green': 0, 'Orange': 0, 'Amount': 0},
                 'Split Wager 3': {'White': 0, 'Pink':0, 'Red': 0, 'Green': 0, 'Orange': 0, 'Amount': 0}}
player.place_bet("Insurance")
print(player.wagers)