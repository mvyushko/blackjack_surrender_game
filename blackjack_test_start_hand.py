from blackjack_with_chips import HumanPlayer

player = HumanPlayer('Masha')
player.start_hand()
player.start_split_hand1()
player.start_split_hand2()

print(player.hand.cards)
print(player.hand.score)
print (player.hand.type)
print('\n')

print(player.split_hand1.cards)
print(player.split_hand1.score)
print (player.split_hand1.type)
print('\n')

print(player.split_hand2.cards)
print(player.split_hand2.score)
print (player.split_hand2.type)