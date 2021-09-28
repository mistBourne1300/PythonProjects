import re
import random as rand
import os
from time import time


if __name__ == "__main__":
	built_string = ""
	english_file = open("all_english_words.txt")
	words = [str.lower(line.strip()) for line in english_file]
	english_file.close()
	hang_word = rand.choice(words)
	tries = 0
	for i in range(len(hang_word)):
		built_string += '.'
	
	start_time = time()
	while built_string != hang_word:
		tries +=1
		print(built_string)
		input_character = input("enter a single character to try: ")
		os.system("clear")
		if(input_character == "i give up"):
			# hahahahha
			print("I understand. I was unneccesarily cruel, wasn't I?")
			break
		while (len(input_character) != 1):
			# if they're not giving up, they need to only have a single character
			input_character = input("not a single character. try again: ")
		if(hang_word.find(input_character) == -1):
			# they input an incorrect character 
			print("nice try. shuffling word")
			# need to truncate the built_string to only contain the letters then know 
			# (and the unknown ones in between)

			# going up
			while len(built_string) > 0:
				if(built_string[0] != '.'):
					break
				else:
					built_string = built_string[1:]
			
			# going down
			while len(built_string) > 0:
				if(built_string[-1] != '.'):
					break
				else:
					built_string = built_string[:-1]

			# finding all words that match the current built_string
			matches = []
			for word in words:
				if(bool(re.search(built_string, word))):
					matches.append(word)
			hang_word = rand.choice(matches)
			match = re.search(built_string, hang_word)
			temp_string = built_string
			built_string = ''
			for i in range(len(hang_word)):
				built_string += '.'
			built_string = built_string[:match.start()] + temp_string + built_string[match.end():]

			# debug purposes
			# print(len(built_string))
			# print(hang_word)
			# print(f'built string: {built_string[:match.start()]} + {temp_string} + {built_string[match.end():]}')
			# print(built_string)
			# print(match)

			if(len(hang_word) != len(built_string)):
				raise RuntimeError(f"lengths of hang_word and built_string are unequal: {len(hang_word)}, {len(built_string)}")

			
		else:
			print("success. here's your word:")
			for i in range(len(hang_word)):
				#print(hang_word[i], input_character, hang_word[i] == input_character)
				if(hang_word[i] == input_character):
					built_string = built_string[:i] + input_character + built_string[i+1:]
	
	end_time = time()
	print(built_string, hang_word)
	total_time = round(end_time - start_time)
	if(built_string == hang_word):
		print(f'it took you {tries} guesses and {total_time} seconds to finish the game')
	else:
		print(f'it took you {tries} guesses and {total_time} seconds to give up')
	
	

			
					
		
