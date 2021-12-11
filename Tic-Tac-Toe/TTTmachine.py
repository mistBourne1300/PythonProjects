import numpy as np
from TTTboard import Board

class TicEsMachina:
	'''
		an AI class for a TicTacToe board
		Data Members:
			layer1 (3x9 ndarray): the first layer weights
			layer2 (3x3 ndarray): the second layer weights
			layer3 (9x3 ndarray): the third layer weights
	'''

	def __init__(self, player, foldername = ""):
		self.player = player
		if(foldername):
			self.layer1 = np.load(f'{foldername}/layer1.npy')
			self.layer2 = np.load(f'{foldername}/layer2.npy')
			self.layer3 = np.load(f'{foldername}/layer3.npy')
			return
		
		self.layer1 = np.random.random((3,9))
		self.layer2 = np.random.random((3,3))
		self.layer3 = np.random.random((9,3))
	
	
	def choose_move(self, board):
		'''
			chooses the move based on the values in it's layers
			Parameters:
				board (1x9 ndarray): the current tic tac toe board state
			
			Returns:
				ndarray: the array where the maximum value is the chose move
		'''
		return self.player * self.layer3@self.layer2@self.layer1@board

	def __mod__(self, other):
		if type(other) != type(self):
			raise ValueError(f"cannot broadcast between {type(other)} and {type(self)}")
		
		newmachine = TicEsMachina(1)
		layer1_stack = np.dstack((self.layer1, other.layer1))
		layer2_stack = np.dstack((self.layer2, other.layer2))
		layer3_stack = np.dstack((self.layer3, other.layer3))
		newmachine.layer1 = layer1_stack.mean(axis = 2)
		newmachine.layer2 = layer2_stack.mean(axis = 2)
		newmachine.layer3 = layer3_stack.mean(axis = 2)
		return newmachine

	def __str__(self):
		string = ""
		string += f'layer1:\n{self.layer1}\n\n'
		string += f'layer2:\n{self.layer2}\n\n'
		string += f'layer3:\n{self.layer3}\n\n'
		return string

	def write_to_file(self, foldername = "TTTmachine"):
		np.save(f'{foldername}/layer1', self.layer1)
		np.save(f'{foldername}/layer2', self.layer2)
		np.save(f'{foldername}/layer3', self.layer3)