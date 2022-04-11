import numpy as np
from scipy.stats import uniform

def pull(thetas, jackpots, action):
	wl = uniform.rvs()
	if wl <= thetas[action]:
		return jackpots[action], (1,0)
	return 0.0, (0,1)

def compute_r(M,r,beta):
	little_boy = np.zeros((M+1,M+1))
	for a in range(M+1):
		b = M-a
		little_boy[a,b] = max(a/(a+b),r)/(1-beta)
	
	for i in range(M-1,-1,-1):
		for a in range(i+1):
			b = i-a
			little_boy[a,b] = max( (a*(1 + beta*little_boy[a+1,b]) + b*beta*little_boy[a,b+1])/(a+b) ,r/(1-beta))
	little_boy[0,0] = 0
	return little_boy

def gittens(jackpots, states, M, K, beta=0.9):
	def get_abs_diff(r,a,b,temp_mat):
		return np.abs(r/(1-beta) - (a/(a+b)*(1+beta*temp_mat[a+1,b]) + b/(a+b)*beta*temp_mat[a,b+1]))
	fat_man = np.ones(len(states))
	diffs = np.ones(len(states))
	for r in np.linspace(0,1,K):
		temp_mat = compute_r(M,r,beta)
		for i,s in enumerate(states):
			new_diff_val = get_abs_diff(r,s[0],s[1],temp_mat)
			if new_diff_val < diffs[i]:
				fat_man[i] = r
				diffs[i] = new_diff_val
	return [jackpots[i]*fat_man[i] for i in range(len(jackpots))]

def simulacrum(thetas, jackpots, K,T,M, beta = 0.9):
	states = [[1,1] for i in range(len(thetas))]
	payout_potatoes = 0
	for i in range(T):
		arm = np.argmax(gittens(jackpots, states, M,K, beta))
		print(i,":",arm)
		payout, state = pull(thetas, jackpots, arm)
		payout_potatoes += payout
		states[arm][0] += state[0]
		states[arm][1] += state[1]
		print(states)
	
	est_probs = [s[0]/(s[0] + s[1]) for s in states]
	return est_probs, payout_potatoes

if __name__ == "__main__":

	M = 101
	T = 100
	K = 100
	jackpots = [1,2,3,4,5,6,7,8,9]

	thetas = [.9,.8,.7,.6,.5,.4,.3,.2,.1]

	print(simulacrum(thetas, jackpots, K, T, M))
