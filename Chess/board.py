from colorama import Fore, Back, Style
from piece import Piece
import numpy as np

class Board:
	def __init__(self):
		self.board = np.array([[None for i in range(8)] for i in range(8)])
		self.board[0,0] = Piece('r')
		self.board[0,0].make_black()

		self.board[0,1] = Piece('n')
		self.board[0,1].make_black()

		self.board[0,2] = Piece('b')
		self.board[0,2].make_black()

		self.board[0,3] = Piece('q')
		self.board[0,3].make_black()

		self.board[0,4] = Piece('k')
		self.board[0,4].make_black()
	
	def print_me(self):
		i = 0
		for row in self.board:
			for piece in row:
				print(Style.RESET_ALL, end = "")
				if i%2 == 0:
					print(Back.LIGHTWHITE_EX, end = "")
				else:
					print(Back.LIGHTBLACK_EX, end = "")
				i += 1
				if piece != None:
					if piece.value < 0:
						print(Fore.BLUE + str(piece), end = "")
					else:
						print(Fore.RED + str(piece), end = "")
				else:
					print(Fore.BLACK + ".", end = "")
			print(Style.RESET_ALL)
			i += 1

board = Board()
board.print_me()