import numpy as np
from numpy.linalg import inv, norm
from autograd import jacobian

def BFGS(f, df, x0, A0, max_iter=40, tol=1e-8):
	"""Minimize f using BFGS, given the derivative df, an
	initial guess x0, and an initial approx AO of D'2f (×0) ."""
	
	# Initialize
	done = False
	iters = 0
	# Count the number of iterations
	A_inv = inv(A0)
	# Initial approximate inverse Hessian
	x = x0 - A_inv @ df(x0) #x1
	s = x - x0 # s1
	while not done: # Main BFGS loop
		y = df(x) - df(x0) # Update y
		sy = s@y # This product is used several times
		Ay = A_inv @ y # This product is used several times
		#Approximiate the new inverse Hessian
		A_inv = (A_inv + ((sy + y @ Ay)/sy**2) * np.outer (s,s)- (np.outer(Ay, s) + np. outer (s, Ay)) /sy)
		x0 = x
		x = x0 - A_inv @ df(x0) # Update X.
		
		s = x - x0 # Update S
		iters += 1
		# Stopping criteria
		done = ((norm(s) < tol) or (norm(df(x)) < tol) or (np.abs (f(x) - f(x0)) < tol) or (iters >= max_iter))
	return x, (iters < max_iter), iters


if __name__ == "__main__":
	f1 = lambda x: x[0]**3 -3*x[0]**2 + x[1]**2
	x01 = np.array([0.1,0.])
	df1 = jacobian(f1)
	A01 = np.array([[1.,0.],[0.,1.]])
	print(BFGS(f1, df1, x01, A01, tol = 1e-5))


