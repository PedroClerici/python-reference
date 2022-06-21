"""
Basic Control Flow in Python with (if, elif, else):
"""

password = 'p@ssword1234'

if len(password) > 12 and '@' in password:
    print('This password is STRONG!')
elif len(password) > 12:
    print('This password is mighty strong!')
elif len(password) > 8:
    print('This password is long enough.')
else:
    print('This password is not long enough.')