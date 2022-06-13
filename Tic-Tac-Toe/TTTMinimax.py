from TTTboard import Board as bd
from copy import deepcopy
import numpy as np

class Minimax:

	def __init__(self, player):
		"""
			Initialize a Minimax TicTacToe player.
			Parameters:
				player (-1,1): the player type the computer is. 1 is X, -1 is O.
		
			player must be either 1 or -1
		"""

		if player != 1 and player != -1:
			raise ValueError("player must be either 1 or -1")
		self.player = player
		self.row = 0
		self.col = 0
		self.count = 0
		
		self.starting_moves = {"UP LEFT" : (0,0), "UP RIGHT" : (0,2), "LOW RIGHT" : (2,2), "LOW LEFT" : (2,0)}
	
	def utility(self, board:bd):
		return board.check_win() * self.player * (board.empty_squares() + 1)
	
	def move_recur(self, board:bd, player, level = 0):
		# temp = input("press enter to continue recursion")
		print(f"level: {level}, count: {self.count}")
		self.count += 1
		
		if board.check_win() or board.check_full():
			return self.utility(board)

		boards = []
		moves = []
		for row, col in board.poss_moves():
			new_board = deepcopy(board)
			if new_board.make_move(player, row, col):
				boards.append(new_board)
				moves.append((row,col))
		
		utilities = []
		for b in boards:
			if b.check_win() or b.check_full():
				utilities.append(self.utility(b))
			else:
				utilities.append(self.move_recur(b, player * -1, level + 1)) # needs to be a max call somewhere here

		if self.player == player:
			util_argmax = np.argmax(utilities)
			util = utilities[util_argmax]
			self.row, self.col = moves[util_argmax]
		else:
			util = np.min(utilities)
		return util


					

					
						

	def move(self, board:bd):
		print("Calculating next move...")
		# temp = input(f"{board.empty_squares()} press enter to continue")
		if board.empty_squares() == 9:
			row, col = self.starting_moves[np.random.choice(list(self.starting_moves.keys()))]
			board.make_move(self.player, row, col)
			return
		self.count = 0
		util = self.move_recur(board, self.player)
		print(f"making move at {self.row}, {self.col} with utility {util}")
		board.make_move(self.player, self.row, self.col)
	
