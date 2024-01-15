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
    print('Find the greatest common divisor of given numbers.')


def is_number():
    number1 = random.randint(1, 100)
    number2 = random.randint(1, 100)
    expression = f'{number1} {number2}'
    if number1 >= number2:
        num = number2
    else:
        num = number1
    while num > 0:
        if number1 % num == 0 and number2 % num == 0:
            correct_answer = num
            break
        else:
            num = num - 1
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
        corr_ans = is_number()
        ans = your_answer()
        if str(ans) == str(corr_ans):
            print('Correct!')
            n += 1
            continue
        elif str(ans) != str(corr_ans):
            print(
                f"'{ans}' is wrong answer ;(. Correct answer was '{corr_ans}'."
                )
            print(f"Let's try again, {name}!")
            break
    if n == 3:
        print(f'Congratulations, {name}!')


def main():
    greet()
    game()


if __name__ == '__main__':
    main()
