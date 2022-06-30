import numpy as np


def random_strat(num_priz:int):
	boxes_and_foxes = [i for i in range(num_priz)]
	np.random.shuffle(boxes_and_foxes)

	for i in range(num_priz):
		print(f'prizoner #{i}')
		choices = [i for i in range(num_priz)]
		np.random.shuffle(choices)
		found = False
		for j in range(num_priz//2):
			print(f"\ttry {j}: box {choices[j]}: {boxes_and_foxes[choices[j]]}")
			if boxes_and_foxes[choices[j]] == i:
				found = True
				break
		if not found:
			print(f"prisoner {i} failed")
			return False
		else:
			print(f'prisoner {i} succeeded')
	return True


def loop_strat(num_priz:int):
	boxes_and_foxes = [i for i in range(num_priz)]
	np.random.shuffle(boxes_and_foxes)

	for priz in range(num_priz):
		print(f'prisoner #{priz}', end = f"\n\t{priz}")
		curr_choice = priz
		found = False
		for choice in range(num_priz//2):
			next_box = boxes_and_foxes[curr_choice]
			print(f' -> {next_box}', end = " ")
			if next_box == priz:
				found = True
				break
			curr_choice = next_box
		print()
		if found:
			print(f"prisoner {priz} succeeded")
		else:
			print(f'prisoner {priz} failed')
			return False
	return True
			


if __name__ == "__main__":
	# print(random_strat(100))
	print(loop_strat(100))