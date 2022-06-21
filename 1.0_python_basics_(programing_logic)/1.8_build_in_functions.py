num_1 = input('Please type a number: ')
num_2 = input('Please type another number: ')

if num_1.isnumeric() and num_2.isnumeric():
    print(f'The addition of {num_1} and {num_2} is {int(num_1) + int(num_2)}')
else:
    print('ERROR: invalid user input!')
