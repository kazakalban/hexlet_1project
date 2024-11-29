from brain_games.cli import welcome_user as main_user_name
from brain_games.scripts.brain_games import max_raund_game as max_raund  # Импорт количества раунда
from random import randint
import prompt



def chek_is_prime_number(number:int) -> bool:
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


def number_is_prime(max_raunds):
    user_name = main_user_name()
    print('Answer "yes" if given number is prime. Otherwise answer "no".')
    correct_answers = 0

    while correct_answers < max_raunds:
        number = randint(1, 100)
        print(f'Question: {number}')
        user_answer = prompt.string('Your answer: ').lower()

        if user_answer not in ('yes', 'no'):
            print(f"Incorrect answer. Let's try again, {user_name}!")
            break

        correct_answer = 'yes' if chek_is_prime_number(number) else 'no'

        if user_answer == correct_answer:
            print("Correct!")
            correct_answers += 1
        else:
            print(f"'{user_answer}' is wrong answer ;(. Correct answer was '{correct_answer}'.")
            print(f"Let's try again, {user_name}")
            break

        if correct_answers == max_raunds:
            print(f'Congratulations, {user_name}!')


def main():
    number_is_prime(max_raund)


if __name__ == "__main__":
    main()


