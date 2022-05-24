# do something with 
import numpy as np
import matplotlib.pyplot as plt
import time



gold = (1+np.sqrt(5))/2

binet = lambda n: (gold**n - (1-gold)**n)/np.sqrt(5)

lower = -5
upper = 5

domain = np.linspace(lower, upper, 1000)



# for i in domain:
# 	print(f'{i}: {binet(complex(i,0))}')

pants_on_fire = np.array([binet(complex(n,0)) for n in domain])

plt.plot(pants_on_fire.real, pants_on_fire.imag)
plt.title(f"parametrized fractional fibonacci numbers: ({lower}, {upper})")
plt.xlabel("real component")
plt.ylabel("imaginary component")
plt.show()