import numpy as np

def find_maximal(unimodal_list):
	'''finds the maximal element of a unimodal list

		Parameters: unimodal_list (a list composed of an increasing sequence 
									followed by a decreasing sequence)

	'''
	if(len(unimodal_list) == 1):
		return unimodal_list[0]
	mid_index = int(len(unimodal_list)/2)
	if(unimodal_list[mid_index - 1] < unimodal_list[mid_index]):
		return find_maximal(unimodal_list[mid_index:])
	else:
		return find_maximal(unimodal_list[:mid_index])

if __name__ == "__main__":	
	my_list = [0,1,2,3,4,5,4,3,2,1,0,-1,-2]
	print(find_maximal(my_list))
