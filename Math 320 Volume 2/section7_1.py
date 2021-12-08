from scipy.stats import norm, chi2, uniform, beta
import matplotlib.pyplot as plt
import numpy as np



def problem1(k):
	num_samples = 10**k
	print(f"\n\n\tSAMPLE OF {num_samples}")
	NUM_BINS = 10*k
	cdf_x = [.5, 1, 1.5]
	df = 1
	exxes = norm.rvs(0,1,size = num_samples)**2 # sample from the normal distribution, then square the sample to get chi-squared
	plt.subplot(121)
	plt.hist(exxes, bins = NUM_BINS, density=True)
	plt.title("random sampling")
	sample_mean = np.mean(exxes)
	sample_var = np.var(exxes)
	plt.xlabel(f'E[X]: {sample_mean}\nVar(X): {sample_var}')

	print("\nCalculated cdf:")
	for x in cdf_x:
		mask = exxes < x
		prob = np.sum(mask) / num_samples
		print(f'prob(X<{x}) = {prob}')

	
	
	plt.subplot(122)
	domain = np.linspace(0,np.max(exxes))
	plt.plot(domain, chi2.pdf(domain, df))
	plt.title("scipy chi square")
	plt.ylim(0)
	plt.xlim(0)
	mean, var = chi2.stats(df, moments = 'mv')
	plt.xlabel(f'E[X]: {mean}\nVar(X): {var}')


	print('\nActual cdf:')
	for x in cdf_x:
		print(f'prob(X<{x}) = {chi2.cdf(x, df)}')

	plt.suptitle(f'Chi squared with {num_samples} samples')
	plt.show()
	
def problem2(k):
	num_samples = 10**k
	print(f"\n\n\tSAMPLE OF {num_samples}")
	unif = uniform(loc = -1, scale = 2)
	exxes = unif.rvs(num_samples)
	whys = unif.rvs(num_samples)
	mask = exxes**2 + whys**2 <= 1
	prob = np.sum(mask)/num_samples
	approx_pi = 4 * prob
	print(f'\ncalculated pi: {approx_pi}; diff: {approx_pi - np.pi}')

def problem3_1(k):
	num_samples = 10**k
	unif = uniform(0,2)
	exxes = unif.rvs(num_samples)
	return 2*np.mean(exxes), np.var(exxes)/np.sqrt(num_samples)

def problem3_2(k):
	BOXAREA = 2*np.e
	num_samples = 10**k
	unif02 = uniform(0,2) # get the uniform distribution on [0,2]
	unif0e = uniform(0,np.e) # get the uniform distribution on [0,e], since h(x) has a max value of e
	exxes = unif02.rvs(num_samples) # get num_samples x values
	whys = unif0e.rvs(num_samples) # get num_samples y values
	mask = np.exp(np.cos(exxes**2)) < whys # determine if each (x,y) pair is under the curve
	prob = np.sum(mask)/num_samples # calculate the probability of a point landing under the curve
	return BOXAREA*prob

def problem4(k):
	num_samples = 10**k
	print(f"\n\n\tSAMPLE OF {num_samples}")
	beta25 = beta(2,5)
	beta2055 = beta(20,55)
	sample25 = beta25.rvs(num_samples)
	sample2055 = beta2055.rvs(num_samples)
	mask = sample25 < sample2055
	prob = np.sum(mask)/num_samples
	return prob

def problem5(iter):
	'''here, k is the number of 10-round games to play'''
	print(f"\n\n\tSAMPLE OF {iter}")
	die = [1,2,3,4]
	money_vect = []
	for i in range(iter):
		money = 0
		for j in range(10):
			roll = np.random.choice(die)
			if roll == 4: money -= 1
			if roll == 3: money += 2
			if roll == 1 or roll == 2: money += 1
		money_vect.append(money)
	mask = np.array(money_vect) < 0
	return np.sum(mask)/iter




if __name__ == "__main__":

	kiss = [2,4,6] # every kiss begins with k
	
	print("\n\n\n************ Problem 1 ************")
	for k in kiss:
		problem1(k)
	
	print("\n\n\n************ Problem 2 ************")
	for k in kiss:
		problem2(k)
	

	print("\n\n\n************ Problem 3 ************")
	for k in kiss:
		integral, var = problem3_1(k)
		print(f"\n\n\tSAMPLE OF {10**k}")
		print(f'\nmethod 1:')
		print(f'estimated value: {integral}; std err: {var}')

		integral = problem3_2(k)
		print(f'method 2:')
		print(f'estimated value: {integral}; std err: {None}')
	
	print("\n\n\n************ Problem 4 ************")
	for k in kiss:
		est_prob = problem4(k)
		print(f'estimated probability: {est_prob}')
	
	print("\n\n\n************ Problem 5 ************")
	for i in range(1000, 10000, 1000):
		est_prob = problem5(i)
		print(f'estimated probability: {est_prob}')

	
	





	

