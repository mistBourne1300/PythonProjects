import numpy as np
from imageio import imread
from imageio import imwrite
from matplotlib import pyplot as plt

# image = imread("/Users/chase/Downloads/IMG_0124.JPG")
# scaled = image / 255
# plt.imshow(scaled)
# plt.show()
# greyscale = scaled.mean(axis=2)
# plt.imshow(greyscale, cmap = "magma")
# plt.show()

states = np.array(["hot", 'mild', 'cold', 'freezing'])
choice = np.array([0,0,1,0])
mask = choice == 1
print(states[mask]) # prints a list containing the label chosen
print(states[np.argmax(choice)]) # they want just the label, not the array containing the label

A = np.array([[1,2],[1,2]])
print(np.sum(A, axis = 0))