#!/usr/bin/python3
import json
import random
# Read a database dump of all yugioh cards (gotten separately from ygoprodeck)
with open("yugiohcarddatabasedump") as dump:
	dump_dict = json.loads(dump.read())
cards = dump_dict['data'] # Pull out the cards

# Pull out the IDs, separating extra deck and not extra deck cards
ids = set()
edids = set()
for card in cards:
	if "Token" in card['type']:
		pass
	elif "XYZ" in card['type'] or "Link" in card['type'] or "Synchro" in card['type'] or "Fusion" in card['type']:
		edids.add(card['id'])
	else:
		ids.add(card['id'])

deck = []
extradeck = []
num = 0
while num < 40:
	id = int(random.random() * 100000000)
	if id in ids:
		num += 1
		deck.append(id)
	elif id in edids:
		extradeck.append(id)

# Output (to stdout, use pipes) a .ydk file
print("#main")
for card in deck:
	print(card)
print("")
print("#extra")
for card in extradeck:
	print(card)
print("")
print("!side")
print("")
