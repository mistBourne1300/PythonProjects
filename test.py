# b
# c
# d
# e
# f
# g
# h
# i
# j
# k
# l
# m
# n
# o
# p
# q
# r
# s
# t
# u
# v
# w
# x
# y
# z






import numpy as np
from imageio import imread
from imageio import imwrite
from matplotlib import pyplot as plt
import os
from scipy.stats import linregress
from datetime import date

def sigmoid(x):
	return 1/(1+np.exp(-x))

# image = imread("/Users/chase/Downloads/IMG_0124.JPG")
# scaled = image / 255
# plt.imshow(scaled)
# plt.show()
# greyscale = scaled.mean(axis=2)
# plt.imshow(greyscale, cmap = "magma")
# plt.show()

# states = np.array(["hot", 'mild', 'cold', 'freezing'])
# choice = np.array([0,0,1,0])
# mask = choice == 1
# print(states[mask]) # prints a list containing the label chosen
# print(states[np.argmax(choice)]) # they want just the label, not the array containing the label

# A = np.array([[1,2],[1,2]])
# print(np.sum(A, axis = 0))


# p = np.log(1/2)
# sum = 0
# for i in range(2**32-77166,2**32-1):
# 	sum += np.log(1)

# sum -= 77164*np.log(2**32-1)
# print(sum)
os.chdir("/Users/chase/Desktop/Python")

# A = np.load("anscombe.npy")

# print(A[:,0], A[:,1])

# for i in range(2,len(A[:,0])):
# 	exxes = A[:i,0]
# 	whys = A[:i,1]
# 	regress = linregress(exxes, whys)
# 	domain = np.linspace(0, 15)
# 	rng = regress[0] * domain + regress[1]
# 	plt.plot(domain, rng)
# 	plt.scatter(exxes, whys)
# 	plt.title(f"anscombe with {i} data points\n r = {regress[2]}")
# 	plt.xlim(0,15)
# 	plt.ylim(0,15)
# 	plt.show()

print(np.sqrt(800))


for i in range(9):
	print(f'{i//3,i%3}')

domain = np.linspace(-10,10)
rng = sigmoid(domain)
plt.plot(domain,rng)
plt.show()

exxes = [x for x in range(10)]
whys = [y for y in range(9)]
whys.append(None)
plt.plot(exxes, whys)
plt.show()
today = date.today()
print(today)