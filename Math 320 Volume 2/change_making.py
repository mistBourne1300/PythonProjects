import time
import os
import matplotlib.pyplot as plt


def naive_change(amount, system):
	""" accepts an coinage amount, and recursivly solve for the minimum number of coins it takes to equal that amount
			parameters: 
				amount (int) the amount of change to compute
				system (set) the coinage system to work under
			
			returns:
				minumum_coins (int) the minimum number of coins it takes to equal [amount]

			raises:
				ValueError if system does not contain 1 (may result in unsolvable problem)
	"""
	# print(f'naive_change({amount})')
	if(1 not in system):
		raise ValueError(f'1 must be in system. your system: {system}')
	
	if(amount < 0):
		raise ValueError("cannot compute coinage for negative numbers")
	
	if(amount == 0):
		return 0

	if(amount in system):
		# if the amount passed in is already in the coinage system, we only need one more coin
		return 1
	
	minimum_coins = naive_change(amount-system[0], system)
	for i in range(1, len(system)):
		if(amount - system[i] >= 0):
			poss_min = naive_change(amount-system[i], system)
			if(poss_min < minimum_coins):
				minimum_coins = poss_min
	return minimum_coins + 1

def bottom_up_change(amount, system):
	solved_states = {0:0}
	for coin in system:
		solved_states[coin] = 1
	if amount in system:
		return 1
	
	for i in range(1,amount +1):
		# print(f'coins for {i}: ')
		if i not in system:
			poss_mins = []
			for coin in system:
				if(i-coin > 0):
					poss_mins.append(solved_states[i-coin])
			minimum = min(poss_mins)
			solved_states[i] = 1 + minimum
		

	return solved_states[amount]
		
def greedy_change(amount, system):
	system_solved = {}
	for coin in system:
		system_solved[coin] = 0
	num_coins = 0
	for coin in system[::-1]:
		while(amount >= coin):
			amount -= coin
			num_coins += 1
			system_solved[coin] += 1
	return num_coins, system_solved

def greedy_change_David(amount, system):
	system_solved = {}
	coins = 0
	for coin in system:
		system_solved[coin] = 0
	if(amount in system):
		system_solved[amount] += 1
		return 1, system_solved
	
	for coin in system[::-1]:
		coins += int(amount/coin)
		system_solved[coin] += coins
		amount = amount%coin

		if(amount == 0):
			return coins, system_solved

		

if __name__ == "__main__":
	os.chdir("/Users/chase/Desktop/Math 320 Volume 2")
	sec_count = int(input("how many thousanths of a second do you want to test for? "))
	sec_count = sec_count/1000
	US_system = [1,5,10,25,50,100]
	domain = range(1000000)
	greedy = []
	greedy_david = []
	sum_mine_faster = 0
	i = 0
	while True:
		start_time = time.time()
		greedy_amount, system_solved = greedy_change_David(i, US_system)
		greedy_david.append(time.time() - start_time)

		start_time = time.time()
		greedy_amount, system_solved = greedy_change(i, US_system)
		greedy.append(time.time() - start_time)

		if greedy_david[i] > greedy[i]:
			print(f'{i}:\n\tgreedy_david: {greedy_david[i]}\n\tgreedy:{greedy[i]}')
			sum_mine_faster += 1
		if(greedy[-1] > sec_count or greedy_david[-1] > sec_count):
			break
		i+=1
	
	print(f'{i} was the first amount that took longer than {sec_count}')
	print(f'davids was slower for {sum_mine_faster} numbers')
	print(f'thats {100 * sum_mine_faster/len(domain)}% of the tests')
	
	plt.plot(greedy)
	plt.plot(greedy_david)
	plt.legend(["Greedy", "greedy_david"])
	plt.xlabel("value")
	plt.ylabel("time to compute")
	plt.savefig(f'change_making_timings/greedy_algorithm_times_sec_count_less_than__{sec_count}.png')
	os.system('say "computation complete"')
	plt.show()