import numpy as np
from scipy.fftpack import fft
import matplotlib.pyplot as plt

f = lambda x: np.where(x<0, 1+x, x)

runge = lambda x: 1/(1+25*x**2)

def cheby(f,n):
	y = np.cos((np.pi * np.arange(2*n)) / n)
	samples = f(y)
	coeffs = np.real(fft(samples))[:n+1] / n
	coeffs[0] /= 2
	coeffs[n] /= 2

	return coeffs

def interpol(f, n, x):
	a = cheby(f,n)
	
	
	
	un1 = 0
	un = a[-1]
	for k in range(1,n+1):
		uk = 2*x*un - un1 + a[n-k]
		if k != n: un1 = un
		un = uk
	

	return 1/2*(a[0] + un - un1)



if __name__ == "__main__":
	domain = np.linspace(-1,1, 1000)
	for k in range(1,10):
		plt.subplot(3,3,k)
		plt.plot(domain, interpol(f,2**k,domain))
		plt.plot(domain,f(domain))
	plt.suptitle("Chebyshex interpolation of np.where(x<0, 1+x, x)")
	plt.show()


