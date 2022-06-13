import numpy as np

class Board:
	''' 
		a tic tac toe board class
		Data members:
			board (ndarray): the tic tac toe board
	'''

	def __init__(self):
		self.board = np.array([[0 for j in range(3)] for i in range(3)])
	
	def poss_moves(self):
		for row in range(3):
			for col in range(3):
				if self.board[row,col] == 0:
					yield row, col
	
	def check_full(self):
		'''	
			check if the board is in a full state
			Returns: 
				True if the board is full
				False otherwise
		'''
		if np.all(self.board != 0):
			return True
		
	def empty_squares(self):
		'''
			return the number of empty squares on the board
		'''
		empty = 0
		for i in np.ravel(self.board):
			if i == 0:
				empty += 1
		return empty
	
	def check_win(self):
		'''
			check whether one player or the other has won
			Returns:
				1 if X has won
				-1 if O has won
				0 otherwise
		'''
		# check all rows and columns for an X win
		if np.all(self.board[:,0] == 1):
			# print(1)
			return 1
		if np.all(self.board[:,1] == 1):
			# print(2)
			return 1
		if np.all(self.board[:,2] == 1):
			# print(3)
			return 1
		if np.all(self.board[0,:] == 1):
			# print(4)
			return 1
		if np.all(self.board[1,:] == 1):
			# print(5)
			return 1
		if np.all(self.board[2,:] == 1):
			# print(6)
			return 1
		
		# check all rows and columns for an O win
		if np.all(self.board[:,0] == -1):
			# print(7)
			return -1
		if np.all(self.board[:,1] == -1):
			# print(8)
			return -1
		if np.all(self.board[:,2] == -1):
			# print(9)
			return -1
		if np.all(self.board[0,:] == -1):
			# print(10)
			return -1
		if np.all(self.board[1,:] == -1):
			# print(11)
			return -1
		if np.all(self.board[2,:] == -1):
			# print(12)
			return -1

		# grab the two diagonals
		diag1 = np.array([self.board[i,i] for i in range(3)])
		diag2 = np.array([self.board[2-i,i] for i in range(3)])
		
		# check the two diagonals for an X win
		if np.all(diag1 == 1):
			# print(13, diag1)
			return 1
		if np.all(diag2 == 1):
			# print(14, diag2)
			return 1
		
		# check the diagonals for an O win
		if np.all(diag1 == -1):
			# print(15, diag1)
			return -1
		if np.all(diag2 == -1):
			# print(16, diag2)
			return -1
		
		return 0
	
	def make_move(self, player, row, col):
		'''
			make a move on the tic tac toe board
			
			Parameters:
				player (int):	must be 1 or -1. 1 stands for X, -1 for O
				row (int):		must be 0,1, or 2. the row of the move to make
				col (int):		"				  " the col of the move to make
			
			Returns:
				False if the board already has a nonzero entry at [row, col]
				True if a move was successfully completed
		'''

		if player != 1 and player != -1:
			raise ValueError(f"player must be a 1 or -1. you passed: {player}")
		
		if row>2 or row<0 or col>2 or col<0:
			raise ValueError(f'row and col must be 0-2 inclusive. you passed: {row}, {col}')
		
		# dont raise an error if the row and column has already been played on,
		# as an untrained AI will often choose row,col pairs that are already played 
		if self.board[row,col] != 0:
			return False
		
		self.board[row,col] = player
		return True

	def __str__(self):
		string = ""
		counter = 0
		for i in np.ravel(self.board):
			if i == 0:
				if(counter<6):
					string += "_"
				else:
					string += " "
			elif i == -1: string += "O"
			elif i == 1: string += "X"
			counter += 1
		
		spacing = "||\n||\n||\n"
		lace = ""
		for i in range(9):
			lace += string[i] + spacing[i]
		return lace