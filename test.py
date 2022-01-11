lst = ["hello", 'world',4,1,1,2,5,4]
WORD = 4
index = len(lst) - lst[::-1].index(WORD) - 1
print(index)
print(lst[:index])