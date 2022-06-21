"""
Strings Index:
"""
my_str = 'Python <3'
# Positives [012345678]
print(my_str[0])
print(my_str[8])

# Negatives -[987654321]
print(my_str[-1])
print(my_str[-4])

# Cutting strings
new_str = my_str[:6]
print(new_str)

heart = my_str[7:]
print(heart)

step = my_str[0::2]
#step = my_str[0:6:2]
print(step)

for word in my_str:
    print(word)