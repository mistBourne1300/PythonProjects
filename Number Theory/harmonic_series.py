if __name__ == "__main__":
	n = int(input("how many terms do you want to compute? "))
	harmonic_n = 0
	for i in range(1,n+1):
		harmonic_n += 1/i
		print(harmonic_n)
	