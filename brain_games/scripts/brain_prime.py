#!/usr/bin/env python3
from brain_games.games.prime import get_question_and_answer, RULE
from brain_games.engine import run_game


def main():
    run_game(get_question_and_answer, RULE)


if __name__ == '__main__':
    main()
