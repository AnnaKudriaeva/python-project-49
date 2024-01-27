import random


RULE = 'What is the result of the expression?'

def get_calc(number1, number2, chosen_operator):
    if chosen_operator == '+':
        answer = number1 + number2
    elif chosen_operator == '-':
        answer = number1 - number2
    elif chosen_operator == '*':
        answer = number1 * number2
    return answer


def get_question_and_answer():
    number1 = random.randint(1, 100)
    number2 = random.randint(1, 100)
    operators = ['+', '-', '*']
    chosen_operator = random.choice(operators)
    correct_answer = get_calc(number1, number2, chosen_operator)
    question = f'{number1} {chosen_operator} {number2}'
    return question, correct_answer
