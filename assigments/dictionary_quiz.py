#! /bin/python3

right_answers = 0
questions = {
    'Question 1': {
        'question': 'What is the formula to calculate the area of a circle?',
        'answers': {'a': 'd / 2', 'b': 'pi * r^2', 'c': 'b^2 + c^2', 'd': 'l^2'},
        'right answer': 'b',
    },
    'Question 2': {
        'question': 'What of those animals shed their skin?',
        'answers': {'a': 'Pig', 'b': 'Capybara', 'c': 'Monkey', 'd': 'Snake'},
        'right answer': 'd',
    },
    'Question 3': {
        'question': 'What is the closest planet to the sun in our solar system?',
        'answers': {'a': 'Mercury', 'b': 'Mars', 'c': 'Venus', 'd': 'Jupiter'},
        'right answer': 'a',
    },
}

for question_key, question_value in questions.items():
    print(f"{question_key}: {question_value['question']}")

    for answer_key, answer_value in question_value['answers'].items():
        print(f"{answer_key}: {answer_value}")

    user_answer = input('Enter your answer: ')

    if user_answer.lower() == question_value['right answer']:
        right_answers += 1

    print()

print(f'Correct answers: {right_answers} of {len(questions)}')
