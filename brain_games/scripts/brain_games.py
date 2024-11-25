#!/usr/bin/env python3
from brain_games.cli import welcome_user

max_raund_game = 3  # Максимальное количество раундов одинаково для всех игр


def greet(text):
    print(text)


def main():
    greet("Welcome to the Brain Games!")
    welcome_user()


if __name__ == '__main__':
    main()
