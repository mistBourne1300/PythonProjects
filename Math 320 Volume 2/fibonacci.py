import os
import time

def fib_naive(n):
	#print("fib(", n, ")", sep = "")
	if(n == 0 or n == 1):
		return n
	return fib_naive(n-1) + fib_naive(n-2)


def fib_memo(n, dictionary = dict([])):
	#print(f'fib_memo({n})')
	if(n in dictionary):
		return dictionary[n]
	elif(n == 0 or n == 1):
		dictionary[n] = n
		return n
	dictionary[n] = fib_memo(n-1, dictionary) + fib_memo(n-2, dictionary)
	return dictionary[n]

def fib_iter(n):
	ith_fib = 0
	ith_plus_1_fib = 1
	nth_fib = 0
	for i in range(n):
		#print(ith_fib)
		nth_fib = ith_fib + ith_plus_1_fib
		ith_fib = ith_plus_1_fib
		ith_plus_1_fib = nth_fib
	return ith_fib

def time_fib_naive(n):
	start_time = time.time()
	fib_naive(n)
	end_time = time.time()
	return (end_time - start_time)

def time_fib_memo(n):
	dictionary = dict([])
	start_time = time.time()
	fib_memo(n)
	end_time = time.time()
	return (end_time - start_time)

def time_fib_iter(n):
	start_time = time.time()
	fib_iter(n)
	end_time = time.time()
	return (end_time - start_time)

def get_ordinal(n):
	if(n%10 == 1):
		return str(n) + "st"
	elif(n%10 == 2):
		return str(n) + "nd"
	elif(n%10 == 3):
		return str(n) + "rd"
	return str(n) + "th"

if __name__ == "__main__":
	n = int(input("Enter the fibonacci number you want me to find: "))
	# print("\n\n\ntiming naive approach")
	# start_time = time.time()
	# naive_fib = fib_naive(n)
	# end_time = time.time()
	# print(f'fib_naive({n}) = {naive_fib}. naive approach took {end_time - start_time} seconds\n\n\n')

	print('timing memoized approach')
	dictionary = dict([])
	start_time = time.time()
	memo_fib = fib_memo(n)
	end_time = time.time()
	print(f'fib_memo({n}) = {memo_fib}. memoized approach took {end_time - start_time} seconds\n\n\n')

	print('timing iterative approach')
	start_time = time.time()
	iter_fib = fib_iter(n)
	end_time = time.time()
	print(f'fib_iter({n}) = {iter_fib}. iterative approach took {end_time - start_time} seconds\n\n\n')

	sec_count = float(input("enter a number of seconds to find the nth computation that takes more than that number of seconds to complete for all three versions: "))
	n = 0
	while ((time_fib_naive(n) < sec_count) and (time_fib_memo(n) < sec_count) and (time_fib_iter(n) < sec_count)):
		print(f'{n} passed. trying {n+1}')
		n+=1
	
	print(f"the {get_ordinal(n-1)} fibonacci number is the largest number for which it took less than {sec_count} seconds for all three to solve")
	os.system('say "computation complete"')

	