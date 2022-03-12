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

# import numpy as np

# alpha = 'qwertyuiopasdfghjklzxcvbnm1234567890!@#$%^&*()QWERTYUIOP|ASDFGHJKL:"ZXCVBNM<>?-=_+[]\;,./'
# alpha = list(alpha)
# for i in range(100000):
# 	print(np.random.choice(alpha), end = "")

lzt = ['98595', '32791', '28392', '77323', '92715', '26083', '130094', '99464', '12846', '332', '106064', '31328', '86049', '123900', '74923', '90571', '119538', '139197', '116900', '15672']
lzt.sort()
print(lzt)