import matplotlib.pyplot as plt
import numpy as np
from time import time
from autograd import grad
from autograd import numpy as anp



def forward_diff(n, f, x, h = 2*np.sqrt(np.finfo(float).eps)):
	I = np.identity(len(x))
	Jacob = []
	for i in range(len(f(x))):
		ithrow = []
		for ej in I:
			ithrow.append((f(x+h*ej)[i] - f(x)[i])/(h))
		
		Jacob.append(ithrow)
	return np.array(Jacob)

def centered_diff(n, f, x, h = 1.4*np.cbrt(np.finfo(float).eps)):
	I = np.identity(len(x))
	Jacob = []
	for i in range(len(f(x))):
		ithrow = []
		for ej in I:
			ithrow.append((f(x+h*ej)[i] - f(x-h*ej)[i])/(2*h))
		
		Jacob.append(ithrow)
	return np.array(Jacob)

def complex_step(n, f, x, h = np.finfo(float).eps):
	return f(x + 1j*h).imag/h

def prob16():
	f = lambda x: np.array([x[0]/(x[0] + 2 + x[1]**2), x[1]/(x[0]**2 + x[1]**2)])
	point = np.array([2,3])
	# print(forward_diff(1, f, point))

	correctomundo = np.array(	[[11/169, -12/169],
								[-12/169, -5/169]])

	errors = []
	values = 2.**(-np.arange(2,54))
	times = []

	for h in values:
		start = time()
		approx = forward_diff(1, f, point, h)
		times.append(time() - start)
		errors.append(np.linalg.norm(correctomundo - approx))
		print(f'error: {errors[-1]}')


	# plot h value v time
	plt.subplot(211)
	plt.plot(values, times)
	plt.xlabel('h value')
	plt.ylabel('computation time')
	plt.xscale('log', base = 2)
	plt.title('Time for forward difference quotients')

	# plot h value v error
	plt.subplot(212)
	plt.plot(values, errors)
	plt.xlabel('h value')
	plt.ylabel('error')
	plt.xscale('log', base = 2)
	plt.title('Error for forward difference quotients')
	plt.tight_layout()
	plt.show()


	print("\n\nProblem 16: ")
	print(f'least time h (forward): 2^{np.log2(values[np.argmin(times)])}')
	print(f'minimum error h (forward): 2^{np.log2(values[np.argmin(errors)])}\n\n')

def prob17():
	f = lambda x: np.array([x[0]/(x[0] + 2 + x[1]**2), x[1]/(x[0]**2 + x[1]**2)])
	point = np.array([2,3])
	# pause = input(f'matrix of most accurate: \n{forward_diff(1, f, point, values[np.argmin(errors)])}')

	errors = []
	times = []

	correctomundo = np.array(	[[11/169, -12/169],
								[-12/169, -5/169]])

	errors = []
	values = 2.**(-np.arange(2,54))
	times = []

	for h in values:
		start = time()
		approx = centered_diff(1, f, point, h)
		times.append(time() - start)

		errors.append(np.linalg.norm(correctomundo - approx))

	plt.subplot(211)
	plt.plot(values, times)
	plt.xlabel('h value')
	plt.ylabel('computation time')
	plt.xscale('log', base = 2)
	plt.title('Time for centered difference quotients')

	plt.subplot(212)
	plt.plot(values, errors)
	plt.xlabel('h value')
	plt.ylabel('error')
	plt.xscale('log', base = 2)
	plt.title('Error for centered difference quotients')
	plt.tight_layout()
	plt.show()

	print("\n\nProblem 17:")
	print(f'least time h (centered): 2^{np.log2(values[np.argmin(times)])}')
	print(f'minimum error h (centered): 2^{np.log2(values[np.argmin(errors)])}\n\n')

def prob18():
	f = lambda x: np.array([((np.sin(x))**3 + np.cos(x))/np.exp(x)])
	f_a = lambda x: ((anp.sin(x))**3 + anp.cos(x))/anp.exp(x)
	x0 = np.array([1.5])
	x0_a = 1.5

	for_err = []
	cent_err = []
	comp_err = []
	

	for_time = []
	cent_time = []
	comp_time = []

	correctomundo = -0.411985

	values = 2.**(-np.arange(2,54))

	start = time()
	auto_err = np.abs(grad(f_a)(x0_a) - correctomundo)
	auto_time = time() - start
	auto_err = [auto_err for i in range(len(values))]
	auto_time = [auto_time for i in range(len(values))]

	for h in values:
		start = time()
		approx = forward_diff(1,f,x0,h)
		for_time.append(time() - start)
		for_err.append(np.abs(correctomundo - approx[0][0]))

		start = time()
		approx = centered_diff(1,f,x0,h)
		cent_time.append(time() - start)
		cent_err.append(np.abs(correctomundo - approx[0][0])) # approx is a one-element matrix, so I need the first (and only) entry

		start = time()
		approx = complex_step(1,f,x0[0],h)
		comp_time.append(time() - start)
		comp_err.append(np.abs(correctomundo - approx)) # now approx is actually a scalar

	# plot times
	plt.subplot(211)
	plt.plot(values, for_time)
	plt.plot(values, cent_time)
	plt.plot(values, comp_time)
	plt.plot(values, auto_time)
	plt.xscale('log', base = 2)
	plt.xlabel("h value")
	plt.ylabel('computation time')
	plt.legend(['forward', 'centered', 'complex', 'autograd'])
	plt.title("Problem 18 Times")

	# plot errors
	plt.subplot(212)
	plt.plot(values, for_err)
	plt.plot(values, cent_err)
	plt.plot(values, comp_err)
	plt.plot(values, auto_err)
	plt.xscale('log', base = 2)
	plt.xlabel("h value")
	plt.ylabel('error')
	plt.legend(['forward', 'centered', 'complex', 'autograd'])
	plt.title("Problem 18 Errors")
	plt.tight_layout()
	plt.show()

if __name__ == "__main__":
	f = lambda x: np.array([((np.sin(x))**3 + np.cos(x))/np.exp(x)])

	# print(complex_step(1,f,np.array([1.5]),2**-2))
	prob16()
	prob17()
	prob18()