"""
Creates an instance of HumanPlayer class and runs the get_chips(self) method of this class. Prints out the updated
self.chips dictionary.
"""
from player_classes import HumanPlayer

player = HumanPlayer('Masha')

player.get_chips()

print(player.chips)
