"""
split(), join() & enumerate() in Python:
* split - divides a string in determined character.
* join - concatenate a list / string.
* enumerate - enumerate element in a list.
"""

phrase = 'Snakes are fun & dangerous.'
words = phrase.split(' ')

print('The value of words is: ', words)
print(f'Making the words array back to a string using "join()":\n{" ".join(words)}')

for index, value in enumerate(words): # <- NOTE: enumerate returns a tuple.
    print(index, value)

# Doing the same thing of enumerate() but with lists
list_2d = [
    [1, 2],
    [3, 4],
    [5, 6],
]

for value1, value2 in list_2d:
    print(value1, value2)