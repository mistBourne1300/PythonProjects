import os

# print(len('4217643999648948533686334868689238648684936926487387936483792387473874873879277487739827083744470283757473727734087449816356081604710870805773074037775080387883874737473738717537476913846993774830183757488293864783588876433600098765421123455699999999999999995280522225138166806691251291352861698530421623488512'))
NUMBERS_TO_WORDS = {
	10**303: 'centillion',
	10**100: 'googol',
	10**63: 'vigintillion',
	10**60: 'novemdecillion',
	10**57: 'octodecillion',
	10**54: 'septen-decillion',
	10**51: 'sexdecillion',
	10**48: 'quindecillion',
	10**45: 'quatturodecillion',
	10**42: 'tredecillion',
	10**39: 'duodecillion',
	10**36: 'undecillion',
	10**33: 'decillion',
	10**30: 'nonillion',
	10**27: 'octillion',
	10**24: 'septillion',
	10**21: 'sextillion',
	10**18: 'quintillion',
	10**15: 'quadrillion',
	10**12: 'trillion',
    10**9: 'billion',
    10**6: 'million',
    10**3: 'thousand',
    10**2: 'hundred',
    90: 'ninety',
    80: 'eighty',
    70: 'seventy',
    60: 'sixty',
    50: 'fifty',
    40: 'forty',
    30: 'thirty',
    20: 'twenty',
    19: 'nineteen',
    18: 'eighteen',
    17: 'seventeen',
    16: 'sixteen',
    15: 'fifteen',
    14: 'fourteen',
    13: "thirteen",
    12: "twelve",
    11: "eleven",
    10: "ten",
    9: "nine",
    8: "eight",
    7: "seven",
    6: "six",
    5: "five",
    4: "four",
    3: "three",
    2: "two",
    1: "one"
}

WORDS_TO_NUMBERS = {
	'centillion': 10**303,
	'googol': 10**100,
	'vigintillion': 10**63,
	'novemdecillion': 10**60,
	'octodecillion': 10**57,
	'septen-decillion': 10**54,
	'sexdecillion': 10**51,
	'quindecillion': 10**48,
	'quatturodecillion': 10**45,
	'tredecillion': 10**42,
	'duodecillion': 10**39,
	'undecillion': 10**36,
	'decillion': 10**33,
	'nonillion': 10**30,
	'octillion': 10**27,
	'septillion': 10**24,
	'sextillion': 10**21,
	'quintillion': 10**18,
	'quadrillion': 10**15,
	'trillion': 10**12,
	'billion': 10**9,
	'million': 10**6,
	'thousand': 10**3,
	'hundred': 10**2,
	'ninety': 90,
	'eighty': 80,
	'seventy': 70,
	'sixty': 60,
	'fifty': 50,
	'forty': 40,
	'thirty': 30,
	'twenty': 20,
	'nineteen': 19,
	'eighteen': 18,
	'seventeen': 17,
	'sixteen': 16,
	'fifteen': 15,
	'fourteen': 14,
	"thirteen": 13,
	"twelve": 12,
	"eleven": 11,
	"ten": 10,
	"nine": 9,
	"eight": 8,
	"seven": 7,
	"six": 6,
	"five": 5,
	"four": 4,
	"three": 3,
	"two": 2,
	"one": 1,
	"zero": 0
}

def string_to_num(string, v=False): 
	words = string.split()
	def parse_list(lst, whitespace = ''):

		for WORD in WORDS_TO_NUMBERS:
			if WORD not in lst: continue
			if v:
				print(f'{whitespace}{WORD}')
			if len(lst) == 1: return WORDS_TO_NUMBERS[WORD]

			index = len(lst) - lst[::-1].index(WORD) - 1

			# if the index is the last in the list, there is nothing to add at the end, and we don't want to raise an exception
			if index == len(lst) - 1:
				return parse_list(lst[:index], whitespace+'\t*') * WORDS_TO_NUMBERS[WORD]
			
			if index == 0:
				return WORDS_TO_NUMBERS[WORD] + parse_list(lst[index+1:], whitespace+'\t+')
			
			return parse_list(lst[:index], whitespace+'\t*') * WORDS_TO_NUMBERS[WORD] + parse_list(lst[index+1:], whitespace+'\t+')
			




		
	return parse_list(words)
		

def get_string(num, p=False, whitespace = ''):
	#if num == 0:
		#return 'zero'
	userNumStr = ""
	for NUMBER in NUMBERS_TO_WORDS:
		if num >= NUMBER:
			number_of_NUMBERS = num // NUMBER
			
			if p:
				print(f'{whitespace}num: {num}')
				print(f'{whitespace}numNUMBER: {NUMBER}')
				print(f'{whitespace}numnumber_of_NUMBERS: {number_of_NUMBERS}')
			
			
			# if greater than 100, find how many there are
			if NUMBER >= 100:
				userNumStr += get_string(number_of_NUMBERS,p,whitespace+'\t')
				userNumStr += NUMBERS_TO_WORDS[NUMBER] + ' '
			# otherwise, just append the number
			else:
				userNumStr += NUMBERS_TO_WORDS[NUMBER] + ' '
			
			# subtract off the value we just computed
			num = num - (number_of_NUMBERS * NUMBER)
			
		if p:
			print(f'{whitespace}numpassed {NUMBERS_TO_WORDS[NUMBER]}, userNumStr: {userNumStr}')
	return userNumStr

def get_num_letters(str):
	num_letters = 0
	for l in str:
		if l.isalpha(): num_letters += 1
	return num_letters



userNum = int(input(f"Enter an integer: "))
userNum2 = userNum
userNumStr = get_string(userNum, True)

print(f'\n\n{userNum}: {userNumStr}\n\ncalculating back:')
calc_back = string_to_num(userNumStr,True)

print(calc_back)
print(f'string_to_num worked: {calc_back == userNum}')


# os.system(f'say {userNumStr}')

# for i in range(1,10):
# 	os.system(f'say {get_string(i)}')





# while userNum != 4:
# 	userNumStr = get_string(userNum)
# 	# print(f'{userNum}: {userNumStr}')
# 	num_letters = get_num_letters(userNumStr)
# 	print(f'{userNum} has {num_letters} letters')
# 	userNum = num_letters
# userNumStr = get_string(userNum)
# # print(f'{userNum}: {userNumStr}')
# num_letters = get_num_letters(userNumStr)
# print(f'{userNum} has {num_letters} letters')
# userNum = num_letters











# if userNum2 < 100000:
# 	throw_away = input("press enter to continue")
# 	for i in range(25):
# 		print('*', end = "")
# 	print(f'\nCalculating the iterations for each number up to {userNum2}...\n\n')
# 	iterations_array = []
# 	for i in range(1, userNum2+1):
# 		num_to_calculate = i
# 		counter = 1
# 		while num_to_calculate != 4:
# 			userNumStr = get_string(num_to_calculate)
# 			num_letters = get_num_letters(userNumStr)
# 			num_to_calculate = num_letters
# 			counter += 1
# 		iterations_array.append(counter)
	
# 	#for i in range(len(iterations_array)):
# 	    #print(f'{i+1} took {iterations_array[i]} iterations to reach four.')
# 	max_iter = max(iterations_array)
# 	print(f'The number \'{iterations_array.index(max_iter) + 1}\' is longest anything took to reach four with {max_iter} iterations')


