from TTTboard import Board as bd
from TTTmachine import TicEsMachina
import numpy as np

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
	tim = TicEsMachina("TTTmachine")
	player = 1
	winner = 0
	# human chose to go second
	# this makes a choice with the AI
	if player_first != 'y':
		choices = tim.choose_move(np.ravel(game.board))
		for i in range(9):
			choice = np.argmax(choices)
			choices[choice] = 0
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
		
		choices = tim.choose_move(np.ravel(game.board))
		for i in range(9):
			choice = np.argmax(choices)
			choices[choice] = 0
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
			print("X's turn")
		else:
			print("O's turn")
		
		# tim chooses a move
		choices = tim.choose_move(np.ravel(game.board))
		for i in range(9):
			choice = np.argmax(choices)
			choices[choice] = 0
			row, col = choice // 3, choice % 3
			if game.make_move(player, row, col): break
		winner =  game.check_win()
		if winner: break
		player *= -1


		print(game)
		if(player == 1):
			print("X's turn")
		else:
			print("O's turn")
		# tem chooses a move
		choices = tem.choose_move(np.ravel(game.board))
		for i in range(9):
			choice = np.argmax(choices)
			choices[choice] = 0
			row, col = choice // 3, choice % 3
			if game.make_move(player, row, col): break
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


	


if __name__ == "__main__":
	game = bd()

	HUMAN_V_HUMAN = 0
	HUMAN_V_AI = 1
	AI_V_AI = 2
	TRAIN_AI = 3

	print("Welcome to the Tic Tac Toe machine! Choose a play style:")
	print("Human v human: 0")
	print("Human v AI: 1")
	print("AI v AI: 2")
	print("Train AI (this will clear the current best AI): 3")
	choice = -1
	while choice < 0 or choice > 3:
		choice = int(input("Pick an option: "))
	
	if choice == HUMAN_V_HUMAN:
		human_v_human()
	elif choice == HUMAN_V_AI:
		human_v_ai()
	elif choice == AI_V_AI:
		tim = TicEsMachina("TTTmachine")
		tem = TicEsMachina()
		ai_v_ai(tim,tem)
	else:
		raise NotImplementedError("not yet implemented")


		


