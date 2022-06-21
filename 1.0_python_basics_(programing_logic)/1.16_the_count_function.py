"""
The count() function
"""

fun_fact = 'A snake shed their skin for the reason of allowing further growth of their scales.'
words = []
counter = 0
most_repeated_word = ''

for word in fun_fact.split(' '):
    words.append(word.lower())

for word in words:
    times_appeared = words.count(word)

    if times_appeared > counter:
        counter = times_appeared
        most_repeated_word = word

print(f'"{most_repeated_word}" is most repeated word in the phrase:\n{fun_fact}')




