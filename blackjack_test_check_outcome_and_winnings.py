"""
Creates an instance of HumanPlayer class representing the human player. Sets a nonzero number of chips in HumanPlayers
chip pile and wagers. Runs the check_outcome_and_add_winnings(player, player_score_list, player_natural_list,
 player_wager_list, dealer_score, dealer_natural) function. Prints out the updated HumanPlayer's self.chips dictionary.
"""
from blackjack_with_chips import HumanPlayer, check_outcome_and_add_winnings

plr = HumanPlayer('Masha')

#total amount (chips + wagers): 36
plr.chips = {'White': 0, 'Pink': 0, 'Red': 6, 'Green': 0, 'Orange': 0, 'Amount': 30}
plr.wagers = {'Main Wager': {'White': 1, 'Pink': 0, 'Red': 1, 'Green': 0, 'Orange': 0,
                                'Amount': 6},
                 'Insurance': {'White': 0, 'Pink': 0, 'Red': 0, 'Green': 0, 'Orange': 0, 'Amount': 0},
                 'Split Wager 1': {'White': 3, 'Pink': 0, 'Red': 0, 'Green': 0, 'Orange': 0, 'Amount': 3},
                 'Split Wager 2': {'White': 0, 'Pink': 1, 'Red': 0, 'Green': 0, 'Orange': 0, 'Amount': 2.5},
                 'Split Wager 3': {'White': 0, 'Pink': 0, 'Red': 0, 'Green': 0, 'Orange': 0, 'Amount': 0}}

check_outcome_and_add_winnings(plr, [22, 20, 22], [False, False, False],
                               ['Main Wager', 'Split Wager 2', 'Split Wager 1'], 17, False)

print(plr.chips)