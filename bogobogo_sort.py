import numpy as np
import time
import matplotlib.pyplot as plt

def bogobogo(liszt:list, level = 0, v = False):
	"""
		this ain't your grandmother's sorting algorithm

		Parameters:
			liszt (list):	the list to sort
			level (int): 	the current recursion level
			v (bool): 		whether or not to print the current list
		
		Returns:
			liszt(list): 	the sorted list
			iter(int): 		the total number of iterations used to sort the list 
							(including iterations used by lower recursion levels)
	"""
	
	# base case. list is of length one
	if len(liszt) <= 1:
		if v:
			[print(end = f"\t") for i in range(level)]
			print(liszt)
		return liszt, 0
	iter = 0
	while True:
		if v:
			[print(end = f"\t") for i in range(level)]
			print(liszt)
		iter += 1
		# get the first element for later
		l0 = liszt[0]

		# sort the last n-1 elements using bogobogo
		liszt, more_iter = bogobogo(liszt[1:], level+1, v = v)
		# reinsert the 0th element at the proper index
		liszt.insert(0,l0)
		iter += more_iter

		# if the oth element is less than the minimum of the rest of the list,
		# the entire list is sorted. return
		if liszt[0] < np.min(liszt[1:]):
			if v:
				[print(end = f"\t") for i in range(level)]
				print("sorted")
			return liszt, iter
		
		# otherwise, we randomize and try again
		np.random.shuffle(liszt)
		


if __name__ == "__main__":
	times = []
	iterations = []
	i = 0
	# basically, I wait for the user to get fed up with the algorithm, and keyboard quit it. 
	# Only then does the algorithm terminate. 
	# it's O(user's patience)
	while True:
		print(i)
		lsd = list(np.arange(i))
		np.random.shuffle(lsd)
		print(lsd)
		# print(lsd[:1])
		# print(lsd[1:])
		start = time.time()
		try:
			lsd, iter = bogobogo(lsd)
		except:
			break
		times.append(time.time() - start)
		iterations.append(iter)
		print(lsd, iter)
		i += 1

	plt.subplot(211)
	plt.plot(times)
	plt.title("Times for Bogobogo sort")
	plt.xlabel("length of input")
	plt.ylabel("time taken")
	plt.yscale('log')

	plt.subplot(212)
	plt.plot(iterations)
	plt.title("iterations for Bogobogo sort")
	plt.xlabel("length of input")
	plt.ylabel("iterations taken")
	plt.yscale('log')

	plt.tight_layout()
	plt.show()
