from blackjack_with_chips import HumanPlayer

player = HumanPlayer('Masha')
player.chips = {'White': 0, 'Pink': 0, 'Red': 0, 'Green': 0, 'Orange': 0}
player.wager = {'White': 1, 'Pink': 51, 'Red': 0, 'Green': 0, 'Orange': 0}
player.insurance = {'White': 0, 'Pink':0, 'Red': 0, 'Green': 0, 'Orange': 0}
player.split_wagers =  [{'White': 1, 'Pink': 51, 'Red': 0, 'Green': 0, 'Orange': 0},
                        {'White': 1, 'Pink': 51, 'Red': 0, 'Green': 0, 'Orange': 0}]
player.display_chips("Split Wager 1", "Split Wager 2", 'Insurance','Chips', "Main Wager")