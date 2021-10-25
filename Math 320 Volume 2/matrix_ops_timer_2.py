import numpy as np
import time

def calcTimes(u,v,x):
    ID = np.identity(len(x))
    startTime = time.time()
    np.matmul((ID + np.matmul(u,v.T)), x)
    endTime = time.time()
    firstTime = endTime - startTime

    startTime = time.time()
    x + (u * np.matmul(v.T,x))
    endTime = time.time()
    secondTime = endTime - startTime

    return firstTime, secondTime

def getTimes(n):
    first_method = [0 for i in range(n)]
    second_method = [0 for i in range(n)]
    for i in range(1, n+1):
        A = np.random.randint(0, 1000, size = (2**i, 2**i))
        B = np.random.randint(0, 1000, size = (2**i, 2**i))
        x = np.random.randint(0, 1000, size = 2**i)
        first_method[i-1], second_method[i-1] = calcTimes(A, B, x)
        print("first: ", first_method[i-1], "second: ", second_method[i-1])
    return first_method, second_method

def findRatios(first, second):
    ratios = []
    for i in range(len(first)):
        ratios.append(first[i] / second[i])
    return ratios


if __name__ == "__main__":
    time_calcs = getTimes(11)
    print(time_calcs[0])
    print("\n\n\n")
    print(time_calcs[1])
    print("\n\n\n")
    print(findRatios(time_calcs[0], time_calcs[1]))