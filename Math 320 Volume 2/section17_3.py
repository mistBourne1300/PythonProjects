import numpy as np
from scipy.stats import beta
import time
import matplotlib.pyplot as plt


import numpy as np
from scipy.stats import uniform

def pull(thetas, jackpots, action):
	wl = uniform.rvs()
	if wl <= thetas[action]:
		return jackpots[action], (1,0)
	return 0.0, (0,1)

def compute_r(M,r,Beta):
	little_boy = np.zeros((M+1,M+1))
	for a in range(M+1):
		b = M-a
		little_boy[a,b] = max(a/(a+b),r)/(1-Beta)
	
	for i in range(M-1,-1,-1):
		for a in range(i+1):
			b = i-a
			little_boy[a,b] = max( (a*(1 + Beta*little_boy[a+1,b]) + b*Beta*little_boy[a,b+1])/(a+b) ,r/(1-Beta))
	little_boy[0,0] = 0
	return little_boy

def gittens(jackpots, states, M, memoized_matrices:dict(), Beta=0.9):
	def get_abs_diff(r,a,b,temp_mat):
		return np.abs(r/(1-Beta) - (a/(a+b)*(1+Beta*temp_mat[a+1,b]) + b/(a+b)*Beta*temp_mat[a,b+1]))
	fat_man = np.ones(len(states))
	diffs = np.ones(len(states))
	for r,temp_mat in memoized_matrices.items():
		for i,s in enumerate(states):
			new_diff_val = get_abs_diff(r,s[0],s[1],temp_mat)
			if new_diff_val < diffs[i]:
				fat_man[i] = r
				diffs[i] = new_diff_val
	return [jackpots[i]*fat_man[i] for i in range(len(jackpots))]

def simulacrum(thetas, jackpots, K,T,M, Beta = 0.9):
	states = [[1,1] for i in range(len(thetas))]
	memoized_matrices = {r:compute_r(M,r,Beta) for r in np.linspace(0,1,K)}
	payout_potatoes = 0
	for i in range(T):
		arm = np.argmax(gittens(jackpots, states, M, memoized_matrices, Beta))
		print(i,":",arm)
		payout, state = pull(thetas, jackpots, arm)
		payout_potatoes += payout
		states[arm][0] += state[0]
		states[arm][1] += state[1]
		print(states)
	
	est_probs = [s[0]/(s[0] + s[1]) for s in states]
	return est_probs, payout_potatoes

def thompson(thetas, N, jackpots = None, Beta = 0.9, animate = False):
	domain = np.linspace(0,1,500)
	n = len(thetas)
	a = np.ones(n)
	b = np.ones(n)
	if not jackpots:
		jackpots = np.ones(n)
	x_axis = np.zeros(n)
	X = np.random.random(N)
	traj = np.zeros(N)
	for k in range(N):
		draw = beta.rvs(a,b)
		index = np.argmax(draw*jackpots)
		if animate:
			for i in range(n):
				# plot beta of arm i
				dist = beta(a[i],b[i])
				plt.plot(domain, dist.pdf(domain))
				# plt.plot(draw[i], dist.pdf(draw[i]), '.')
			plt.plot(draw, x_axis, '.')
			plt.title(f'T = {k}/{N} ({100*k/N:.0f}%)')
			plt.show(block = False)
			plt.pause(1/N)
			plt.close()
		
		
		if X[k] <= thetas[index]:
			a[index] += 1
			traj[k] = traj[k-1] + (jackpots[index] * (Beta**k))
		else:
			b[index] += 1
			traj[k] = traj[k-1]
	return traj/np.arange(1,N+1), traj[-1]

def AB_testing(thetas, jackpots, m, N, Beta = 0.9):
	n = len(thetas)
	payout = 0
	if n*m > N:
		raise ValueError(f"nm > N: {n*m} > {N}")
	
	a = np.zeros(n)
	b = np.zeros(n)
	counter = 0
	for arm in range(n):
		for i in range(m):
			pay, state = pull(thetas, jackpots, arm)
			payout += pay * (Beta**counter)
			counter += 1
			a[arm] += state[0]
			b[arm] += state[1]
	to_pull = np.argmax(a/(a+b))
	for i in range(N-n*m):
		pay, _ = pull(thetas, jackpots, to_pull)
		payout+= pay * (Beta**counter)
		counter += 1

	return payout




def test_thompson_gittins_times():
	T = 100
	K = 100
	M = T+1
	jackpots = [1,1,1]

	thetas = [.2,.5,.7]
	gittins_time = []
	thompson_time = []

	for i in range(20):
		print(i, end = "\r")
		start = time.time()
		est_probs, payout = simulacrum(thetas, jackpots, K, T, M)
		gittins_time.append(time.time() - start)

		start = time.time()
		t_est_probs = thompson(thetas,T)
		thompson_time.append(time.time() - start)

	print(f'thompson avg time: {np.mean(thompson_time)}')
	print(f'gittins avg time: {np.mean(gittins_time)}')

def test_AB_testing():
	N = 100
	m = 20
	jackpots = [1,1,1]

	thetas = [.2,.5,.7]
	print(f'thompson: {thompson(thetas,N)[-1]}')

	print(f'AB_testing: {AB_testing(thetas, jackpots, m, N)}')

def test_beta_discounted():
	N = 100
	m = 20
	jackpots = [1,1,1]
	thetas = [.2,.5,.7]

	print(f'thompson: {thompson(thetas,N)[-1]}')
	print(f'AB_testing: {AB_testing(thetas, jackpots, m,N)}')

def thompson_animation():
	T = 1000
	jackpots = [1,1,1,1,1]

	thetas = [.2,.6,.7,.9,.05]
	start = time.time()
	thompson(thetas, T, jackpots = jackpots, animate=True)
	print(f'{T} iters took {time.time() - start:.3f} seconds')


if __name__ == "__main__":
	# print("\nThompson time vs Gittins time:")
	# test_thompson_gittins_times()
	# print('\nAB testing vs Thompson payout:')
	# test_AB_testing()
	# print('\nAB testing vs Thompson payout -- discounted:')
	# test_beta_discounted()

	print("\nAnimated Thompson:")
	thompson_animation()
