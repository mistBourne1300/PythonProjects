# Exercise 4.1 and 4.2 and 4.3

from abc import get_cache_token
import time
import os
import matplotlib.pyplot as plt
# Problem 4.1
""" Code up the naive, the memoized, and the bottom-up dynamic programming
    algorithms for computing the Fibonacci number F(n) for n in N (the natural numbers).
    Time all three mehtods and compare their performance for n in {1, 2,..., 40}.
    Experiment to find the largest value of n for which each of the three algorithms gives
    an answer in less than one minute.

    Write down your findings on the piece of paper you turn in. """

# The larget value of n for which it takes the naive_Fibonacci function less than a minute to solve is 41.
# As the value of n increases, naive_Fibonacci skyrockets, and is impractical for any n > 32 (it starts taking
# more than a second for n > 32). The memoized approach and the iterative approach both take very little time,
# comparitave to the naive approach, solving for n = 998 in less than one hundreth of a second. However, at n = 999,
# the recursive solution reaches maximum recursion depth and throws an error. Thus, for an arbitrary n, the best solution 
# must be the bottom-up solution.

def naive_Fibonacci(n):
    #print("fib(", n, ")", sep = "")
	if(n == 0 or n == 1):
		return n
	return naive_Fibonacci(n-1) + naive_Fibonacci(n-2)

def memoized_Fibonacci(n, dictionary = dict([])):
    #print(f'fib_memo({n})')
	if(n in dictionary):
		return dictionary[n]
	elif(n == 0 or n == 1):
		dictionary[n] = n
		return n
	dictionary[n] = memoized_Fibonacci(n-1, dictionary) + memoized_Fibonacci(n-2, dictionary)
	return dictionary[n]

def bottom_up_Fibonacci(n):
	ith_fib = 0
	ith_plus_1_fib = 1
	nth_fib = 0
	for i in range(n):
		#print(ith_fib)
		nth_fib = ith_fib + ith_plus_1_fib
		ith_fib = ith_plus_1_fib
		ith_plus_1_fib = nth_fib
	return ith_fib

# Problem 4.2
""" Code up both the naive recursion and the bottom-up dynamic programming algorithm
    to compute the optimal number n(v) of coins in the change-making problem for v cents
    and an arbitrary coinage system C (a set of coin values, in cents). Adapt your code to
    also return the optimal configuration of coins summing up to v. Time both methods and
    compare their performance on each of the values v in {1, 2,..., 1999} for the current
    U.S. coinage system where C = {1, 5, 10, 25, 50, 100}. It is acceptable to stop your code
    for values that take more than one minute to run.

    Write down your findings on the piece of paper you turn in. """

# the code in __main__ double checks whether the optimal solution is the same as the greedy solution for all values {0...1999} 
# the plt plot shows the timings for those 



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


# Problem 4.3
""" Code up a greedy version of the change-making problem. For the U.S. coinage system, verify
    that the greedy solution is the same as the optimal solution for all values v in {1, 2,..., 1999}.
    Time your code for the greedy solution on those values and compare your answers with those in
    Exercise 4.2.

    Write down your findings on the piece of paper you turn in. """

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
    


if __name__ == "__main__":
	# You can run test code in this block
	US_system = [1,5,10,25,50,100]
	greedy_change_times = []
	optimal_change_times = []
	greedy_change_amounts = []
	optimal_change_amounts = []
	domain = range(20000)
	for i  in domain:
		greedy_change_amount, i_solved = greedy_change(i, US_system)
		print(f'greedy:\n\t{i_solved}')
	
	os.system('say "greedy done, press enter to continue"')
	input("Press enter to continue:")

	for i in domain:
		print(f'testing {i}:')
		start_time = time.time()
		greedy_change_amount, i_solved = greedy_change(i, US_system)
		greedy_change_amounts.append(greedy_change_amount)
		greedy_change_times.append(time.time() - start_time)
		print(f'greedy:\n\t{i_solved}')
		

		start_time = time.time()
		optimal_change_amount = bottom_up_change(i, US_system)
		optimal_change_amounts.append(optimal_change_amount)
		optimal_change_times.append(time.time() - start_time)

	
	for i in range(len(greedy_change_amounts)):
		# print(f'greedy_change_amounts[{i}] = {greedy_change_amounts[i]}', end = " ")
		# print(f'optimal_change_amounts[{i}] = {optimal_change_amounts[i]}', end = " ")
		# print(f'equality: {greedy_change_amounts[i] == optimal_change_amounts[i]}\n')
		if(greedy_change_amounts[i] != optimal_change_amounts[i]):
			os.system(f'say "equality failed for {i}"')
			break
			# input("press enter to continue")

	plt.plot(domain, greedy_change_times)
	plt.plot(domain, optimal_change_times)
	plt.xlabel("Money Amount")
	plt.ylabel("Time to compute cents")
	plt.legend(["Greedy Algorithm", "Optimal Algorithm"])
	os.system('say "testing complete"')
	plt.show()
	# print(greedy_change_times, "\n\n\n")
	# print(optimal_change_times)