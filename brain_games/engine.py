from prompt import string  # Внешняя библиотека

from brain_games.cli import welcome_user  # Локальный модуль

MAX_ROUNDS = 3


def run_game(game):
    """
    Движок для запуска игры, принимает на вход объект игры
    """
    # Приветствие
    name = welcome_user()
    # Описание игры
    print(game.DESCRIPTION)
    # Количества правильных ответов
    correct_answers = 0
    # Играем пока правильный ответ не равно MAX_ROUNDS
    while correct_answers < MAX_ROUNDS:
        # получаем вопрос и правильный ответ
        question, correct_answer = game.generate_question_and_answer()
        print(f'Question: {question}')
        # Ответ пользователя
        answer = string('Your answer: ')
        # Если ответ пользователя правильный увеличиваем счетчик на 1
        if answer == correct_answer:
            print('Correct!')
            correct_answers += 1
        # Иначе - завершаем игру
        else:
            print(f"'{answer}' is wrong answer ;(. "
                  f"Correct answer was '{correct_answer}'")
            print(f"Let's try again, {name}!")
            return
        # Поздравление если победил
    print(f'Congratulations, {name}!')
