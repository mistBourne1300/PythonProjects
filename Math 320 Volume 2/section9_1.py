import numpy as np
import matplotlib.pyplot as plt
from math import comb

def burn(n,k,x):
	return comb(n,k) * (x**k) * ((1-x)**(n-k))

def bernstein(f,n, x):
	sum = np.zeros(len(x))
	for k in range(n+1):
		sum = sum + (f(k/n) * burn(n,k,x))
	
	return sum

def func(x):
	return (x**2)*np.sin(2*np.pi*x + np.pi)

if __name__ == "__main__":
	domain = np.linspace(0,1)
	f_range = func(domain)
	plt.subplot(221)
	plt.plot(domain, f_range,'r')
	b_range = bernstein(func,4,domain)
	plt.plot(domain,b_range,'k')
	plt.title("n = 4")

	plt.subplot(222)
	plt.plot(domain, f_range,'r')
	b_range = bernstein(func,10,domain)
	plt.plot(domain,b_range,'k')
	plt.title("n = 10")

	plt.subplot(223)
	plt.plot(domain, f_range,'r')
	b_range = bernstein(func,50,domain)
	plt.plot(domain,b_range,'k')
	plt.title("n = 50")

	plt.subplot(224)
	plt.plot(domain, f_range,'r')
	b_range = bernstein(func,200,domain)
	plt.plot(domain,b_range,'k')
	plt.title("n = 200")

	plt.tight_layout()
	plt.show()