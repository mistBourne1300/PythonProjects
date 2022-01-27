from turtle import back, forward
import numpy as np
import matplotlib.pyplot as plt


def prob2():

	totally_not_unrepresentable = 2**53


	for i in range(-3, 5):
		print(f'{totally_not_unrepresentable + i}:  {float(totally_not_unrepresentable + i)}') 


def prob3():
	print(1/3)

def prob4():
	forward_sum = 0
	backward_sum = 0
	N = 10**7
	for n in range(1,N+1):
		forward_sum += 1000/n
		backward_sum += 1000/(N + 1 - n)
	
	print(f'forward: {forward_sum}')
	print(f'backward: {backward_sum}')

def prob5():
	"""	The graph of (1 - x) - 1 looks jagged because we are on the inner limits of the floating point numbers. 
		It jumps because the each x-value rounds to the nearest floating point number.
		The ratio gets more jagged  as x->0 because the little jumps in the floating point become larger 
		relative to the actual distance away from the true value. """
	f = lambda x: (1 - x) - 1
	ratio = lambda x: ((1 - x) - 1)/x
	domain = np.linspace(-3e-15, 3e-15, 1000)
	plt.subplot(211)
	plt.plot(domain, f(domain), 'goldenrod') 
	plt.plot(domain, domain, 'tomato')
	plt.legend(['(1 - x) - 1', 'x'])
	plt.subplot(212)
	plt.plot(domain, ratio(domain), 'mediumseagreen')
	plt.legend(['ratio'])
	plt.show()



if __name__ == "__main__":
	print("\n\n\n") # beginning of file print
	[print('*', end = '') for i in range(50)]
	print(f'\nProblem 2:\n')
	prob2()
	print("\n\n")
	

	[print('*', end = '') for i in range(50)]
	print(f'\nProblem 3:\n')
	prob3()
	print("\n\n")
	
	[print('*', end = '') for i in range(50)]
	print("\nProblem 4:\n")
	prob4()
	print("\n\n")


	[print('*', end = '') for i in range(50)]


	prob5()
	print("\n\n\n") # eof print