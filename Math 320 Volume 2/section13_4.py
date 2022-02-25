import numpy as np

class SimplexSolver(object):
    """Class for solving the standard linear optimization problem

                        minimize        c^Tx
                        subject to      Ax <= b
                                         x >= 0
    via the Simplex algorithm.
    """
    # Problem 1
    def __init__(self, c, A, b):
        """Check for feasibility and initialize the dictionary.

        Parameters:
            c ((n,) ndarray): The coefficients of the objective function.
            A ((m,n) ndarray): The constraint coefficients matrix.
            b ((m,) ndarray): The constraint vector.

        Raises:
            ValueError: if the given system is infeasible at the origin.
        """
        self.c = c
        self.A = A
        self.b = b
        self.m,self.n = A.shape
        if np.min(b) < 0:
            # need to solve auxiliary problem
            self.D = self._generate_aux_dict()
            print(self.D)
            raise ValueError("problem is not feasible at the origin")
        else:
            self.D = self._generatedictionary()
            print(self.D)
        

    # Problem 2
    def _generatedictionary(self):
        """Generate the initial dictionary.

        Parameters:
            c ((n,) ndarray): The coefficients of the objective function.
            A ((m,n) ndarray): The constraint coefficients matrix.
            b ((m,) ndarray): The constraint vector.
        """
        _A_ = np.hstack((self.A,np.identity(self.m)))
        _c_ = np.concatenate((self.c, np.zeros(self.m)))
        Dtop = np.hstack(([0], _c_.T))
        Dbottom = np.hstack((self.b.reshape(-1,1), -_A_))
        return np.vstack((Dtop, Dbottom))

    def _generate_aux_dict(self):
        print("A:",self.A.shape)
        print("b:",self.b.shape)
        print("c:",self.c.shape)
        _A_ = np.hstack((self.A, np.identity(self.m), np.ones(self.m).reshape(-1,1)))
        print("_A_:",_A_.shape)
        _c_ = np.concatenate((self.c, np.zeros(self.m+1)))
        print("_c_:",_c_.shape)
        Dtop = np.hstack(([0], _c_.T))
        print("Dtop:", Dtop.shape)
        Dbottom = np.hstack((self.b.reshape(-1,1), -_A_))
        print("Dbottom:",Dbottom.shape)
        return np.vstack((Dtop, Dbottom))

    # Problem 3a
    def _pivot_col(self):
        """Return the column index of the next pivot column.
        """
        for i in range(1,len(self.D[0])):
            if self.D[0][i] < 0:
                return i
        return -1

    # Problem 3b
    def _pivot_row(self, index):
        """Determine the row index of the next pivot row using the ratio test
        (Bland's Rule).
        """
        if np.min(self.D[1:,index]) >= 0.:
            raise RuntimeError("problem is unbounded, no solution exists")
        
        mask = self.D[1:,index] >= 0. 
        ratios = -self.D[1:,0] / self.D[1:,index]
        ratios[mask] = np.inf
        print("ratios:", ratios)
        return np.argmin(ratios) +1

    # Problem 4
    def pivot(self):
        """Select the column and row to pivot on. Reduce the column to a
        negative elementary vector.
        """
        j = self._pivot_col()
        i = self._pivot_row(j)
        self.D[i,:] /= -self.D[i,j]
        print(i,j)
        for k in range(len(self.D)):
            if k == i: continue
            self.D[k,:] += self.D[k,j]*self.D[i,:]


    # Problem 5
    def solve(self, v = False):
        """Solve the linear optimization problem.

        Returns:
            (float) The minimum value of the objective function.
            (dict): The basic variables and their values.
            (dict): The nonbasic variables and their values.
        """
        while np.min(self.D[0,1:]) < 0:
            if v: print(self.D, end = "\n\n")
            self.pivot()
            input("press enter:")
        if v: print(self.D)
        # min_val = self.D[0,0]
        independent = dict()
        dependent = dict()
        for j in range(1,len(self.D[0])):
            if self.D[0,j] == 0:
                # dependent
                index = self.D[:,j].tolist().index(-1)
                # print(index)
                dependent[j] = self.D[index,0]
            elif self.D[0,j] > 0:
                # independent
                independent[j] = 0
            else:
                raise RuntimeError("problem solving failed")
        return self.D[0,0], dependent, independent


def prob22():
    c = np.array([-5.,4.])
    A = np.array([	[2.,-3.],
					[1.,-6.],
					[1.,1.]])
    b = np.array([4.,1.,6.])
    min_val, dependent, independent = SimplexSolver(c,A,b).solve(v=True)
    print(min_val, dependent, independent)
    soln = np.zeros(len(c))
    max_index = len(c) - 1
    print('dependent:')
    for i in dependent.keys():
        print(i)
        if i-1 > max_index: continue
        soln[i-1] = dependent[i]
        print(soln)
        print(dependent[i])
    print("independent:")
    for i in independent.keys():
        print(i)
        if i-1 > max_index: continue
        soln[i-1] = 0
    return soln

def prob23():
    c = np.array([-3.,-1.])
    A = np.array([  [1.,3.],
                    [2.,3.],
                    [1.,-1.]])
    b = np.array([15.,18.,4.])
    min_val, dependent, independent = SimplexSolver(c,A,b).solve(v=True)
    soln = np.zeros(len(c))
    max_index = len(c) - 1
    print('dependent:')
    for i in dependent.keys():
        print(i)
        if i-1 > max_index: continue
        soln[i-1] = dependent[i]
        print(dependent[i])
    print("independent:")
    for i in independent.keys():
        print(i)
        if i-1 > max_index: continue
        soln[i-1] = 0.
    return soln

def prob24():
    c = np.array([-4.,-6.])
    A = np.array([  [-1.,1.],
                    [1.,1.],
                    [2.,5.]])
    b = np.array([11.,27.,90.])
    min_val, dependent, independent = SimplexSolver(c,A,b).solve(v=True)
    soln = np.zeros(len(c))
    max_index = len(c) - 1
    print('\ndependent:')
    for i in dependent.keys():
        print(i)
        if i-1 > max_index: continue
        soln[i-1] = dependent[i]
        print(dependent[i])
    print("independent:")
    for i in independent.keys():
        print(i)
        if i-1 > max_index: continue
        soln[i-1] = 0
    return soln

def prob25():
    c = np.array([-4,-3])
    A = np.array([  [15., 10.],
                    [2., 2.],
                    [0.,1.]])
    b = np.array([1800.,300.,200.])
    min_val, dependent, independent = SimplexSolver(c,A,b).solve(v=True)
    soln = np.zeros(len(c))
    max_index = len(c) - 1
    print('\ndependent:')
    for i in dependent.keys():
        print(i)
        if i-1 > max_index: continue
        soln[i-1] = dependent[i]
        print(dependent[i])
    print("independent:")
    for i in independent.keys():
        print(i)
        if i-1 > max_index: continue
        soln[i-1] = 0
    return soln


def test00():
    c = np.array([-3.,-1.])
    A = np.array([  [1.,3.],
                    [2.,3.],
                    [1.,-1.]])
    b = np.array([15.,18.,-4.])
    SimplexSolver(c,A,b)
    

if __name__ == "__main__":
	print(test00())
