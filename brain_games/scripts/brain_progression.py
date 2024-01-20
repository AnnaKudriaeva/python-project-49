#!/usr/bin/env python3

from brain_games.engine import game
from brain_games.games.progression import is_number


def main():
    game(is_number)


if __name__ == '__main__':
    main()
