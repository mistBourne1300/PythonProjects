import numpy as np
from scipy.fftpack import fft
import matplotlib.pyplot as plt

def func(x):
	return 1-3*np.sin(12*np.pi*x+7)+5*np.sin(2*np.pi*x-1)+5*np.sin(4*np.pi*x-3)

#problem 8.33
def problem33a(nu,n,T,f):
	domain = np.linspace(0,(n-1)*T/n,n)
	samples = f(domain)
	fhat = fft(samples)/n
	coef = []
	for k in range(-nu,nu+1):
		if k<0:
			coef.append(fhat[k+n])
		else:
			coef.append(fhat[k])
		
	return np.array(coef)

def problem33b(nu,n,T,f):
	coef = problem33a(nu,n,T,f)
	def g(x):
		sum = 0
		k = -nu
		for c in coef:
			sum += c*np.exp(1j * (2*np.pi/T) * k * x)
			k+=1
		return sum
	
	return g




if __name__ == "__main__":
	print(problem33a(1,3,1,func))

	enns = [3,7,11,13]
	T = 1
	for n in enns:
		domain = np.linspace(0,T,500)
		sam_dom = np.linspace(0,(n-1)*T/n,n)
		sample = func(sam_dom)
		gt = problem33b(n//2,n,T,func)
		plt.plot(domain, func(domain))
		plt.plot(domain, gt(domain))
		plt.scatter(sam_dom, sample)
		plt.title(f'sample of {n} points')
		plt.show()