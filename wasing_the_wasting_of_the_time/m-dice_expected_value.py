from numpy import roll
from pytz import country_names


class base_n_counter:
	def __init__(self, base:int):
		self.base = base
	
	def _tostring(self, curr:list):
		retrun = ''
		for d in curr:
			retrun += f'{d}|'
		return retrun
	
	def _need_digit(self, curr:list):
		for d in curr:
			if d != self.base-1:
				return False
		return True
	
	def count_to(self, n:int):
		curr = [0]
		for i in range(n):
			yield self._tostring(curr)
			if self._need_digit(curr):
				curr.insert(0,0)
			for d in range(len(curr)-1, -1, -1):
				if curr[d]+1 != self.base:
					curr[d] += 1
					break
				curr[d] = 0


def count_rolls_highest(high:int, m:int):
	'''	counts the number of ways we can roll <m> dice with the best roll being <high>.
		assumes the dice have at least <m> sides
			Parameters:
				high (int) : the value of the highest roll
				m (int) : the number of dice we are rolling
		
			Returns:
				count (int) : the number of possible ways to roll m dice with the highest being <high>
	'''
	basehigh = base_n_counter(high)
	num_poss = high**m
	count = 0
	for i,s in enumerate(basehigh.count_to(num_poss)):
		# print(f'\tpossibility no. {i}: ' + s)
		roll_list = [int(i) for i in s.split('|')[:-1]]
		# print(roll_list)

		if high-1 in roll_list:
			count += 1
	return count

if __name__ == "__main__":
	# basen = base_n_counter(60)
	# for i,s in enumerate(basen.count_to(120)):
	# 	print(i,s)
	
	n = int(input("enter number of sides: "))
	m = int(input("enter number of rolls for advantage: "))
	weighted_sum = 0
	for high in range(1,n+1):
		print(f'counting with {high} being highest roll')
		# count = count_rolls_highest(high,m)
		# print(f'\tcounting: {count}; arithmetic: {high**m - (high-1)**m}')
		weighted_sum += high * (high**m - (high-1)**m)
	
	expected_value = weighted_sum / (n**m)
	print(f'the expected value for {m}d{n}\'s with advantage is {expected_value}')
