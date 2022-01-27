
from cmath import cos
from scipy import linalg as la
import numpy as np
from scipy.stats import norm
import matplotlib.pyplot as plt

"""the cosine quadrature is much more accurate, probably because the |x| function
is not analytic at x = 0. So, the quadtrature methods comverge much more slowly."""

class GaussianQuadrature:
    """Class for integrating functions on arbitrary intervals using Gaussian
    quadrature with the Legendre polynomials or the Chebyshev polynomials.
    """
    # Problems 1 and 3
    def __init__(self, n, polytype="legendre"):
        """Calculate and store the n points and weights corresponding to the
        specified class of orthogonal polynomial (Problem 3). Also store the
        inverse weight function w(x)^{-1} = 1 / w(x).

        Parameters:
            n (int): Number of points and weights to use in the quadrature.
            polytype (string): The class of orthogonal polynomials to use in
                the quadrature. Must be either 'legendre' or 'chebyshev'.

        Raises:
            ValueError: if polytype is not 'legendre' or 'chebyshev'.
        """
        # value error if the polytype is wrong
        if polytype not in ['legendre', 'chebyshev']:
            raise ValueError("polytype must be either legendre or chebyshev")

        # assign class veriables 
        self.polytype = polytype
        if self.polytype == 'legendre':
            self.winv = lambda x: 1
        else:
            self.winv = lambda x: np.sqrt(1-x**2)
        
        # use the class method to calculate the points and weights
        self.points, self.weights = self.points_weights(n)



    # Problem 2
    def points_weights(self, n):
        """Calculate the n points and weights for Gaussian quadrature.

        Parameters:
            n (int): The number of desired points and weights.

        Returns:
            points ((n,) ndarray): The sampling points for the quadrature.
            weights ((n,) ndarray): The weights corresponding to the points.
        """
        # calculate the jacobi matrix
        if self.polytype == 'legendre':
            jacobi = np.diag([np.sqrt(k**2/(4*k**2 - 1)) for k in range(1,n)], 1) + np.diag([np.sqrt(k**2/(4*k**2 - 1)) for k in range(1,n)], -1)
        
        else: 
            bk = [1/2]
            for i in range(2,n):
                bk.append(1/4)
            bk = np.sqrt(bk)
            jacobi = np.diag(bk, 1) + np.diag(bk, -1)
        
        # get the eigenvalues and eigenvetors of jacobi
        eigvals, eigvects = la.eig(jacobi)
        
        # get the real part
        eigvals = eigvals.real

        # calculate the weights using the vi's
        wi = eigvects[0,:].real**2
        if self.polytype == 'legendre':
            wi *= 2
        else: wi *= np.pi

        return eigvals, wi

    # Problem 3
    def basic(self, f):
        """Approximate the integral of a f on the interval [-1,1]."""
        # calculate g and return the sum of the haadamard product
        g = lambda x: f(x)*self.winv(x)
        return np.sum(g(self.points) * self.weights)

    # Problem 4
    def integrate(self, f, a, b):
        """Approximate the integral of a function on the interval [a,b].

        Parameters:
            f (function): Callable function to integrate.
            a (float): Lower bound of integration.
            b (float): Upper bound of integration.

        Returns:
            (float): Approximate value of the integral.
        """
        # change of variables to shift the bounds of integration
        h = lambda x: f((b-a)*x/2 + (a+b)/2)
        # return the shifted basic integral times the jacobian constant
        return self.basic(h)*(b-a)/2


    # Problem 6.
    def integrate2d(self, f, a1, b1, a2, b2):
        """Approximate the integral of the two-dimensional function f on
        the interval [a1,b1]x[a2,b2].

        Parameters:
            f (function): A function to integrate that takes two parameters.
            a1 (float): Lower bound of integration in the x-dimension.
            b1 (float): Upper bound of integration in the x-dimension.
            a2 (float): Lower bound of integration in the y-dimension.
            b2 (float): Upper bound of integration in the y-dimension.

        Returns:
            (float): Approximate value of the integral.
        """
        # calculate the h and g functions
        h = lambda x, y: f((b1-a1)/2*x + (a1+b1)/2, (b2-a2)/2*y + (a2+b2)/2)
        g2d = lambda x,y: h(x,y)*self.winv(x)*self.winv(y)
        # create a matrix of all the values to the multiply by the weights
        G_mat = []
        for x in self.points:
            row = [g2d(x,y) for y in self.points]
            G_mat.append(row)
        G_mat = np.array(G_mat)
        # return the dot product and matrix product
        return np.dot(self.weights, G_mat@self.weights) * (b1-a1)*(b2-a2)/4



def quadricepts(f, n):
	return GaussianQuadrature(n+1).basic(f)

if __name__ == "__main__":
	f = lambda x: np.where(x<0, 1+x, x)

	ABS_EXACT = 1
	COS_EXACT = 2*np.sin(1)

	values = np.arange(2,10)*10
	abs_err = []
	cos_err = []
	for n in values:
		print(n)
		abs_err.append(np.abs(quadricepts(f,n) - ABS_EXACT))
		cos_err.append(np.abs(quadricepts(np.cos,n) - COS_EXACT))
	
	plt.plot(values, abs_err, 'k')
	plt.plot(values, cos_err, 'r')
	plt.yscale('log')
	plt.xlabel('degree of polynomial')
	plt.ylabel('error')
	plt.show()
