#!/usr/bin/env python3

from brain_games.engine import game, greet
from brain_games.games.brain_prime import is_number


def main():
    greet()
    game(is_number)


if __name__ == '__main__':
    main()
