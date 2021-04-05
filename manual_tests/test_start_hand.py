"""
Creates an instance of HumanPlayer class. Starts an empty "Normal" Hand for HumanPlayer and two empty "Split Hand"
Hands. Prints out the attributes of all three Hands.
"""
from player_classes import HumanPlayer

player = HumanPlayer('Masha')
player.start_hand()
player.start_split_hand('1', 0)
player.start_split_hand('2', 1)

print ('Hand type:', player.hand.type)
print('Cards:', player.hand.cards)
print('Hand Score:', player.hand.score)
print ('Split hand number:', player.hand.split_hand_number)
print('Split wager number:', player.hand.split_wager_number)
print('\n')

print ('Hand type and number:', player.split_hands[0].type, player.split_hands[0].split_hand_number)
print('Cards:', player.split_hands[0].cards)
print('Hand Score:', player.split_hands[0].score)
print ('Split wager number:', player.split_hands[0].split_wager_number)
print('\n')

print ('Hand type and number:', player.split_hands[1].type, player.split_hands[1].split_hand_number)
print('Cards:', player.split_hands[1].cards)
print('Hand Score:', player.split_hands[1].score)
print ('Split wager number:', player.split_hands[1].split_wager_number)
