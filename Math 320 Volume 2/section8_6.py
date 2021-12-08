import numpy as np
import matplotlib.pyplot as plt
from scipy.fftpack import fft, ifft

f = lambda x: x
g = lambda x: np.sin(x)
n=1000
domain = np.linspace(0,10*np.pi, n)
fx = f(domain)
gx = g(domain)
convolution = 1/n*ifft(fft(fx) * fft(gx))
haadamard = fx*gx
plt.subplot(221)
plt.plot(domain, fx)
plt.title("f(x) = x")

plt.subplot(222)
plt.plot(domain, gx)
plt.title("g(x) = sin(x)")

plt.subplot(223)
plt.plot(domain, convolution)
plt.title("f*g(x)")

plt.subplot(224)
plt.plot(domain, haadamard)
plt.title("haadamard product")

plt.show()

plt.plot(domain, fx)
plt.plot(domain, gx)
plt.plot(domain, convolution)
plt.plot(domain, haadamard)
plt.legend(["f(x)", "g(x)", "f*g(x)", "haadamard"])
plt.show()