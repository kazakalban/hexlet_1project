from random import randint  # Стандартная библиотека

import prompt  # Внешние библиотеки

from brain_games.cli import welcome_user as main_user_name  # Локальные модули
from brain_games.scripts.brain_games import max_raund_game as max_raund

def is_even(number: int) -> bool:
    return number % 2 == 0 


def game_parity_check(max_rounds):
    user_name = main_user_name()
    print('Answer "yes" if the number is even, otherwise answer "no".')
    correct_answers = 0

    while correct_answers < max_rounds:
        number = randint(1, 100)
        print(f'Question: {number}')
        user_answer = prompt.string('Your answer: ').lower()

        if user_answer not in ('yes', 'no'):
            print(f"Incorrect answer. Let's try again, {user_name}!")
            break

        correct_answer = 'yes' if is_even(number) else 'no'

        if user_answer == correct_answer:
            print("Correct!")
            correct_answers += 1
        else:
            print(f"'{user_answer}' is wrong answer ;(.")
            print(f"Correct answer was '{correct_answer}'")
            print(f"Let's try again, {user_name}!")
            break

    if correct_answers == max_rounds:
        print(f'Congratulations, {user_name}!')


def main():
    game_parity_check(max_raund)


if __name__ == "__main__":
    main()
