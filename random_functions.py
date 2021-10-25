import random
import numpy as np


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

def random_point_in_unit_circle_cartesian_method():
	while True:
		x = random.random() * 2 - 1
		y = random.random() * 2 - 1
		if x**2 + y**2 <=1:
			return x,y

def non_random_point_in_unit_circle_polar_method():
	r = random.random()
	theta = random.random() * 2 * np.pi
	return r*np.cos(theta), r*np.sin(theta)

def random_point_in_unit_circle_polar_method():
	theta = random.random() * 2 * np.pi
	r = np.sqrt(random.random())
	return r*np.cos(theta), r*np.sin(theta)

if __name__ == "__main__":
	from matplotlib import pyplot as plt
	# print(estimate_pi(10000))
	points = []
	for i in range(1000):
		points.append(random_point_in_unit_circle_cartesian_method())
		plt.scatter(points[-1][0], points[-1][1], s=1)
	print(points)
	plt.show()

	points = []
	for i in range(1000):
		points.append(non_random_point_in_unit_circle_polar_method())
		plt.scatter(points[-1][0], points[-1][1], s=1)
	plt.show()

	points = []
	for i in range(1000):
		points.append(random_point_in_unit_circle_polar_method())
		plt.scatter(points[-1][0], points[-1][1], s=1)
	plt.show()
