from brain_games.engine import game
import random


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


def run_game_prime():
    game(rule, is_number)
