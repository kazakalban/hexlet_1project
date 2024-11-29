from random import randint  # Стандартная библиотека

import prompt  # Внешние библиотеки

from brain_games.cli import welcome_user as main_user_name  # Локальные модули
from brain_games.scripts.brain_games import max_raund_game as max_raund


def find_progression(max_raund):
    user_name = main_user_name()
    print('What number is missing in the progression?')
    correct_answer = 0
    while max_raund != correct_answer:
        number_start = randint(1, 10)  # старт
        progress_list = []  # массив чисел
        number_progress = randint(2, 5)  # прогресс
        list_len = randint(5, 10)  # длина массива

        while len(progress_list) != list_len:
            # создаем массив с рандомными числами
            number_start += number_progress
            progress_list.append(number_start)

        secret_position = randint(0, list_len - 1)
        # определим позицию для скрытия
        secret_number = progress_list[secret_position]
        # сохраняем правильный число
        progress_list[secret_position] = '..'
        print('Question:', *progress_list)
        user_answer = prompt.integer('Your answer: ')
        if user_answer == secret_number:
            print('Correct!')
            correct_answer += 1
        else:
            print(f"'{user_answer}' is wrong answer ;(.")
            print(f"Correct answer was '{correct_answer}'")
            print(f"Let's try again, {user_name}!")
            break
        if correct_answer == 3:
            print(f'Congratulations, {user_name}!')


def main():
    find_progression(max_raund)


if __name__ == "__main__":
    main()
