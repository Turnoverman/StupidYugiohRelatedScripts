#! /usr/bin/python3

import math
import random
import sys

class Card:
    def __init__(self, name, value):
        self.name = name
        self.value = value

    def __lt__(self, other):
        return self.value < other.value

    def play(self):
        return self.value
    
class ThePathsOfDestiny(Card):
    def play(self):
        return 2000 if random.random() > 0.5 else -2000

class FireDarts(Card):
    def play(self):
        rolls = 0
        for i in range(3):
            rolls += math.ceil(random.random() * 6)
        return rolls * 100        

class Deck:
    def __init__(self):
        self.cards = []
        for i in range(3):
            self.cards.append(self.makeCard("Hinotama", 500))
            self.cards.append(self.makeCard("Goblin Thief", 500))
            self.cards.append(self.makeCard("Chain Detonation", 500))
            self.cards.append(self.makeCard("Ookazi", 800))
            self.cards.append(self.makeCard("Meteor of Destruction", 1000))
            self.cards.append(self.makeCard("Tremendous Fire", 1000))
            self.cards.append(self.makeCard("Raimei", 300))
            self.cards.append(self.makeCard("Secret Barrel", 1200))
            self.cards.append(ThePathsOfDestiny("The Paths of Destiny", 0))
            self.cards.append(self.makeCard("Meteor Flare", 2000))
            self.cards.append(self.makeCard("Secret Blast", 1800))
            self.cards.append(self.makeCard("Bad Luck Blast", 1500))
            self.cards.append(FireDarts("Fire Darts", 1050))
        self.cards.append(self.makeCard("Fairy Wind", 1200))
        random.shuffle(self.cards)
        
    def makeCard(self, name, value):
        return Card(name, value)
                          
class Hand:
    def __init__(self, deck, numcards, verbose):
        self.cards = []           
        if verbose:
            print("I drew:")
        for i in range(numcards):
            self.cards.append(deck.cards.pop())
            if verbose:
                print(self.cards[i].name)
        self.cards.sort(reverse=True)

    def discard(self, position):
        self.cards.pop(position)

    def play(self, position):
        card = self.cards.pop(position)
        return card.play()

    def empty(self):
        return len(self.cards) == 0

    def getCard(self, position):
        return self.cards[position]

    def numcards(self):
        return len(self.cards)

def playMeteorFlare(hand):
                          
    if hand.numcards() < 3:
        hand.discard(0)
        return 0
    meteorflares = 0
    for card in hand.cards:
        meteorflares += (card.name == "Meteor Flare")
    if meteorflares == 0:
        print("I broke because I'm trying to play a nonexistent Meteor Flare")
        exit()
    if meteorflares == 1:
        if (hand.cards[-1].value + hand.cards[-2].value) < hand.cards[0].value:
            hand.discard(hand.numcards() - 1)
            hand.discard(hand.numcards() - 1)
            return hand.play(0)
        else:
            hand.discard(0)
            return 0
    if meteorflares == 2:
        hand.discard(hand.numcards() - 1)
        for i in range(1, hand.numcards()):
            if hand.getCard(i).name == "Meteor Flare":
                hand.discard(i)
                break
        return hand.play(0)
    if meteorflares == 3:
        for i in range(1, hand.numcards()):
            if hand.getCard(i).name == "Meteor Flare":
                hand.discard(i)
                break
        for i in range(1, hand.numcards()):
            if hand.getCard(i).name == "Meteor Flare":
                hand.discard(i)
                break
        return hand.play(0)
    if meteorflares > 3:
        print("I broke because there were " + str(meteorflares) + " Meteor Flares")
        exit()

def playAGame():
    deck = Deck()
    numcards = 5
    verbose = False
    if len(sys.argv) > 1:
       verbose = True 
    hand = Hand(deck, numcards, verbose)
    damage = 0
    while not hand.empty():
        if hand.getCard(0).name == "Meteor Flare":
            damage += playMeteorFlare(hand)
        else:
            damage += hand.play(0)
    if(verbose):
        print("I did " + str(damage) + " which is" + (" not" if damage < 8000 else "") +  " a kill")
    return damage > 8000, damage

def main():
    kills = 0
    totaldamage = 0
    games = 1000000
    for i in range(games):
        kill, damage = playAGame()
        kills += kill
        totaldamage += damage
    print("Out of " + str(games) + " games, " + str(kills) + " were kills.")
    print("Average damage was " + str(totaldamage/games) + ".")
                          
if __name__ == '__main__':
    main()

