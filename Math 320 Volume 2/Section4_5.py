# Exercises 4.26, 4.27


# Problem 4.26 / 4.27
def knapsack(W, Items):
	"""This implements a dynamic programming algorithm for the {0,1}-knapsack
    problem (i.e. only one of each item is allowed).

    Inputs:
        W (int):
            A maximum weight that the knapsack can hold
        Items (list (tuple)):
            A list of 2-tuples where the ith tuple contains the pair
            (weight, value) corresponding to the weight of that item and
            its value.

    Outputs:
        max_val (float):
            Maximum value that can be carried in the knapsack.
        packed_items (list):
            The number of each item that should be used to achieve the maximum
            value. The ith entry should be an integer showing how many of the
            ith item should be packed.

    Examples:
    >>> knapsack( 100, [(20, 0.5), (100, 1.0)] )
    (1.0, [0, 1])

    >>> knapsack( 115, [(15, 0.5), (25, 1.0)] )
    (1.5, [1, 1])

    >>> knapsack( 10, [(6, 30), (3, 14), (4, 16), (2, 9)] ) # Example 4.5.4
    (46, [1, 0, 1, 0])

    """
	def contains_duplicate(list1, list2):
		#print(f'comparing:\n{list1}\n{list2}')
		if(len(list1) != len(list2)):
			raise ValueError("list1 not the same length as list2")
		for i in range(len(list1)):
			if(list1[i] + list2[i] > 1):
				#print("returning false")
				return True
		#print('returning true')
		return False

	def add_two_lists(list1, list2):
		if(len(list1) != len(list2)):
			raise ValueError("list1 not the same length as list2")
		retrun = [list1[i] + list2[i] for i in range(len(list1))]
		#print(f'retrun: {retrun}')
		return retrun

	items_for_weight = {}
	# initialize the items_for_weight with 0's
	for i in range(W+1):
		items_for_weight[i] = 0, [0 for j in range(len(Items))]


	#initialize the weight data with each item
	for i in range(len(Items)):
		items_for_weight[Items[i][0]] = Items[i][1], [int(j == i) for j in range(len(Items))] 
	#print(items_for_weight)


	#loop through weights and find the optimal solution for each
	for i in range(W+1):
		poss_solutions = []
		if(i in items_for_weight):
			poss_solutions.append(items_for_weight[i])
		# loop throught the solved states and add the possible solutions
		for j in range(i):

			#print(f'j:{j}, i-j:{i-j}')
			#print(items_for_weight[j], items_for_weight[i-j])
			if not contains_duplicate(items_for_weight[j][1], items_for_weight[i-j][1]):
				poss_solutions.append((items_for_weight[j][0] + items_for_weight[i-j][0], add_two_lists(items_for_weight[j][1], items_for_weight[i-j][1])))
		
		#print(f'poss_solutions for {i}: {poss_solutions}')
		#find the optimal solution from the possible ones
		optimal_solution = poss_solutions[0]
		for j in range(len(poss_solutions)):
			if(poss_solutions[j][0] > optimal_solution[0]):
				optimal_solution = poss_solutions[j]
		
		items_for_weight[i] = optimal_solution
		# for item in items_for_weight:
		# 	#print(item, items_for_weight[item])
		
	#print(f'solution: {items_for_weight[W]}')
	return items_for_weight[W]

	raise NotImplementedError()


if __name__ == "__main__":
    # You can run test code as long as it's in this block.
	items = [(6,30), (3,14), (4,16), (2,9)]
	max_weight = 10
	knapsack(max_weight, items)

	pass