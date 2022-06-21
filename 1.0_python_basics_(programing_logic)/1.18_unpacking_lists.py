"""
Unpacking Lists on Python:
"""
color = ['#ff0000', '#00ff00', '#0000ff']
red, green, blue = color

print('The hex value of red is: ', red)
print('The hex value of green is: ', green)
print('The hex value of blue is: ', blue)

my_list = ['Scott', 'Maria', 'Pedro', 1, 2, 3, 4, 5, True]
name1, name2, name3, *numbers, last_value = my_list

print('Names: ' + name1, name2, name3, sep=', ')
print('Numbers: ', numbers)
print('Last value: ', last_value)
