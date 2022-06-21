"""
The conditional "or"
"""
name = input('Please enter your name: ')

print(name or "You typed nothing.")

a = 0
b = None
c = False
d = []
e = {}
f = 22
g = 'Snake'

variable = a or b or c or d or e or f or g

print('The value of variable is: ', variable)