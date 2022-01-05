from SolitaireStack import SolitaireStack
from SolitaireGame import SolitaireGame
from card import Card
import os


# TODO: clean up the print statements and add in clearing the output. Need to do the same for Solitaireplayer file
class SolitaireAlgor():
	def __init__(self, game:SolitaireGame):
		self.game = game
		self.made_move = False
		self.give_up = False
		self.prev_move = None
		self.prev_to_card = None
	
	def can_move(self, move_card : Card, to_card : Card):
		""" determines if the moving card can be placed on the other in the normal stacks
			
		Parameters: 
			move_card (Card): the moving card
			
			to_card (Card): the card being placed onto
		
		Returns: 
			(boolean): whether the moving card is able to be placed on the other in the normal stacks
		"""
		if not move_card: return False

		if move_card.rank == 13 and not to_card: return True
		
		if not to_card: return False
		
		return move_card.rank == to_card.rank - 1 and move_card.color != to_card.color
	
	def can_ace_move(self, move_card : Card, to_card : Card):
		""" determines if the moving card can be placed on the other in the ace stacks
			
		Parameters: 
			move_card (Card): the moving card
			
			to_card (Card): the card being placed onto
		
		Returns: 
			(boolean): whether the moving card is able to be placed on the other in the ace stacks
		"""
		if not move_card: return False
		
		if move_card.rank == 1 and not to_card: return True

		if not to_card: return False

		return move_card.rank == to_card.rank +1 and move_card.suit == to_card.suit

	def try_stacks_high(self):
		""" loops through the stacks searching for a move. if one is found, it will make the move and return True. Otherwise returns false
			
			Returns: 
				T/F (boolean): whether or not a move was made on the game
		"""
		print("try_stacks_high()")
		for i in range(len(self.game.SolitaireStacks)-1,-1,-1): # loop through all the stacks, starting at index 6
			move_card = self.game.SolitaireStacks[i].highFaceUpCard()
			print(f'i {i}: {move_card}')
			for j in range(len(self.game.SolitaireStacks)): # loop through all the stacks
				if(i==j): continue
				to_card = self.game.SolitaireStacks[j].lowFaceUpCard()
				print(f'\tj {j}: {to_card}')
				if (move_card is not self.prev_move) and self.can_move(move_card, to_card):
					# if the previous card to move was a king to an empty space, and the current card to move is a king to an empty space, quit
					if self.prev_move:
						if self.prev_move.rank == 13 and move_card.rank == 13 and not self.prev_to_card and not to_card: return False

					if not self.game.makeMove(0,i,j):
						print(f"failed to move {move_card} to {to_card}")
						raise ValueError()
					self.prev_move = move_card
					self.prev_to_card = to_card
					return True
		return False
	
	def try_stacks_low(self):
		""" loops through the stacks' low cards looking for a move to the aces
		
			Returns:
				(boolean): whether a move to the aces was made
		"""
		print("try_stacks_low()")
		for i in range(len(self.game.SolitaireStacks)-1,-1,-1):
			move_card = self.game.SolitaireStacks[i].lowFaceUpCard()
			if not move_card: continue
			print(f'i {i}: {move_card}')
			if move_card.rank == 1: # the card is an ace, we just need to move it to an empty stack
				if not self.game.makeMove(3,i): raise ValueError()
				self.prev_move = move_card
				self.prev_to_card = None
				return True
			for j in range(len(self.game.aceStacks)):
				to_card = self.game.aceStacks[j].lowFaceUpCard()
				if self.can_ace_move(move_card, to_card):
					if not self.game.makeMove(3,i): raise ValueError()
					self.prev_move = move_card
					self.prev_to_card = to_card
					return True
		return False

	def loop_through_helper(self):
		print("loop_through_helper()")
		if not self.game.helpStack.faceUpStack:
			self.game.makeMove(4,0,0)
		
		num_times_went_through = 0
		while num_times_went_through < 2 or self.game.helpStack.faceDownStack:
			move_card = self.game.helpStack.lowFaceUpCard()
			print(f'trying {move_card}')

			for i in range(len(self.game.aceStacks)): # check to see if the card can be moved to the ace stacks
				to_card = self.game.aceStacks[i].lowFaceUpCard()
				print(f'\tto: {to_card}')
				if self.can_ace_move(move_card, to_card):
					if not self.game.makeMove(2,0,-1):
						print(f'failed to move {move_card} to {to_card}')
						raise ValueError()
					self.prev_move = move_card
					self.prev_to_card = to_card
					return True
			
			for i in range(len(self.game.SolitaireStacks)): # check to see if the card can be moved to the regular stacks
				to_card = self.game.SolitaireStacks[i].lowFaceUpCard()
				print(f'\tto: {to_card}')
				if (move_card is not self.prev_move) and self.can_move(move_card, to_card):
					if not self.game.makeMove(2,0,i):
						print(f'failed to move {move_card} to {to_card}')
						raise ValueError()
					self.prev_move = move_card
					self.prev_to_card = to_card
					return True
			
			self.game.makeMove(4,0,0)
			if not self.game.helpStack.faceDownStack:
				num_times_went_through += 1
		
		return False
			
	def play(self):
		while not self.give_up and not self.game.checkWin():
			try:
				if self.try_stacks_low():
					print(self.game)
					continue
			except KeyboardInterrupt:
				print("threw error in self.try_stacks_low()")
				return self.game.checkWin()
			
			try:
				if self.try_stacks_high():
					print(self.game)
					continue
			except KeyboardInterrupt:
				print("threw error in self.try_stacks_high()")
				return self.game.checkWin()
			
			try:
				if not self.loop_through_helper(): self.give_up = True
			except KeyboardInterrupt:
				print("threw error in self.loop_through_helper()")
				return self.game.checkWin()
			print(f'give up: {self.give_up}')
			print(self.game)
		
		return self.game.checkWin()


if __name__ == "__main__":
	newDeck = [Card(s, i) for i in range(1,14) for s in ["S","H","C","D"]]
	newGame = SolitaireGame(newDeck)
	print(newGame)
	algor = SolitaireAlgor(newGame)
	win = algor.play()
	if win:
		print("game Freaking MATCH")
	else:
		print("try again")
