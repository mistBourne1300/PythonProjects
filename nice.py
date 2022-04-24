from itertools import combinations
import matplotlib.pyplot as plt
import numpy as np




def powerset(iter):
	s = list(iter)
	returnme = []
	for r in range(len(s) + 1):
		for combo in combinations(s,r):
			# print(combo)
			returnme.append(combo)

	return returnme

def calc_percent_sum_69(iter):
	total_sums = 0 
	p_set = powerset(iter)
	for s in p_set:
		if sum(s) == 69:
			total_sums += 1
	return total_sums/len(p_set)

if __name__ == "__main__":
	percentages = []
	try:
		counter = 0
		while True:
			print(counter, 2**counter, end = "\r")
			percentages.append(calc_percent_sum_69([i for i in range(counter)]))
			counter += 1
	except KeyboardInterrupt:
		best = np.argmin(np.abs(np.array(percentages) - np.array([.69 for i in range(len(percentages))])))
		print(f'the best set is {best} with a percentage of {percentages[best]}. heres the set')
		s = [i for i in range(best)]
		print(s)
		# print(powerset(s))
		print(f"({calc_percent_sum_69(s)}) percent")