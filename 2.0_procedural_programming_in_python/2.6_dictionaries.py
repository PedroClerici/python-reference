"""
Dictionaries
"""

# Dictionary example:
my_car = {
  'brand': 'Ford',
  'model': 'Mustang',
  'year': 1964
}
print(my_car['model'])
# or
# print(my_car.get('model'))

# Keys in a dictionary can have different data types
random_dictionary = {
  1: 'Hello',
  (1, 7, 2): [7, 2,1],
  'PI': 3.14,
}
print(random_dictionary[(1, 7, 2)], random_dictionary['PI'])

# Adding or updating values in dictionaries:
random_dictionary[0] = "Hi, i'm a new value!"
# or
# random_dictionary.update({0: "Hi, i'm a new value!"})

# Removing values in dictionaries:
del random_dictionary[0]

# Check if a key is in a dictionary
if 0 in random_dictionary:
  print(random_dictionary[0])
else:
  print('There is no key with the value of "0" in the "random_dictionary".')
# or
# if random_dictionary.get(0):
#   print(random_dictionary[0])
# else:
#   print('There is no key with the value of "0" in the "random_dictionary".')

# Since dictionaries are iterable you can use "for" to do something with the keys.
for key in random_dictionary:
  print(key, random_dictionary[key], sep=': ')
# or
for key, value in random_dictionary.items():
  print(key, value, sep=': ')

# Dictionaries inside dictionaries:
users = {
    'user1': {
        'name': 'steve',
        'email': 'st3v3@example.com',
    },
    'user2': {
        'name': 'scott',
        'email': 'scott.brown@example.com',
    },
}
for user_key, user_value in users.items():
    print('\nShowing: ' + user_key)
    for key, value in user_value.items():
       print(f'{key}: {value}')