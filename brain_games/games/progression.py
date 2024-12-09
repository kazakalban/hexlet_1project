from random import randint

DESCRIPTION = 'What number is missing in the progression?'


def generate_question_and_answer():
    """
    Генерирует арифметической прогрессии с пропушенным
      числом и правильного ответа.
    Возвращает tuple: Вопрос в виде строки и правильный ответ в виде строки.
    """
    number_start = randint(1, 10)  # старт
    progress_list = []  # массив чисел
    number_progress = randint(2, 5)  # прогресс
    list_len = randint(5, 10)  # длина массива

    while len(progress_list) != list_len:
        # создаем массив с рандомными числами
        number_start += number_progress
        progress_list.append(number_start)

    # определим позицию для скрытия
    secret_position = randint(0, list_len - 1)
    # сохраняем правильный число
    correct_answer = progress_list[secret_position]
    progress_list[secret_position] = '..'
    question = " ".join(map(str, progress_list))
    return question, str(correct_answer)
