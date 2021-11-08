import numpy as np


means = []
for i in range(100):
	flips = []
	for j in range(1000):
		flips.append(np.random.choice([0,1]))
	means.append(np.mean(flips))
print(f'means: {means}')

epsilons = [.1, .01, .001]

proportions = []
for e in epsilons:
	within_e = []
	for m in means:
		within_e.append(np.abs(m-.5) >= e)
	proportions.append(np.mean(within_e))

print(f'proportions (bernoulli): {proportions}')


from scipy.stats import beta

means = []
for i in range(100):
	means.append(np.mean(beta.rvs(1,9,size=1000)))
# print(f'means: {means}')

epsilons = [.1, .01, .001]

proportions = []
for e in epsilons:
	within_e = []
	for m in means:
		within_e.append(np.abs(m-.1) >= e)
	proportions.append(np.mean(within_e))

print(f'proportions (beta): {proportions}')