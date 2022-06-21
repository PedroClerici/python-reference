"""
Lists on Python:
"""

#       +   0    1    2    3    4
my_list = ['A', 'B', 'C', 'D', 'E']
#       -   5    4    3    2    1

# Reversing a list
print(my_list[::-1])

list1 = [1, 2, 3]
list2 = [4, 5, 6]

# List concatenation
list3 = list1 + list2
list3.append(7)
# insert(index, value)
list3.insert(0, 0)

print(list3)

del(list3[3:6])
print(list3)
