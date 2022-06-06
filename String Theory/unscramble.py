import numpy as np

def get_variations(word:str):
	letters = list(word)
	new_var =  ''
	list_of_gits = [i for i in range(len(word))][::-1]
	update_index = len(list_of_gits)-1
	while sum(list_of_gits) > 0:
		let_copy = letters.copy()
		new_word = ''
		# get the new variation of the word
		for index in list_of_gits:
			new_word += let_copy.pop(index)
		yield new_word

		# now the hard part. if the git list at the update index is at max capacity, we need to move the update index up by one
		# and then we need to drop it again? 
		# lets see. if I pop off the list of the word, we can update each index by dropping it by one.
		# once it hits zero, we can move over one until we get a nonzero entry, drop that by one, then 

		for i in range(len(list_of_gits)):
			index = len(list_of_gits)-1-i
			if list_of_gits[index] == 0:
				continue
			update_index = index
			break
		list_of_gits[update_index] -= 1
		for i in range(update_index+1, len(list_of_gits)):
			list_of_gits[i] = len(list_of_gits)-i-1
	
	# return the last iteration of the word
	let_copy = letters.copy()
	new_word = ''
	for index in list_of_gits:
		new_word += let_copy.pop(index)
	yield new_word


if __name__ == "__main__":
	english = open("all_english_words.txt").read().split()
	word = input('enter word: ')
	N = np.math.factorial(len(word))
	english = np.array([w.lower() for w in english])
	lengths = np.array([len(w) for w in english])
	poss_words = english[lengths == len(word)]
	for i, poss in enumerate(get_variations(word)):
		per = int(100*(i+1)/N)
		print(f'{i}/{N}: {poss} ({per}%)', end = "\r")
		if poss in poss_words:
			[print("-",end = '') for i in range(len(poss)+2*len(str(N))+10)]
			print("\nunscrambled word:")
			print(f'{poss} ({per}% percent computed)')
			break
	print(f'saved {len(english)-len(poss_words)} words ({len(poss_words)} comparisons per iteration)')
#eomselohw
#someolewh
#someolehw
