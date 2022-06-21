"""
Primitive data types:
str - string
int - integer
float - float point number
bool - boolean
"""
x = 10.7
y = True
z = 'Hello, world!'

# Printing the type of a variable:
print(x, type(x))
print(y, type(y))
print(z, type(z))

# Type conversion:
name = 'Pedro'
number = '1070'
print(type(name), bool(name))
print(type(number), int(number))

# Concatenation vs addition
print(10 + 10)
print('10' + '10')
print('10' + 10) # <- This is not JavaScript LMAO.
