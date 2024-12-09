from math import gcd
from random import randint

DESCRIPTION = 'Find the greatest common divisor of given numbers.'


def generate_question_and_answer():
    """
    Генерация двух случайных чисел и вычисление
    их наиьбольшего обшего делителя (НОД)
    Возвращает tuple: Вопрос в виде строки и правильный ответ в виде строки.
    """
    # формурирует чтобы номера не были ровными и общ дел не был ровно 1
    while True:
        number_a, number_b = randint(2, 25), randint(2, 25)
        if number_a != number_b and gcd(number_a, number_b) != 1:
            break
    question = f'{number_a} {number_b}'
    correct_answer = str(gcd(number_a, number_b))
    return question, correct_answer
