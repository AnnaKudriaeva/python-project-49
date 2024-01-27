import random


RULE = 'Find the greatest common divisor of given numbers.'


def get_gcd(number1, number2, number):
    while number > 0:
        if number1 % number == 0 and number2 % number == 0:
            answer = number
            break
        else:
            number = number - 1
    return answer


def get_question_and_answer():
    number1 = random.randint(1, 100)
    number2 = random.randint(1, 100)
    question = f'{number1} {number2}'
    number = min(number1, number2)
    correct_answer = get_gcd(number1, number2, number)
    return question, correct_answer
