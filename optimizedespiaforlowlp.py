#!/usr/bin/python3
import json
import random

class Card:
	def __init__(self,name,atk):
		self.name = name
		self.atk = atk

	def __str__(self):
		return self.name + ": " + str(self.atk)

# Read a database dump of all yugioh cards (gotten separately from ygoprodeck)
with open("yugiohcarddatabasedump") as dump:
	dump_dict = json.loads(dump.read())
carddump = dump_dict['data'] # Pull out the cards

candidatesdespia = []
candidateslight = []
candidatesdark = []

for card in carddump:
	if "XYZ" in card['type'] or "Link" in card['type'] or "Synchro" in card['type'] or "Fusion" in card['type']:
		if "Despia" in card['name'] and card['atk'] >= 0:
				candidatesdespia.append(Card(card['name'], card['atk']))
		if "LIGHT" in card['attribute'] and card['atk'] >= 0:
				candidateslight.append(Card(card['name'], card['atk']))
		if "DARK" in card['attribute'] and card['atk'] >= 0:
				candidatesdark.append(Card(card['name'], card['atk']))

#override candidatesdark
# candidatesdark = []
# candidatesdark.append(Card("Barox", 1380))

# starting_lp = 8000
# Assume we made Coordius the Triphasic Dealmon
# with two 0-atk monsters and utopia prime first
starting_lp = 5490
# Assume we used his effect monkaS
# starting_lp = 3490
minimum_lp = starting_lp
for i in range(len(candidatesdespia)):
	for j in range(len(candidateslight)):
		for k in range(len(candidatesdark)):
			total = candidatesdespia[i].atk+candidateslight[j].atk+candidatesdark[k].atk
			if (total < starting_lp) and ((starting_lp-total) <= minimum_lp):
				minimum_lp = starting_lp - total
				print(starting_lp-total, candidatesdespia[i], candidateslight[j], candidatesdark[k])
