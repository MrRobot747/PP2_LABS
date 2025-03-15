from functools import reduce
my_list = [1, 8, 6, 9, 2, 5]
red = reduce(lambda a, b : a*b, my_list)
print(red)
#4320