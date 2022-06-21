"""
*args & **kwargs

args = arguments (tuple)
kwargs = keyword arguments (tuple)
"""

# Using *args:
def add(*nums):
    addition = 0
    for num in nums:
        addition += num

    return addition

print(add(1, 7, 8, 10, 11))

# Unpacking lists:
nums = [1, 2, 3, 4, 5]
print(add(*nums, 6, 7, 8, 9, 10))

# Using **kwargs
def fullname(**kwargs):
    print(kwargs['name'], kwargs['middle_name'], kwargs['last_name'])

fullname( last_name='Clerici', name='Pedro', middle_name='Henrique', food='banana')
