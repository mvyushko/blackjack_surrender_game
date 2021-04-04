"""
Creates an instance of HumanPlayer class and runs the get_chips(self) method of this class. Prints out the updated
self.chips dictionary.
"""
from blackjack_surrender_game import HumanPlayer

player = HumanPlayer('Masha')

player.get_chips()

print(player.chips)