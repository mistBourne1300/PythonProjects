from colorama import Fore, Back, Style
from piece import Piece
import numpy as np
import time

class Board:
	def __init__(self):
		self.board = np.array([[None for i in range(8)] for i in range(8)])
		self.board[0,0] = Piece('r')
		self.board[0,0].make_black()
		self.board[7,0] = Piece('r')

		self.board[0,1] = Piece('n')
		self.board[0,1].make_black()
		self.board[7,1] = Piece('n')

		self.board[0,2] = Piece('b')
		self.board[0,2].make_black()
		self.board[7,2] = Piece('b')

		self.board[0,3] = Piece('q')
		self.board[0,3].make_black()
		self.board[7,3] = Piece('q')

		self.board[0,4] = Piece('k')
		self.board[0,4].make_black()
		self.board[7,4] = Piece('k')

		self.board[0,5] = Piece('b')
		self.board[0,5].make_black()
		self.board[7,5] = Piece('b')

		self.board[0,6] = Piece('n')
		self.board[0,6].make_black()
		self.board[7,6] = Piece('n')
		
		self.board[0,7] = Piece('r')
		self.board[0,7].make_black()
		self.board[7,7] = Piece('r')

		for i in range(len(self.board[1])):
			self.board[1,i] = Piece()
			self.board[1,i].make_black()
			self.board[6,i] = Piece()
	
	def __str__(self):
		'''
			overloaded __str__ method returns empty string, sorry
			but it does print the board to terminal!
		'''
		self.print_me()
		return ""

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
						print(Fore.BLUE + " " + str(piece) + " ", end = "")
					else:
						print(Fore.RED + " " + str(piece) + " ", end = "")
				else:
					print(Fore.BLACK + "   ", end = "")
			print(Style.RESET_ALL)
			i += 1

	def check_piece(self, piece:Piece, type:str):
		if not piece:
			print("piece is null")
			return False
		if piece.type != type:
			print("Piece is not expected type")
			return False
		return True
	
	def friendly_fire(self, attacker:Piece, defender:Piece):
		'''
			returns true if attacking would result in friendly fire
		'''
		if attacker.value < 0:
			return defender.value < 0
		else:
			return defender.value > 0

	def move_pawn(self, row:int, col:int):
		if row == 7 or row == 0:
			print(f"pawns should not be found in row {row}")
			return False
		pawn = self.board[row, col]
		if not self.check_piece(pawn, 'p'):
			return False
		if pawn.value < 0: # we have a black pawn, the row index should increase by one
			if self.board[row+1, col]:
				print("cannot attack forward")
				return False
			self.board[row,col] = None
			self.board[row+1, col] = pawn
		else:
			if self.board[row-1, col]:
				print("cannot attack forward")
				return False
			self.board[row,col] = None
			self.board[row-1, col] = pawn
		return True
		
	def pawn_lunge(self, row:int, col:int):
		if row != 6 and row != 1:
			print("pawns can only lunge in rows 6 or 1")
			return False
		
		pawn = self.board[row, col]
		if not self.check_piece(pawn, 'p'):
			return False
		
		if pawn.value < 0 and row == 1:
			board.move_pawn(row, col)
			board.move_pawn(row+1, col)
			return True
		if pawn.value > 0 and row == 6:
			board.move_pawn(row, col)
			board.move_pawn(row-1, col)
			return True
		print("The color of the pawn and the row does not match up")
		return False

	def pawn_attack(self, row:int, col:int, dir:str):
		if dir != 'l' and dir != 'r':
			print(f"direction must be either 'l' or 'r' not {dir}")
		attacker = self.board[row, col]
		if not self.check_piece(attacker, 'p'):
			return False
		
		

board = Board()
# print(board)
board.move_pawn(6,4)
board.pawn_lunge(1,3)
board.pawn_lunge(6,3)
board.pawn_attack
print(board)