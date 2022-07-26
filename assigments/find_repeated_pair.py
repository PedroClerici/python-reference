"""
Assignment:
Create a function that returns the position and the value of a repeated pair of the same value.
"""

numbers_lists = [
    [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
    [9, 1, 8, 9, 9, 7, 2, 1, 6, 8],
    [1, 3, 2, 2, 8, 6, 5, 9, 6, 7],
    [3, 8, 2, 8, 6, 7, 7, 3, 1, 9],
    [4, 8, 8, 8, 5, 1, 10, 3, 1, 7],
    [1, 3, 7, 2, 2, 1, 5, 1, 9, 9],
    [10, 2, 2, 1, 3, 5, 10, 5, 10, 1],
    [1, 6, 1, 5, 1, 1, 1, 4, 7, 3],
    [1, 3, 7, 1, 10, 5, 9, 2, 5, 7],
    [4, 7, 6, 5, 2, 9, 2, 1, 2, 1],
    [5, 3, 1, 8, 5, 7, 1, 8, 8, 7],
    [10, 9, 8, 7, 6, 5, 4, 3, 2, 1],
]

def is_last_index(index, iterable):
    return index == len(iterable) - 1

def find_repeated_pair(numbers_list):
    for index, value in enumerate(numbers_list):
        if not is_last_index(index, numbers_list) and value == numbers_list[index + 1]:
            return (value, index)
        elif index == len(numbers_list): 
            return -1

for list_index, list_of_numbers in enumerate(numbers_lists):
    if find_repeated_pair(list_of_numbers):
        repeated_value, repeated_index = find_repeated_pair(list_of_numbers)
        feedback = '['
        for index, value in enumerate(list_of_numbers):
            if value == repeated_value and index == repeated_index:
                feedback += f'\033[91m-> {value}, {value}, <- \033[00m'
            elif index != repeated_index + 1 and is_last_index(index, list_of_numbers):
                feedback += f'{value}'
            elif index != repeated_index + 1:
                feedback += f'{value}, '
        feedback += ']'
        print(f'{list_index + 1}st: {feedback} Repeated pair of value: "{repeated_value}" in index: "{repeated_index}".')
    else:
        print(f'{list_index + 1}st: {list_of_numbers} Repeated pair not found.')