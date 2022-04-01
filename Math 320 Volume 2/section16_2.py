import numpy as np

def solve_robot(T,rewards):
	optimums = {1:0,2:0,3:0,4:0,5:0,6:0,7:0,8:0,9:0}
	neighbors = {	1:(2,4),
					2:(1,3,5),
					3:(2,6),
					4:(1,5,7),
					5:(2,4,6,8),
					6:(3,5,9),
					7:(4,8),
					8:(5,7,9),
					9:()}
	for s in range(1,10):
		print(s)
		try:
			optimums[s] = max(rewards[a] for a in neighbors[s])
		except:
			optimums[s] = 0
	
	for t in range(T):
		temp = optimums.copy()
		for s in range(1,10):
			print(s)
			try:
				optimums[s] = max(rewards[a] + temp[a] for a in neighbors[s])
			except:
				optimums[s] = 0
	return optimums

		

if __name__ == "__main__":
	rewards={1:-1,2:.7,3:-1,4:-1,5:-1,6:-1,7:-1,8:-1,9:-1}
	print(solve_robot(1,rewards))