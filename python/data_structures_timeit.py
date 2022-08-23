from timeit import timeit
# from time import time

# Making Lists:

# 1) for loop and append

testcode_loop = '''
squares = list()
for i in range(10):
    squares.append(i**2)   
#print("squares:", squares)
'''
print("for-loop time:", timeit(stmt=testcode_loop))

# 2) map object: function and iterable

testcode_map = '''
def compute_square(x):
    return x * x
square_roots = []
for i in range(10):
    square_roots.append(i)
squares = list(map(compute_square, square_roots))
'''
print("map time:", timeit(stmt=testcode_map))

# 3) list comprehension
testcode_listcomprehension = '''
squares = [x*x for x in range(10)]
'''
print("list_comprehension time:", timeit(stmt=testcode_listcomprehension))
