#!/usr/bin/python3

from random import randint

total = 1000000
opponent_higher = 0
player_higher = 0
for i in range(total):
    player_total = randint(1,6) + randint(1,6)
    opponent_total = max(randint(1,6),randint(1,6)) + 7
    if player_total > opponent_total:
        player_higher += 1
    elif opponent_total > player_total:
        opponent_higher += 1

print("Total trials: " + str(total))
print("Opponent higher: " + str(opponent_higher))
print("Player higher: " + str(player_higher))
print("Probability locked out: " + str(opponent_higher/total))

