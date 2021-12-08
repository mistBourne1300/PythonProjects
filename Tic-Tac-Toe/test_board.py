from TTTboard import  Board as bd
from TTTmachine import TicEsMachina
import numpy as np

if __name__ == "__main__":
	game = bd()
	game.board = np.array([	[ 1,  0, -1],
 							[ 1,  0, -1],
 							[ 0,  0,  0]])


	tim = TicEsMachina("TTTMachine")
	choices = tim.choose_move(game.board.ravel())
	print(choices)
