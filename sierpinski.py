import math
import os

os.system("clear")
os.chdir('/Users/chase/Desktop/Python')

num_levels = int(input("enter the number of levels to compute pascal's triangle to: "))


# get the max width of the numbers, just so we can format this correctly
max_width = len(str(math.comb(num_levels, int(num_levels/2))))

############INFO############
# the nth level has 2n+1 columns but we only print each every other column, 
# and alternating the starting index from 0 to 1 depending on whether the 
# index is even or odd

# build the 0th level and print
fill = [''.ljust(max_width-1) for i in range(num_levels)]

# build each level, then print to the screen
# each level has i+1 non-empty strings to format into the triangle
for i in range(0, num_levels+1):
	# print(f'amount of fill for this level: {num_levels - (i+1)}')
	for f in fill: print(f, end = '')
	for j in range(i+1): print(repr(math.comb(i,j)).ljust(max_width+1), end = '')
	print()
	if(not len(fill) == 0):
		fill.pop()

modulus = int(input("enter the modulus triangle you want me to find: "))
max_width = len(str(modulus-1))

file_out = open(f'pascal_mod_triangles/pascal_mod_{modulus}.txt', 'w')


fill = [''.rjust(max_width) for i in range(num_levels)]
for i in range(num_levels+1):
	build_string = ''
	for f in fill:
		build_string += f
	for j in range(i+1):
		build_string += repr(math.comb(i,j)%modulus).rjust(max_width+1)
	# for f in fill: print(f, end = '')
	# for j in range(i+1): print( repr(	math.comb(i,j)%modulus).rjust(max_width+1), end = '')
	print(build_string)
	file_out.write(f'{build_string}\n')
	if not len(fill) == 0:
		fill.pop()

file_out.close()