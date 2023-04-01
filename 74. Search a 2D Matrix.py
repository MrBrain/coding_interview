from functools import reduce
matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]]


new_list = reduce(lambda merge, ele : merge + ele, matrix, [])

print(new_list)