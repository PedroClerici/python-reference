"""
For & Else in Python:
"""

names = ['Scott', 'Maria', 'Stephanie', 'Smith', 'Joel']

for name in names:
    if name.startswith('J'):
        print(f'{name} starts with "J".')
        break
else:
    print('There are no names in the list that starts with "j".')

