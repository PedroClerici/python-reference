"""
The tuple data type.
HINT: tuples are immutable data types. In other words
you can't change values in tuples.
"""

# Tuple example:
my_tuple = 1, 3.2, 'python'
my_tuple += 7,
print(my_tuple, type(my_tuple))

# One value tuple:
one_value = 1,
print(one_value, type(one_value))

# Repeating values:
numbers = (1, 2, 3, 4, 5) * 5
print(numbers, type(numbers))

# Converting tuples to lists:
numbers = list(numbers)
numbers[1] = 3000
print(numbers, type(numbers))
