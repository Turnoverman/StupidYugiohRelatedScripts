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

candidates = []
for card in carddump:
	if "XYZ" in card['type'] or "Link" in card['type'] or "Synchro" in card['type'] or "Fusion" in card['type']:
		if "Dragon" in card['race']:
			if card['atk'] >= 0:
				candidates.append(Card(card['name'], card['atk']))

minimum_lp = 8000
for i in range(len(candidates)):
	for j in range(i, len(candidates)):
		for k in range(j, len(candidates)):
			for l in range(k, len(candidates)):
				for m in range(l, len(candidates)):
					total = candidates[i].atk+candidates[j].atk+candidates[k].atk+candidates[l].atk+candidates[m].atk
					if (total < 8000) and ((8000-total) <= minimum_lp):
						minimum_lp = 8000 - total
						print(8000-total, candidates[i], candidates[j], candidates[k], candidates[l], candidates[m])
#
# deck = []
# extradeck = []
# num = 0
# while num < 40:
# 	id = int(random.random() * 100000000)
# 	if id in ids:
# 		num += 1
# 		deck.append(id)
# 	elif id in edids:
# 		extradeck.append(id)
#
# # Output (to stdout, use pipes) a .ydk file
# print("#main")
# for card in deck:
# 	print(card)
# print("")
# print("#extra")
# for card in extradeck:
# 	print(card)
# print("")
# print("!side")
# print("")
