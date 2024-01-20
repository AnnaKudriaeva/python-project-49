from brain_games.engine import game
import random


def rule():
    print('Answer "yes" if the number is even, otherwise answer "no".')


def is_number():
    number = random.randint(2, 100)
    print(f'Question: {number}')
    if number % 2 == 0:
        correct_answer = 'yes'
    else:
        correct_answer = 'no'
    return correct_answer


def run_game_even():
    game(rule, is_number)
