class Piece:
	
	def __init__(self, type = 'p'):
		self.type = type
		if (type == 'k'):
			self.value = 10000
		elif type == 'q':
			self.value = 9
		elif type == 'r':
			self.value = 4
		elif type == 'n':
			self.value = 3
		elif type == 'b':
			self.value = 3
		else:
			self.value = 1
		
	def __str__(self): return self.type
	
	def make_black(self): self.value *= -1