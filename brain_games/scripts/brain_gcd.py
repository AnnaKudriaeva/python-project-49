#!/usr/bin/env python3

from brain_games.engine import game
from brain_games.games.gcd import is_number, rule


def main():
    game(rule, is_number)


if __name__ == '__main__':
    main()
