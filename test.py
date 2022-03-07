# from readline import read_init_file
# from joblib import PrintTime
# import numpy as np
# import re
# # import epitran as ep
# import time
# # import panphon


# N = 2000
# print_times = []
# print()
# for i in range(N+1):
# 	per = int(100*i/N)
# 	start = time.time()
# 	print(end = " [")
# 	[print(end = "#") for i in range(per)]
# 	[print(end = " ") for i in range(100-per)]
# 	print(f'] {i}/{N} ({per}%)', end = "\r")
# 	print_times.append(time.time() - start)
# 	time.sleep(5/N)
# print(f'\naverage time to print progress bar: {np.mean(print_times)}\n')

import epitran
epi = epitran.Epitran('eng-Latn')

print(epi.transliterate("hel.o"))