"""
Formatting Strings
"""
name = 'Pedro Clerici'
age = 18
weight = 72
height = 1.79
bmi = weight / height**2

print('His name is', name + ', he is', age, 'years old and his BMI is:', bmi)
print(f'His name is {name}, he is {age} years old and his BMI is: {bmi:.2f}')
print('His name is {}, he is {} years old and his BMI is: {:.2f}'.format(name, age, bmi))
print('His name is {1}, he is {0} years old and his BMI is: {2:.2f}'.format(age, name, bmi))
