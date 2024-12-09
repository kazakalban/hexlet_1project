from random import randint

DESCRIPTION = 'Answer "yes" if given number is prime. Otherwise answer "no".'


def is_prime(number):
    """
    Проверка число на простоту.
    Передается number(int)
    Возвращает bool: True, если число простое,
    иначе False
    """
    if number <= 1:
        return False
    for i in range(2, int(number ** 0.5) + 1):
        if number % i == 0:
            return False
    return True


def generate_question_and_answer():
    """
    Генерирует случайное число и правильный ответ является ли число простым.
    Возвращает tuple: Вопрос в виде строки и правильный ответ в виде строки.
    """
    number = randint(1, 100)
    question = str(number)

    correct_answer = 'yes' if is_prime(number) else 'no'
    return question, correct_answer
