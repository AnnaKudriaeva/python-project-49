import random


RULE = 'Answer "yes" if given number is prime. Otherwise answer "no".'


def question_and_answer():
    question = random.randint(2, 100)
    is_prime = True
    for i in range(2, int(question**0.5) + 1):
        if question % i == 0:
            is_prime = False
            break
    if is_prime:
        correct_answer = 'yes'
    else:
        correct_answer = 'no'
    return question, correct_answer
