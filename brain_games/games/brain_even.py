import random


def is_number():
    number = random.randint(1, 100)
    print(f'Question: {number}')
    if number % 2 == 0:
        correct_answer = 'yes'
    else:
        correct_answer = 'no'
    return correct_answer
