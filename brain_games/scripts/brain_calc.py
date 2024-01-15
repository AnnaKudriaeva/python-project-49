#!/usr/bin/env python3

import prompt
import random


def greet():
    print('Welcome to the Brain Games!')


def welcome_user():
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}!')
    return name


def rule():
    print('What is the result of the expression?')


def is_number():
    number1 = random.randint(1, 100)
    number2 = random.randint(1, 100)
    operators = ['+', '-', '*']
    chosen_operator = random.choice(operators)
    expression = f'{number1} {chosen_operator} {number2}'
    correct_answer = eval(expression)
    print(f'Question: {expression}')
    return correct_answer


def your_answer():
    answer = prompt.string('Your answer: ')
    return answer


def game():
    name = welcome_user()
    rule()
    n = 0
    while n < 3:
        correct_answer = is_number()
        answer = your_answer()
        if str(answer) == str(correct_answer):
            print('Correct!')
            n += 1
            continue
        elif str(answer) != str(correct_answer):
            print(
                f"'{answer}' is wrong answer ;(. Correct answer was '{correct_answer}'.\nLet's try again, {name}!"
                )
            break
    if n == 3:
        print(f'Congratulations, {name}!')


def main():
    greet()
    game()


if __name__ == '__main__':
    main()
