# Flatten a 2D list in Python
flatten_2d_list = lambda lst: [item for sublist in lst for item in sublist]
print(flatten_2d_list([[1, 2, 3], [4,5], [6]]))  # Output: [1, 2, 3, 4, 5, 6]
print(flatten_2d_list([['a', 'b'], ['c', 'd', 'e'], ['f']]))  # Output: ['a', 'b', 'c', 'd', 'e', 'f']



# Flatten a 2D list using sum
flatten_2d_list_sum = lambda lst: sum(lst, [])
print(flatten_2d_list_sum([[1, 2], [3, 4], [5]]))  # Output: [1, 2, 3, 4, 5]
print(flatten_2d_list_sum([['x', 'y'], ['z']])) # Output: ['x', 'y', 'z']

# Flatten a 2D list using itertools.chain
from itertools import chain
flatten_2d_list_chain = lambda lst: list(chain.from_iterable(lst))
print(flatten_2d_list_chain([[10, 20], [30, 40], [50]]))  # Output: [10, 20, 30, 40, 50]
print(flatten_2d_list_chain([['foo'], ['bar', 'baz']]))  # Output: ['foo', 'bar', 'baz']    

