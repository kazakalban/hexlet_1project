from random import randint  # Стандартная библиотека
from math import gcd

import prompt  # Внешние библиотеки

from brain_games.cli import welcome_user as main_user_name  # Локальные модули
from brain_games.scripts.brain_games import max_raund_game as max_raund


def find_gcd(max_raund):
    user_name = main_user_name()
    correct_answer = 0
    print('Find the greatest common divisor of given numbers.')
    while correct_answer < max_raund:
        while True:
            number_a, number_b = randint(1, 25), randint(1, 25)
            if number_a != number_b and gcd(number_a, number_b) != 1:
                break

        number_gcd = gcd(number_a, number_b)
        print(f'Question: {number_a} {number_b}')
        user_answer = prompt.integer('Your answer: ')

        if user_answer == number_gcd:
            print('Correct!')
            correct_answer += 1
        else:
            print(f"'{user_answer}' is wrong answer ;(.")
            print(f"Correct answer was '{correct_answer}'")
            print(f"Let's try again, {user_name}!")
            break
        if correct_answer == max_raund:
            print(f'Congratulations, {user_name}!')


def main():
    find_gcd(max_raund)


if __name__ == "__main__":
    main()
