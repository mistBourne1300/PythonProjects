# Exercise 9
# NOTE: for Exercise 10, you will use the functions that you code here.
# However, the results of Exercise 10 should be included in your written
# submission to gradescope.

import numpy as np
import matplotlib.pyplot as plt

# 9.9 part 1
def bary_weights(points):
    """Computes the barycentric weights for a given set of distinct points
    {x_0,...,x_n} (the elements of parameter x).
    """
    weights = []
    for j in range(len(points)):
        wj = 1
        for k in range(len(points)):
            if j == k: continue
            wj *= points[j] - points[k]
        weights.append(1/wj)
    return weights
    


# 9.9 part 2
def eval_poly(x,y,z):
    """Evaluates the unique interpolating polynomial through {(x_0, y_0), ... ,
    (x_n, y_n)}. Should use bary_weights.
    Parameters:
        x (ndarray): the set of x_0, x_1, ... , x_n.
        y (ndarray): the set of y_0, y_1, ... , y_n.
        z (float): the point at which to evaluate the polynomial.
    Returns:
        The value of the polynomial which interpolates the points in x, y
        evaluated at z.
    """
    weights = bary_weights(x)
    numerator = 0
    denominatorinator = 0
    for j in range(len(x)):
        numerator += y[j] * weights[j]/(z-x[j])
        denominatorinator += weights[j]/(z-x[j])
    
    return numerator / denominatorinator

def wilk(domain):
    product = 1
    for i in range(1,21):
        product *= domain - i 
    
    return product

if __name__ == "__main__":
    # domain = np.linspace(-1,1)
    # for n in range(2,21):
    #     plt.subplot(4,5,n)
    #     plt.plot(domain, np.abs(domain))
    #     exxes = np.linspace(-1,1,n)
    #     whys = np.abs(exxes)
    #     plt.plot(domain, eval_poly(exxes, whys, domain))
    # plt.show()

    # exxes = [-1, -1/3, 1/3, 1]
    # whys = [0, np.sin(-np.pi/3), np.sin(np.pi/3), 0]
    # print(bary_weights(exxes))
    # domain = np.linspace(-1.1,1.1)
    # plt.plot(domain, eval_poly(exxes, whys, domain), 'k')
    # plt.plot(domain, np.sin(np.pi * domain), 'b')
    # exxes = []
    # whys = []
    # for j in range(4):
    #     exxes.append(np.cos(j*np.pi/3))
    #     whys.append(np.sin(np.pi * np.cos(j*np.pi/3)))
    
    # plt.plot(domain, eval_poly(exxes, whys, domain), 'r')
    # plt.legend(['poly', 'np.sin(pi x)', 'chebyshev zeros'])
    # plt.show()

    exxes = []
    whys = []
    n= 20
    for j in range(n):
        x = (np.cos((np.pi/n) * (j+1/2)) + (21/19))/(2/(19))
        exxes.append(x)
        whys.append(0)
    
    domain = np.linspace(1, 20, 10000)
    plt.plot(domain, wilk(domain), 'r')
    plt.plot(domain, eval_poly(exxes, whys, domain))
    print(f'wilk max: {np.max(wilk(domain))}')
    print(f'chebyshev max: {np.max(eval_poly(exxes, whys, domain))}')
    plt.show()
    