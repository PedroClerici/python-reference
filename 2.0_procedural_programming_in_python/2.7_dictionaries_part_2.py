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