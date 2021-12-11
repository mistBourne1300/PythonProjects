from TTTboard import  Board as bd
from TTTmachine import TicEsMachina
import numpy as np

if __name__ == "__main__":
	# game = bd()
	# game.board = np.array([	[ 1,  0, -1],
 	# 						[ 1,  0, -1],
 	# 						[ 0,  0,  0]])


	# tim = TicEsMachina(1,"TTTMachine")
	# choices = tim.choose_move(game.board.ravel())
	# print(choices)
	# print(np.flip(np.argsort(choices)))

	# arr = np.array([TicEsMachina() for i in range(5)])
	# print(f'arr: {arr}; type: {type(arr)}')
	# arr = [a for a in arr]
	# print(f'arr: {arr}; type: {type(arr)}')
	# arr.append([TicEsMachina() for i in range(10)])
	# print(f'arr: {arr}; type: {type(arr)}')
	# arr = np.array(arr)
	# print(f'arr: {arr}; type: {type(arr)}')

	oh = np.array([1,1,0,1,0,1])
	save = oh<0
	print(oh, oh[save], sep = "\n")
	print(np.arange(10))
