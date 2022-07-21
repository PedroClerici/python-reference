"""
The set data type.
HINT 1: Sets can only contains unique values. In other words
sets can't have repeated data in it.
HINT 2: Sets also only supports immutable elements (objects),
like: ints, strings, floats, tuples, etc...
"""

# Set example:
lucky_numbers = {1, 2, 3, 4, 5}
# HINT 3: If you don't add values to a set like: {} it will be
# considered a dictionary.
# To create a empty set use: set()

my_set = set()
# Adding values to a set:
my_set.add('Hello, world!')
my_set.add(1)
my_set.add(('kingsnake', 4, 5, 6))
# Removing values from a set:
my_set.discard(2)

print(my_set)

# The update method in a set, receives a iterables value and adds
# every instance to the set:
lucky_numbers = set()
lucky_numbers.update([28, 46, 74, 32])
# HINT 4: also notice that sets "doesn't maintain orders".
print(lucky_numbers)

# One of the most common uses of sets is to remove repeated values
# from a iterable:
random_numbers = [1, 2, 2, 2, 3, 4, 4, 5, 5, 5, 5, 'hello', 'hello', 'again']
random_numbers = set(random_numbers)
# You can also easily revert it back to a list:
random_numbers = list(random_numbers)
print(random_numbers)

my_numbers = {1, 2, 3, 4, 5, 32}
more_numbers = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10}
# Intersecting sets (&) returns a new set containing only values that exists
# between the two sets.
print('Intersection: ',my_numbers & more_numbers)
# Uniting sets (|) returns a new set containing values presets between two sets:
print('Union: ', my_numbers | more_numbers)
# Getting the difference (-) between two sets. Notice that order meters.
print('Difference: ', my_numbers - more_numbers)
print('Difference 2: ', more_numbers - my_numbers)