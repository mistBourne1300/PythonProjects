from scipy.stats import beta
from scipy.stats import uniform
from scipy.stats import norm
import matplotlib.pyplot as plt
import numpy as np

def normal_pdf(x):
	return 

domain = np.linspace(0,1)


sizes = [1,2,4,8,16,32]
for n in sizes:
	plt.subplot(121)
	plt.plot(domain, beta.pdf(domain, 1/2, 1/2), 'k', label = "Beta(1/2, 1/2)")
	m = 1/2 
	sigb = np.sqrt((1/8)/n)
	plt.plot(domain, norm.pdf(domain, m, sigb))
	xbars = []
	for i in range(1000):
		xbars.append(np.mean(beta.rvs(1/2, 1/2, size = n)))
	plt.hist(xbars, density = True)


	plt.subplot(122)
	plt.plot(domain, uniform.pdf(domain), label = "Uniform([0,1])")


	sigu = np.sqrt((1/12)/n)
	plt.plot(domain, norm.pdf(domain, m, sigu))
	xbars = []
	for i in range(1000):
		xbars.append(np.mean(uniform.rvs(0,1,size = n)))
	plt.hist(xbars, density = True)

	plt.show()


plt.subplot(121)
plt.plot(domain, beta.pdf(domain, 1/2, 1/2), 'k', label = "Beta(1/2, 1/2)")

plt.subplot(122)
plt.plot(domain, uniform.pdf(domain), label = "Uniform([0,1])")

for n in sizes:
	plt.subplot(121)

	m = 1/2 
	sigb = np.sqrt((1/8)/n)
	plt.plot(domain, norm.pdf(domain, m, sigb))
	xbars = []
	for i in range(1000):
		xbars.append(np.mean(beta.rvs(1/2, 1/2, size = n)))
	plt.hist(xbars, density = True)


	plt.subplot(122)

	sigu = np.sqrt((1/12)/n)
	plt.plot(domain, norm.pdf(domain, m, sigu))
	xbars = []
	for i in range(1000):
		xbars.append(np.mean(uniform.rvs(0,1,size = n)))
	plt.hist(xbars, density = True)







plt.show()