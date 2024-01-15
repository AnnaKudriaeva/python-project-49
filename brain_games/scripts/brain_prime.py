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
    print('Answer "yes" if given number is prime. Otherwise answer "no".')


def is_number():
    number = random.randint(2, 100)
    is_prime = True
    for i in range(2, int(number**0.5) + 1):
        if number % i == 0:
            is_prime = False
            break
    if is_prime:
        correct_answer = 'yes'
    else:
        correct_answer = 'no'
    print(f'Question: {number}')
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