mNUMBERS_TO_WORDS = {
    1000000000: 'billion',
    1000000: 'million',
    1000: 'thousand',
    100: 'hundred',
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

def get_string(num, p=False):
    userNumStr = ""
    for NUMBER in NUMBERS_TO_WORDS:
        if num >= NUMBER:
            number_of_NUMBERS = int(num / NUMBER)
            
            if p:
                print(f'num: {num}')
                print(f'NUMBER: {NUMBER}')
                print(f'number_of_NUMBERS: {number_of_NUMBERS}')



            # if greater than 100, find how many there are
            if NUMBER >= 100:
                userNumStr += get_string(number_of_NUMBERS)
                userNumStr += f'{NUMBERS_TO_WORDS[NUMBER]} '
            # otherwise, just append the number
            else:
                userNumStr += f'{NUMBERS_TO_WORDS[NUMBER]} '
            
            # subtract off the value we just computed
            num = num - (number_of_NUMBERS * NUMBER)
            
        if p:
            print(f'passed {NUMBERS_TO_WORDS[NUMBER]}, userNumStr: {userNumStr}')
    return userNumStr

def get_num_letters(str):
    num_letters = 0
    for l in str:
        if l.isalpha(): num_letters += 1
    return num_letters



userNum = int(input(f"Enter an integer: "))
userNum2 = userNum
userNumStr = get_string(userNum, True)

print(f'\n\n{userNum}: {userNumStr}\n\n')

throw_away = input("press enter to continue")


while userNum != 4:
    userNumStr = get_string(userNum)
    print(f'{userNum}: {userNumStr}')
    num_letters = get_num_letters(userNumStr)
    print(f'{userNum} has {num_letters} letters')
    userNum = num_letters
userNumStr = get_string(userNum)
print(f'{userNum}: {userNumStr}')
num_letters = get_num_letters(userNumStr)
print(f'{userNum} has {num_letters} letters')
userNum = num_letters

for i in range(25):
    print('*', end = "")
print(f'\nCalculating the iterations for each number up to {userNum2}...\n\n')
iterations_array = []
for i in range(1, userNum2+1):
    num_to_calculate = i
    counter = 1
    while num_to_calculate != 4:
        userNumStr = get_string(num_to_calculate)
        num_letters = get_num_letters(userNumStr)
        num_to_calculate = num_letters
        counter += 1
    iterations_array.append(counter)

#for i in range(len(iterations_array)):
    #print(f'{i+1} took {iterations_array[i]} iterations to reach four.')
max_iter = max(iterations_array)

print(f'The number \'{iterations_array.index(max_iter) + 1}\' is longest anything took to reach four with {max_iter} iterations')
