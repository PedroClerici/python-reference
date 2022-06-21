"""
Formatting values in Python:
:s - for strings (str)
:d - for integers (int)
:f - for float points (float)
:.(num)f - quantity of decimal numbers (float)
:(char)(> or < or ^)(quantity)(type - s, d or f)

> - Left
< - Right
^ - Center
"""

num_1 = 10
num_2 = 3
division = num_1 / num_2
print(f'{division:.2f}')
print('{:.3f}'.format(division))

num_3 = 1
print(f'{num_3:0<10}')
num_4 = 2241
print(f'{num_4:0^10}')

name = 'Pedro Clerici'
print(f'{name:-^21}')
