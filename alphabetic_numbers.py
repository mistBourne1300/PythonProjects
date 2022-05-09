import FourLoop as fl
import matplotlib.pyplot as plt

def sorted_alphas(highest):
	liszt = []
	for i in range(highest+1):
		liszt.append(fl.get_string(i))
		liszt.sort()
		yield liszt
	
if __name__ == "__main__":
	highest = int(input('enter highest integer: '))
	invhits =[]
	graph_potatoes = []
	match_potatoes = 0
	count_potatoes = 0
	for lzt in sorted_alphas(highest):
		count = 0
		for i in range(len(lzt)):
			if i == fl.string_to_num(lzt[i]):
				#print(i, '=', lzt[i])
				count += 1
				match_potatoes += 1
		invhits.append(count)
		print(count_potatoes, ':', match_potatoes)
		count_potatoes += 1
		graph_potatoes.append(match_potatoes)
	plt.plot(invhits)
	plt.xlabel('last number inserted')
	plt.ylabel('number of matches')
	plt.show()
	
	plt.plot(graph_potatoes)
	plt.xlabel('last number inserted')
	plt.ylabel('total number of matches')
	plt.show()
	
	print(fl.string_to_num('twenty two hundred',v=True))
