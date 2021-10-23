def estimate_pi(n_iterations):
	'''
		Parameters:
			n_iterations (int): the number of iterations to use in the estimate of pi
			
		Returns:
			pi_estimate (float): the estimate of pi
	'''
	pi_estimate = 0
	for i in range(n_iterations):
		# print(f'adding {(-1)**i * 1 / (2*i + 1)}')
		pi_estimate += (-1)**i * 1 / (2*i + 1)
	return pi_estimate * 4


if __name__ == "__main__":
	print(estimate_pi(10000))
