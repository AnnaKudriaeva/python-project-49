#!/usr/bin/env python3
from brain_games.games.gcd import get_question_and_answer, RULE
from brain_games.engine import run_game


def main():
    run_game(RULE, get_question_and_answer)


if __name__ == '__main__':
    main()
