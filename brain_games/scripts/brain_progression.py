from brain_games.cli import welcome_user as main_user_name
from brain_games.scripts.brain_games import max_raund_game as max_raund  # Импорт количества раунда
from random import randint
import prompt


def find_progression(max_raund):
    user_name = main_user_name()
    print('What number is missing in the progression?')
    current_answer = 0
    while max_raund != current_answer:
        number_start = randint(1, 10)  # старт 
        progress_list = []  # массив чисел
        number_progress = randint(2, 5)  # прогресс
        list_len = randint(5, 10)  # длина массива

        while len(progress_list) != list_len:  # создаем массив с рандомными числами
            number_start += number_progress
            progress_list.append(number_start)

        secret_position = randint(0, list_len-1)  # определим позицию для скрытия
        secret_number = progress_list[secret_position]  # сохраняем правильный число
        progress_list[secret_position] = '..'
        #print(*progress_list)
        print('Question: ', *progress_list)
        user_answer = prompt.integer('Your answer: ')
        if user_answer == secret_number:
            print('Correct!')
            current_answer += 1
        else:
            print(f"'{user_answer}' is wrong answer ;(. Correct answer was '{secret_number}'\n"
                  f"Let's try again,{user_name}!")
            break


def main():
    find_progression(max_raund)


if __name__ == "__main__":
    main()