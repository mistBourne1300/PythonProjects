import numpy as np
from autograd import grad
from autograd import numpy as anp

def newtons(f, x0, tol = 1e-10, maxiter = 100, v = False):
	x0 = float(x0)
	df = grad(f)
	ddf = grad(df)
	print("here")
	counter = 0
	while counter < maxiter:
		x1 = x0 - df(x0)/ddf(x0)
		if v:
			print(x1)
		counter += 1
		if np.abs(x0 - x1) < tol:
			return x1, True, counter
		x0 = x1
	return x1, False, counter

def log(b, a, tol = 1e-16, maxiter = 100):
	f = lambda x: (b**x) - a
	y0 = 1
	y1 = 3
	for i in range(maxiter):
		# print(i)
		y2 = y1 - f(y1)*(y1-y0)/(f(y1) - f(y0))
		# print(y2,y1,np.abs(y2-y1))
		if np.abs(y2 - y1) < tol:
			return y2, True, i

		y0 = y1
		y1 = y2
	return y2, False, maxiter


if __name__ == "__main__":
	f = lambda x: x**4 + 1
	# df = grad(f)
	# print(df(0.))
	# print(newtons(f,1,v = True))

	for n in np.arange(1,129):
		mine = log(2,n)[0]
		pies = np.log2(n)
		print(f'{n}: mine: {mine}, numpy\'s: {pies}, error: {np.abs(mine-pies)}')
