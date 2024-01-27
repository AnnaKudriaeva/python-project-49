import random


RULE = 'Answer "yes" if the number is even, otherwise answer "no".'


def is_even(question):
    if question % 2 == 0:
        answer = 'yes'
    else:
        answer = 'no'
    return answer


def get_question_and_answer():
    question = random.randint(2, 100)
    correct_answer = is_even(question)
    return question, correct_answer
