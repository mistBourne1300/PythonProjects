'''simulates iterations of the game "Odds and Evens"
	Each player chooses odd or even, then
	puts up a hand with a number of fingers extended.
	the sum is calculated, and parity determined. The winner is the
	player who chose the correct parity for the sum.

	two variations are possible: 
		games that allow 0 fingers
		games that do not
	To simulate the two variations, either include
	or exclude o in the poss_hand list.
'''

import random as rand

def get_next():
	poss_hand = [0,1,2,3,4,5]
	hand1 = rand.choice(poss_hand)
	hand2 = rand.choice(poss_hand)

	return hand1 + hand2

if __name__ == "__main__":
	ITERATIONS = 10000
	is_odd = []
	for i in range(ITERATIONS):
		is_odd.append(get_next() % 2)
	
	print(is_odd)

	print("Percentage odd:")
	print(sum(is_odd) / len(is_odd))