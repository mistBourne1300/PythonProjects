import numpy as np
import networkx as nx
import matplotlib.pyplot as plt
from numpy.random.mtrand import rand


'''	will prompt the user if they want to create a random matrix, load a matrix, or input one themselves. 
	it will then print the resulting graph, and ask for two nodes to find the path through.
	then, it will print the graph again, with the path highlighted (coming soon)
'''

if __name__ == "__main__":
	string = "Would you like to:\n"
	string += "1: Create a random adjacency matrix\n"
	string += "2: load adjacency matrix from csv file\n"
	string += "3: input adjacency matrix\n"
	string += "Enter your choice: "
	choice = input(string)
	if (choice == '1'):
		#create a random adjacency matrix
		size = int(input("how large should your random graph be? "))
		rand_matrix = np.random.randint(0,2,(size,size))
		print(rand_matrix)
		rand_graph = nx.from_numpy_array(rand_matrix)
		nx.draw(rand_graph, with_labels = True)
		plt.savefig("random_graph.png")

		vertex1 = int(input("which vertex are you coming from? "))
		vertex2 = int(input("which vertex are you going to? "))

		path_matrix = rand_matrix
		path_length = 1
		while path_matrix[vertex1, vertex2] == 0:
			path_matrix = path_matrix @ rand_matrix
			path_length += 1
		
		print(path_matrix)
		print(f'the shortest path from {vertex1} to {vertex2} is {path_length} units')
	elif(choice == '2'):
		raise NotImplementedError("Option 2 not implemented")
	elif(choice == '3'):
		raise NotImplementedError("Option 3 not implemented")
	else:
		raise ValueError(f'User input: {choice} not a valid option')