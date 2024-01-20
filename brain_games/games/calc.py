#!/usr/bin/env python3
from brain_games.engine import game
import random


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

def run_game_calc():
    game(rule, is_number)
