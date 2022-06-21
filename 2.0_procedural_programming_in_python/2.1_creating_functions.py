"""
Creating functions with "def"
"""
# Defining a function:
def greeting(time='day', name='user'):
    print(f'Good {time}, {name}!')

# Invoking / calling a function:
greeting()
greeting('evening', 'Pedro')
greeting(name='Pedro', time='evening')
greeting('morning', 'Maria')

# Returning values:
def add(var1, var2):
    return var1 + var2

print(add(2, 2))

# Functions as values
def dump():
    return 1

var = dump
print(type(var), var())