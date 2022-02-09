import numpy as np
from autograd import jacobian, grad
from autograd import numpy as anp
from scipy import linalg as la


def prob_20(f, x0, tol = 1e-5, maxiter = 100):

	def newton(f, x0, Df, tol=1e-5, maxiter=15, alpha=1.):
		"""Use Newton's method to approximate a zero of the function f.

		Parameters:
			f (function): a function from R^n to R^n (assume n=1 until Problem 5).
			x0 (float or ndarray): The initial guess for the zero of f.
			Df (function): The derivative of f, a function from R^n to R^(nxn).
			tol (float): Convergence tolerance. The function should returns when
				the difference between successive approximations is less than tol.
			maxiter (int): The maximum number of iterations to compute.
			alpha (float): Backtracking scalar (Problem 3).

		Returns:
			(float or ndarray): The approximation for a zero of f.
			(bool): Whether or not Newton's method converged.
			(int): The number of iterations computed.
		"""
		if np.isscalar(x0):
			x1 = x0 - alpha*f(x0)/Df(x0)
			counter = 0
			while np.abs(x1-x0) > tol:
				x0 = x1
				x1 = x0 - alpha*f(x0)/Df(x0)
				counter += 1
				if counter > maxiter:
					return x1, False, counter
			return x1, True, counter
		else:
			x1 = x0 - alpha*la.solve(Df(x0), f(x0))
			counter = 0
			while counter < maxiter:
				x0 = x1
				x1 = x0 - alpha*la.solve(Df(x0), f(x0))
				counter += 1
				if la.norm(x0-x1) < tol:
					return x1, True, counter
			
			return x1, False, counter
	
	df = jacobian(f)
	ddf = jacobian(df)
	return newton(df, x0, ddf, tol = tol, maxiter = maxiter)

def prob_23(r, x0, tol = 1e-5, maxiter = 100):
	
	dr = jacobian(r)

	for i in range(maxiter):
		J = dr(x0).T
		x1 = x0 - la.solve(J@J.T, J@r(x0))

		if la.norm(x1 - x0) < tol:
			return x1, True, i

		x0 = x1

	return x1, False, i
if __name__ == "__main__":
	# para = lambda x: 100*(x[1] - x[0]**2)**2 + (1-x[0])**2
	# x0 = anp.array([-2.,2.])

	# print(prob_20(para, x0))

	a = anp.array([[0.,0.], [1.,1.], [2.,0.], [-1.,3.]])
	x0 = anp.array([2.,1e-10])
	d = anp.array([3.88506517, 2.87540403, 3.10537735, 3.99674185])
	a = anp.array([[0.,0.], [1.,1.], [2.,0.], [-1.,3.]])

	r0 = lambda x: d[0] - anp.linalg.norm(x - a[0])
	r1 = lambda x: d[1] - anp.linalg.norm(x - a[1])
	r2 = lambda x: d[2] - anp.linalg.norm(x - a[2])
	r3 = lambda x: d[3] - anp.linalg.norm(x - a[3])

	r = lambda x: anp.array([r0(x), r1(x), r2(x), r3(x)])
	
	print(prob_23(r, x0,))