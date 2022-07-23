"""
List Comprehension
Lists comprehensions in python gives you two mains things 
in python, faster performance and less code.
"""

# List comprehension example:
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
times_two = [number * 2 for number in numbers]
print(times_two)

# Returning all numbers that are divisible by 3:
get_devisable_by_three = [number for number in numbers if number % 3 == 0]
print(get_devisable_by_three)

# Return a string if number telling if a number is devisable or not
# by 2 or not:
is_devisable_by_two = [
    f'{number} is devisable by 2' 
    if number % 2 == 0
    else f'{number} is not devisable by 2'
    for number in numbers
]
for number in is_devisable_by_two: print(number)

# Manipulating strings:
names = ['Steve', 'Scott', 'Maria', 'Clarence']
rules = {'t': '7', 'o': '0', 'e': '3', 'a': '4', 'i': '1'}

def replace_all(string: str, rules: dict) -> str:
    for __old, __new in rules.items():
        string = string.replace(__old, __new)
    return string

usernames = [replace_all(name, rules) for name in names]
print(usernames)

# I have no idea what a i did here:
# class User:
#     username: str
#     hobbies: list

#     def __init__(self,username: str, hobbies: list): 
#         self.username = username
#         self.hobbies = hobbies

#     def add_hobby(self, hobby: str):
#         hobbies.append(hobby)

#     def print_hobbies(self):
#         for hobby in self.hobbies: print(hobby)

# hobbies = ['Painting', 'Skating', 'Weight Lifting']
# users = [User(username, list()).add_hobby(hobby) for username in usernames for hobby in hobbies]

# # Giving hobbies to users:
# users = [user.add_hobby(hobby) for user in users for hobby in hobbies]
# print(users)

# for user in users:
#     print(f'Username: {user.username}, Hobbies: {user.hobbies}')