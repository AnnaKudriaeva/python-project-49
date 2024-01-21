import random


RULE = 'What is the result of the expression?'


def question_and_answer():
    number1 = random.randint(1, 100)
    number2 = random.randint(1, 100)
    operators = ['+', '-', '*']
    chosen_operator = random.choice(operators)
    if chosen_operator == '+':
        correct_answer = number1 + number2
    elif chosen_operator == '-':
        correct_answer = number1 - number2
    elif chosen_operator == '*':
        correct_answer = number1 * number2
    question = f'{number1} {chosen_operator} {number2}'
    return question, correct_answer
