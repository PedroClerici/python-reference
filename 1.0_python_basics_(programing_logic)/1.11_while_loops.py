"""
While loops in Python:
"""

# while True:
#     name = input('Hello, what is your name?: ')
#     print(f'Hello {name}, how are you?')

counter = 0
while counter < 100:
    print(f'In loop {counter}')
    counter += 1
else:
    print('The loop is done!')


# counter = 0
# while counter < 100:
#     if counter == 5:
#         continue # Continue to the next loop
#
#     print(f'In loop {counter}')
#     counter += 1

# counter = 0
# while counter < 100:
#     print(f'In loop {counter}')
#     counter += 1
#
#     if counter == 5:
#         break  # Breaks from the loop
