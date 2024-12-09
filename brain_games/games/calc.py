from random import randint


DESCRIPTION = "What is the result of the expression?"


def generate_question_and_answer():
    """
    Генерация математических вырвжения из двух случайных чисел
      и случайной операции.
    Возвращает tuple: Вопрос в виде строки и правильный ответ в виде строки.
    """
    number_1, number_2 = randint(1, 100), randint(1, 100)
    operation_symbol = ['-', '+', '*']
    operation = randint(0, 2)

    question = f"{number_1} {operation_symbol[operation]} {number_2}"
    if operation_symbol[operation] == '+':
        correct_answer = number_1 + number_2
    elif operation_symbol[operation] == '-':
        correct_answer = number_1 - number_2
    elif operation_symbol[operation] == '*':
        correct_answer = number_1 * number_2

    return question, str(correct_answer)
