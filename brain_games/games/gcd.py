import random


RULE = 'Find the greatest common divisor of given numbers.'


def question_and_answer():
    number1 = random.randint(1, 100)
    number2 = random.randint(1, 100)
    question = f'{number1} {number2}'
    number = min(number1, number2)
    while number > 0:
        if number1 % number == 0 and number2 % number == 0:
            correct_answer = number
            break
        else:
            number = number - 1
    return question, correct_answer
