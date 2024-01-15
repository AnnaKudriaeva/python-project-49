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
    print('What number is missing in the progression?')


def is_number():
    start_value = random.randint(1, 10)
    difference = random.randint(1, 5)
    num_elements = 10
    progression = [start_value + i * difference for i in range(num_elements)]
    index_to_replace = random.randint(0, len(progression) - 1)
    replaced_number = progression[index_to_replace]
    progression[index_to_replace] = '..'
    progression = ' '.join(map(str, progression))
    print(f'Question: {progression}')
    return replaced_number


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
