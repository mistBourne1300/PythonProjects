import numpy as np
import time
from autograd import grad, elementwise_grad
import scipy.optimize as opt


def quad_exact_grad_descent(x0, b, Q, tol = 1e-5):
	# i = 0
	while True:
		# print(i, x0)
		# time.sleep(1)
		# i+=1
		df0 = x0.T@Q.T - b.T
		if np.linalg.norm(df0.T, ord = np.inf) < tol:
			return x0
		a0 = (df0@df0.T)/(df0@Q@df0.T)
		x1 = x0 - a0*df0.T
		x0 = x1


def exact_grad_descent(f, x0, tol = 1e-6):
	df = grad(f)
	i = 0
	while True:
		print(i, x0)
		i += 1
		df0 = df(x0)
		phi = lambda a: f(x0 - a*df0.T)
		alpha = opt.newton(elementwise_grad(phi), 1, maxiter = 9001)
		x1 = x0 - alpha*df0.T
		if(np.linalg.norm(df0.T) < tol):
			return x0
		x0 = x1




if __name__ == "__main__":
	Q = np.array([	[100.,0.],
					[0.,10.]])
	
	x0 = np.array([-2.,2.])

	b = np.array([0.,1.])

	print(quad_exact_grad_descent(x0,b,Q))

	print("problem 14:")
	para = lambda x: 100*(x[1] - x[0]**2)**2 + (1-x[0])**2

	print(exact_grad_descent(para, x0))