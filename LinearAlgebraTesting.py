import numpy as np
A = np.array([[1,2,2],[2,1,2],[2,2,1]])
Q = np.array([[-1/np.sqrt(2), -1/np.sqrt(6), 1/np.sqrt(3)], [1/np.sqrt(2), -1/np.sqrt(6), 1/np.sqrt(3)], [0, 2/np.sqrt(6), 1/np.sqrt(3)]])

D = np.array([[-1, 0, 0], [0,-1,0], [0,0,5]])

print(np.transpose(Q) @ A @ Q)