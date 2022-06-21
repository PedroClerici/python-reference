"""
For loops in Python:
"""

# number(start, [int], step):
for number in range(10):
    print(f'Number is: {number}')

text = 'Python'
new_str = ''

for word in text:
    if word == 'y' or word == 't':
        new_str += word.upper()
    else:
        new_str += word

print(new_str)