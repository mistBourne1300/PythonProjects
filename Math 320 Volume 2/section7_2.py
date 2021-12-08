

import numpy as np
from scipy.stats import beta, norm, truncnorm
from matplotlib import pyplot as plt
from scipy.stats import gamma, uniform
from scipy import stats
# Problem 7.6
def prob6():
	"""Calculate a Monte Carlo estimate of the given integral, along with
    the estimated standard error. Do this using a standard normal distribution
    as well as a normal distribution with mean 3 and standard deviation 1.

    Returns:
        est1 (float): Estimate of integral with standard normal
        se1 (float): Estimate of the standard error with standard normal
        est2 (float): Estimate of integral with other normal
        se2 (float): Estimate of the standard error with other normal
    """

	def func(x):
		return np.exp(-(x**2)/2)

	norm01 = truncnorm(3, 10**5)
	norm31 = truncnorm(0,10**5, loc = 3)
	sample_std = norm01.rvs(size=10**5)
	
	sample_shift = norm31.rvs(size=10**5)
	
	vect_func = np.vectorize(func)
	est1 = (1/(10**5)) * np.sum(vect_func(sample_std)/norm01.pdf(sample_std))
	se1 = np.var(sample_std)/np.sqrt(10**5)
	est2 = (1/(10**5)) * np.sum(vect_func(sample_shift)/norm31.pdf(sample_shift))
	se2 = np.var(sample_shift)/np.sqrt(10**5)
	return est1, se1, est2, se2



# Problem 7.7
def prob7(a, b, n):
	"""Use importance sampling to estimate the given integral. Your draws should
    come from the a Beta(a,b) distribution. You may need to run this function many
    times to find values of a and b that will give standard error less than 10^-3.

    Parameters:
        a (float): Parameter used in beta distribution
        b (float): Parameter used in beta distribution
        n (int): Number of samples

    Returns:
        est (float): Estimate of integral
        se (float): Estimate of the standard error
    """

	def func(u):
		return (2*np.pi)/((u/(2*np.pi))**3 + (u/(2*np.pi)) + 1)

	betaab = beta(a,b)
	sample = betaab.rvs(size=n)
	

	est = np.sum(func(sample)/betaab.pdf(sample))/n
	se = np.var(sample)/np.sqrt(n)
	print(np.min(sample))
	return est, se




# Problem 7.8iii
def prob8(n):
	"""Draw n times from Gamma(1,2) using the uniform distribution.

    Parameters:
        n (int): Number os samples to draw

    Returns:
        draw (list (float)): List of length n containing the draws
    """

	unif = beta(1,1)
	sample = unif.rvs(size=n)
	gamma12 = gamma(1, scale = 2)
	LAM = 2
	trans_sample = -np.log(sample)/2
	plt.hist(trans_sample, bins = 100, density = True)
	domain = np.linspace(0, np.max(trans_sample), 500)
	plt.plot(domain, gamma12.pdf(domain))
	plt.show()
	return trans_sample



# Problem 7.9ii-iii
def prob9():
	"""Draw 10^5 times from the logistic distribution. Plot a normed histogram
    of these draws. On the same graph, plot the pdf of the logistic distribution.

    Returns:
        mean (float): Estimate of the mean
        var (float): Estimate of the variance
    """
	def logi_pdf(x):
		return np.exp(-x)/( (1 + np.exp(-x))**2 )
	def f_inv(x):
		return -np.log(1/x - 1)
	
	unif = beta(1,1)
	sample = unif.rvs(size = 10**5)
	sample_trans = f_inv(sample)
	plt.hist(sample_trans, bins = 100, density = True)
	domain = np.linspace(-10,10,1000)
	plt.plot(domain, logi_pdf(domain))
	plt.show()
	return np.mean(sample_trans), np.var(sample_trans)

	


# Problem 7.10

def prob10():
	"""Estimate the volume of the unit ball in d-dimensional space using rejection
    sampling. Do this for d={1,..,10}. Pick numbers of samples so that the standard
    error is less than 10^-2. Return your estimates along with your choices of sample
    size and the corresponding standard errors.

    Returns:
        est (list (float)): List of estimates of the area of the unit ball in dimensions
            d={1,...10}
        se (list (float)): List of standard errors of the given estimates
        n (list (int)): List of number of samples used in the computation of the given
            estimates
    """
	dimensions = [1,2,3,4,5,6,7,8,9,10]
	unif = uniform(-1,2)
	est = []
	for d in dimensions:
		samples_list = []
		vol_cube = 2**d
		for i in range(d):
			samples_list.append(unif.rvs(size = 10**6))
		sample_mat = np.array(samples_list)
		lengths = np.linalg.norm(sample_mat, axis = 0)
		mask = lengths <= 1
		prob = np.sum(mask)/len(mask)
		estimate = prob*vol_cube
		print(f'dimension: {d} est: {estimate}')
		est.append(estimate)
	
	return est


# Problem 7.11iii-iv
def prob11(n):
	"""Use rejection sampling to make n draws from the distribution P. Recall that since
    you will be rejecting some draws from Gamma(1,1), you may need to make more than n
    draws from Gamma(1,1) to get n draws from P.

    Parameters:
        n (int): Number of draws from P to compute

    Returns:
        draw (list (float)): List of length n of draws from P
    """
	def func(x):
		return np.exp(-(x**2) - (x**3))
	gamma11 = gamma(1,1)
	unif = uniform(0,1)
	sample = []
	Z = .663711
	while len(sample) < n:
		z = gamma11.rvs(size=1)
		u = unif.rvs(size = 1)
		if u <= (func(z)/(2*gamma11.pdf(z))):
			#print(f"appending at length {len (sample)}")
			sample.append(z)
	
	sample = np.array(sample)-1
	plt.hist(sample, bins = 100, density = True)
	domain = np.linspace(0,np.max(sample), 500)
	plt.plot(domain, func(domain)/Z)
	plt.show()

if __name__ == "__main__":
	# print("\n\n***** Problem 6 *****")
	# print(prob6())

	# print("\n\n***** Problem 7 *****")
	# print(prob7(1,1,10**5))

	# print("\n\n***** Problem 8 *****")
	# print(prob8(100000))

	# print("\n\n***** Problem 9 *****")
	# print(prob9())

	# print("\n\n***** Problem 10 *****")
	# print(prob10())

	print("\n\n***** Problem 11 *****")
	prob11(1000)