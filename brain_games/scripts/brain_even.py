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
    print('Answer "yes" if the number is even, otherwise answer "no".')


def is_number():
    number = random.randint(1, 100)
    print(f'Question: {number}')
    return number


def your_answer():
    answer = prompt.string('Your answer: ')
    return answer


def game():
    name = welcome_user()
    rule()
    n = 0
    while n < 3:
        number = is_number()
        answer = your_answer()
        if (
            answer == 'yes' and number % 2 == 0
            ) or (
                answer == 'no' and number % 2 != 0
                ):
            print('Correct!')
            n += 1
            continue
        elif (answer == 'yes' and number % 2 != 0):
            print("'yes' is wrong answer ;(. Correct answer was 'no'.")
            print(f"Let's try again, {name}!")
            break
        elif (answer == 'no' and number % 2 == 0):
            print("'no' is wrong answer ;(. Correct answer was 'yes'.")
            print(f"Let's try again, {name}!")
            break
        else:
            print(f"'{answer}' is wrong answer ;(.\nLet's try again, {name}!")
            break
    if n == 3:
        print(f'Congratulations, {name}!')


def main():
    greet()
    game()


if __name__ == '__main__':
    main()
