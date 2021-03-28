from blackjack_with_chips import HumanPlayer

player = HumanPlayer('Masha')

player.chips = {'White': 0, 'Pink': 0, 'Red': 2, 'Green': 2, 'Orange': 0}
player.wager = {'White': 0, 'Pink': 0, 'Red': 0, 'Green': 0, 'Orange': 2}
player.insurance = {'White': 0, 'Pink': 0, 'Red': 0, 'Green': 0, 'Orange': 0}
player.place_bet("Insurance")
print(player.chips)
print(player.insurance)