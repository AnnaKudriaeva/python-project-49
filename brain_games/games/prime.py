import random


RULE = 'Answer "yes" if given number is prime. Otherwise answer "no".'


def is_prime(question):
    is_prime = True
    for i in range(2, int(question**0.5) + 1):
        if question % i == 0:
            is_prime = False
            break
    if is_prime:
        answer = 'yes'
    else:
        answer = 'no'
    return answer


def question_and_answer():
    question = random.randint(2, 100)   
    correct_answer = is_prime(question)
    return question, correct_answer
