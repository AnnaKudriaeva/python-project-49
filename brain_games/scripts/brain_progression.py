#!/usr/bin/env python3
from brain_games.games.progression import RULE, question_and_answer
from brain_games.engine import game


def main():
    game(RULE, question_and_answer)


if __name__ == '__main__':
    main()
