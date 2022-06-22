import copy
"""
Reference, Shallow copy & Deep copy.
"""

my_array = ['Scott', 3.14, {'state': 'texas'}]

# Reference example:
my_array_reference = my_array
my_array_reference[0] = 'Steve'
print('my_array:', my_array)
print('my_array_reference:', my_array_reference)

# Shallow copy example:
my_array_shallow_copy = my_array.copy()
my_array_shallow_copy[0] = 'Maria'
my_array_shallow_copy[-1]['state'] = 'California'
print('my_array:', my_array)
print('my_array_shallow_copy:', my_array_shallow_copy)

# Deep copy example:
my_array_deep_copy = copy.deepcopy(my_array)
my_array_deep_copy[0] = 'Joseph'
my_array_deep_copy[-1]['state'] = 'Florida'
print('my_array:', my_array)
print('my_array_deep_copy:', my_array_deep_copy)
