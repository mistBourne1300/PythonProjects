from random import triangular
from TTTboard import Board as bd
from TTTmachine import TicEsMachina
from TTTMinimax import Minimax
import numpy as np
import time
import matplotlib.pyplot as plt
from scipy.stats import linregress

def get_user_choice():
	row = -1
	col = -1
	while row < 0 or row > 2:
		row = int(input("enter the row (0-2): "))
	while col < 0 or col > 2:
		col = int(input("enter the col (0-2): "))
	return row, col

def human_v_human():
	player = 1
	game = bd()
	winner = 0
	while not game.check_full():
		print(game)
		if(player == 1):
			print("X's turn")
		else:
			print("O's turn")
		row, col = get_user_choice()
		while not game.make_move(player, row, col):
			print("invalid option(s) please input an unused row, col pair: ")
			row, col = get_user_choice()
		winner = game.check_win()
		if winner: break
		player *= -1
	print(game)
	if winner == 0:
		print("It's a draw!")
	elif winner == 1:
		print("X won!")
	elif winner == -1:
		print("O won")

def human_v_ai():
	game = bd()
	player_first = input("Do you want to play as X? [y/n]: ")
	if player_first == 'y':
		tim = TicEsMachina(-1,"TTTmachine")
	else: tim = TicEsMachina(1,"TTTmachine")
	player = 1
	winner = 0
	# human chose to go second
	# this makes a choice with the AI
	if player_first != 'y':
		choices = np.flip(np.argsort(tim.choose_move(np.ravel(game.board))))
		for i in range(9):
			choice = choices[i]
			row, col = choice // 3, choice % 3
			if game.make_move(player, row, col): break
		player *= -1
	
	while not game.check_full():
		print(game)
		if(player == 1):
			print("X's turn")
		else:
			print("O's turn")
		row, col = get_user_choice()
		while not game.make_move(player, row, col):
			print("invalid option(s) please input an unused row, col pair: ")
			row, col = get_user_choice()
		winner =  game.check_win()
		if winner: break
		player *= -1
		
		
		if(player == 1):
			print("X's turn")
		else:
			print("O's turn")
		
		choices = np.flip(np.argsort(tim.choose_move(np.ravel(game.board))))
		for i in range(9):
			choice = choices[i]
			row, col = choice // 3, choice % 3
			if game.make_move(player, row, col): break
		winner =  game.check_win()
		if winner: break
		player *= -1
	print(game)
	if winner == 0:
		print("It's a draw!")
	elif winner == 1:
		print("X won!")
	elif winner == -1:
		print("O won")
		
def ai_v_ai(tim, tem):
	game = bd()
	winner = 0
	player = 1
	while not game.check_full():
		print(game)
		if(player == 1):
			print("X's turn1")
		else:
			print("O's turn1")
		
		# tim chooses a move
		choices = np.flip(np.argsort(tim.choose_move(np.ravel(game.board))))
		for i in range(9):
			choice = choices[i]
			row, col = choice // 3, choice % 3
			if game.make_move(player, row, col):
				print(f'made move at {row,col}')
				break
			else:
				print(f'failed to make move at {row,col}')
			
		winner =  game.check_win()
		if winner: break
		player *= -1


		print(game)
		if(player == 1):
			print("X's turn2")
		else:
			print("O's turn2")
		# tem chooses a move
		choices = np.flip(np.argsort(tim.choose_move(np.ravel(game.board))))
		for i in range(9):
			choice = choices[i]
			row, col = choice // 3, choice % 3
			if game.make_move(player, row, col): 
				print(f'made move at {row,col}')
				break
			else:
				print(f'failed to make move at {row,col}')
		winner =  game.check_win()
		if winner: break
		player *= -1
	
	# final outcome decided
	print(game)
	if winner == 0:
		print("It's a draw!")
	elif winner == 1:
		print("X won!")
	elif winner == -1:
		print("O won")

def minimax():
	game = bd()
	player_first = input("Do you want to play as X? [y/n]: ")
	player = 1
	winner = 0
	if player_first == 'y':
		max = Minimax(-1)
	else:
		max = Minimax(1)
		max.move(game)
		player *= -1
		
	
	while not game.check_full():
		print(game)
		if(player == 1):
			print("X's turn")
		else:
			print("O's turn")
		
		row, col = get_user_choice()
		while not game.make_move(player, row, col):
			print("invalid option(s) please input an unused row, col pair: ")
			row, col = get_user_choice()
		winner = game.check_win()
		if winner: break
		player *= -1

		if(player == 1):
			print("X's turn")
		else:
			print("O's turn")
		
		max.move(game)
		winner = game.check_win()
		if winner: break
		player *= -1

	print(game)
	if winner == 0:
		print("It's a draw!")
	elif winner == 1:
		print("X won!")
	elif winner == -1:
		print("O won")

def mini_v_max():
	game = bd()
	mini = Minimax(-1)
	max = Minimax(1)

	while not game.check_full():
		print(game)
		print("X's turn:")
		max.move(game)
		winner = game.check_win()
		if winner: break
		print(game)
		print("O's turn:")
		mini.move(game)
		winner = game.check_win()
		if winner: break
	print(game)
	if winner == 0:
		print("It's a draw!")
	elif winner == 1:
		print("X won!")
	elif winner == -1:
		print("O won")
		

def get_winner(tim,tem):
	game = bd()
	winner = 0
	player = 1
	while not game.check_full():
		# tim chooses a move
		choices = np.flip(np.argsort(tim.choose_move(np.ravel(game.board))))
		for i in range(9):
			choice = choices[i]
			row, col = choice // 3, choice % 3
			if game.make_move(player, row, col): break
			
		winner =  game.check_win()
		if winner: break
		player *= -1


		# tem chooses a move
		choices = np.flip(np.argsort(tim.choose_move(np.ravel(game.board))))
		for i in range(9):
			choice = choices[i]
			row, col = choice // 3, choice % 3
			if game.make_move(player, row, col): break
		winner =  game.check_win()
		if winner: break
		player *= -1
	
	# final outcome decided
	return winner

def tourney(machines:list):
	""" takes in a list of machines and performs a single-elimination tournament
		to get the winner

		Parameters: 
			machines (list): a list of the machines to tourney
		
		Returns:
			winner (TicEsMachina): the machine that won

		note: ties are decided randomly which machine loses
	"""
	if(type(machines[0]) != TicEsMachina):
		raise ValueError("data type is not TicEsMachina")
	

	while len(machines)>1:
		machines[0].player = 1
		machines[-1].player = -1
		winner = get_winner(machines[0], machines[1])
		if not winner:
			removal = np.random.choice([0,-1])
			machines.pop(removal)
		elif winner == 1:
			machines.pop(-1)
		else:
			machines.pop(0)
		
	return machines[0]

if __name__ == "__main__":
	game = bd()

	HUMAN_V_HUMAN = 0
	HUMAN_V_AI = 1
	AI_V_AI = 2
	TRAIN_AI = 3
	MINIMAX = 4
	MINI_VS_MAX = 5

	POP_NUM = 100
	GEN_NUM = 1000

	print("Welcome to the Tic Tac Toe machine! Choose a play style:")
	print("Human v human: 0")
	print("Human v AI: 1")
	print("AI v AI: 2")
	print("Train AI (this will clear the current best AI): 3\n")
	print("Human vs Minimax: 4")
	print("Minimax vs Minimax: 5")

	choice = -1
	while choice < 0 or choice > 5:
		choice = int(input("Pick an option: "))
	
	if choice == HUMAN_V_HUMAN:
		human_v_human()
	elif choice == HUMAN_V_AI:
		human_v_ai()
	elif choice == AI_V_AI:
		tim = TicEsMachina(1,"TTTmachine")
		tem = TicEsMachina(-1)
		ai_v_ai(tim,tem)
	elif choice == TRAIN_AI:
		exxes = np.array([TicEsMachina(1) for i in range(POP_NUM)])
		ohhhs = np.array([TicEsMachina(-1) for i in range(POP_NUM)])
		training_times = []
		# for 1000 generations, pit the exxes and ohhhs together to find the best ones
		for i in range(GEN_NUM):
			start = time.time()
			print(f'generation {i}')
			try:
				winners = np.array([get_winner(exxes[i], ohhhs[i]) for i in range(POP_NUM)])
				save_x = winners>0
				save_o = winners<0
				exxes = exxes[save_x]
				ohhhs = ohhhs[save_o]
			except:
				print(f'winners length: {len(winners)}')
				print(f'save_x length: {len(save_x)}')
				print(f'save_o length: {len(save_o)}')
				print(f'exxes length: {len(exxes)}')
				print(f'ohhhs length: {len(ohhhs)}')
				print(f'\n\n save_x:\n{save_x}')
				print(f'\n\n save_o:\n{save_o}')
				raise NotImplementedError(f"failed at generation {i}")
			
			# mod the saved exxes together to have a population of 100 again 
			numx_saved = len(exxes)
			if numx_saved == 0:
				exxes = [TicEsMachina(1)]
				numx_saved+=1
			new_exxes = [ex for ex in exxes]
			# mix the first with the last, the second with the second to last, etc (all mod the length of the list, of course)
			for i in range(POP_NUM-numx_saved):
				new_exxes.append(exxes[i%len(exxes)]%exxes[-1*((len(exxes)-i-1)%len(exxes))])
			exxes = np.array(new_exxes)
			

			# mod the saved ohhhs together to have a population of 100 again 
			numo_saved = len(ohhhs)
			if numo_saved == 0:
				ohhhs = [TicEsMachina(-1)]
				numo_saved+=1
			new_ohhhs = [oh for oh in ohhhs]
			# same mixing as before
			for i in range(POP_NUM-numo_saved):
				new_ohhhs.append(ohhhs[i%len(ohhhs)]%ohhhs[-1*((len(ohhhs)-i-1)%len(ohhhs))])
			ohhhs = np.array(new_ohhhs)
			training_times.append(time.time() - start)
		
		print(f'calculating winner')
		# now we need to decide which machine to save
		winners = np.array([get_winner(exxes[i], ohhhs[i]) for i in range(POP_NUM)])
		save_x = winners>0
		save_o = winners<0
		exxes = exxes[save_x]
		ohhhs = ohhhs[save_o]
		numx_saved = len(exxes)
		numo_saved = len(ohhhs)
		if not numx_saved and numo_saved: # case where all the ohhhs won
			winner = tourney([o for o in ohhhs])
			winner.write_to_file()
		elif not numo_saved and numx_saved: # case where all the exxes won
			winner = tourney([x for x in exxes])
			winner.write_to_file()
		elif numo_saved and numx_saved: # there are some exxes and some ohhhs
			winx = tourney([x for x in exxes])
			wino = tourney([o for o in ohhhs])
			winner = get_winner(winx, wino)
			if not winner:
				winx.write_to_file()
			else:
				if(winner == 1):
					winx.write_to_file()
				else:
					wino.write_to_file()
		elif not numo_saved and not numx_saved: # this can only happen if eveyone ties, in which case it doesn't really matter which one we choos
			winner = exxes[0]
			winner.write_to_file()
		
		
		gens = np.arange(GEN_NUM)
		regress = linregress(gens, training_times)
		plt.plot(training_times)
		plt.title(f"generation vs computation time (r={regress[2]})")
		plt.xlabel("generation")
		plt.ylabel("computation time")
		plt.plot(regress[1] + regress[0]*gens)
		plt.savefig(f'Training_Times_Figs/{POP_NUM}for{GEN_NUM}.png')
		plt.show()
	elif choice == MINIMAX:
		minimax()
	elif choice == MINI_VS_MAX:
		mini_v_max()


		


