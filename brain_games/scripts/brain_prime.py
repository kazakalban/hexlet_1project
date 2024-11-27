from random import randint
from math import sqrt
import prompt
def chek_is_prime_number(number = 3):
    """ Вернет True если простое, 
    если не простое тогда False"""
    if number <= 1:
        return False
    elif number == 2:  # 2 - единственное четное число
        return True
    elif number % 2 == 0:
        return  False
    n = int(number ** 0.5)
    for i in range(3, n + 1, 2):  # шаг 2 потому что проверяем нечетные числа
        if number % i == 0:
            return False  # найден делитель
    return True


def number_is_prime(max_raund):
    #user_name = main_user_name()
    user_name = 'Kasym'
    print('Answer "yes" if given number is prime. Otherwise answer "no".')
    correct_answer = 0
    while correct_answer != max_raund:
        number = randint(1, 100)
        print(f'Question: {number}')
        
        user_answer = prompt.string('Your answer: ')
        if chek_is_prime_number(number) and user_answer == 'no':
            print("Correct!")
            correct_answer += 1
        elif chek_is_prime_number(number) and user_answer != 'yes':
            print("Correct!")
            correct_answer += 1
        else:
            print("lets try agan", "yes" if user_answer == 'no' else 'no')
            break
        if correct_answer == 3:
            print(f'Congratulations, {user_name}!')


number_is_prime(3)