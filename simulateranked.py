from random import random

class Rank:
    tier = 5
    tier_points = 0

    def rankup(self):
        self.tier -= 1
        self.tier_points = 0

    def rankdown(self):
        self.tier += 1
        self.tier_points = 0
   
    def win(self):
        if self.tier_points < 0:
            self.tier_points = 0
        self.tier_points += 1
        if self.tier_points >= 5:
            self.rankup()

    def lose(self):
        self.tier_points -= 1
        if self.tier_points <= -3 and self.tier < 5:
            self.rankdown()

def simulateLadder(win_rate):
    rank = Rank()
    iterations = 0
    while rank.tier > 1 and iterations < 1000000:
        if random() < win_rate:
            rank.win()
        else:
            rank.lose()
        iterations += 1
    return iterations

def runTrial(num_trials, win_rate):
    results = []
    i = 0
    while i < num_trials:
        result = simulateLadder(win_rate)
        if result >= 1000000:
            i += 50
        results.append(result)
        i += 1
    return len(results), min(results), sum(results)/len(results), max(results)


num_trials = 1000
for i in range(1, 100):
    win_rate = i/100.0
    trials,min_games,average,max_games = runTrial(num_trials, win_rate)
    print("Simulating", trials, "ladder grind(s) for win rate of", win_rate,":",min_games,average,max_games)
