import prompt
from random import randint
from brain_games.cli import welcome_user as main_user_name
from brain_games.scripts.brain_games import max_raund_game as max_raund


def game_calc(max_raund):
    user_name = main_user_name()
    print('What is the result of the expression?')
    correct_answer = 0
    while correct_answer != max_raund:
        number_a, number_b = randint(1, 10), randint(1, 10)
        operation_symbol = ['-', '*', '+']
        operation = randint(0, 2)
        print(f'Question: {number_a} {operation_symbol[operation]} {number_b}')
        if operation_symbol[operation] == '+':
            correct_result = number_a + number_b
        elif operation_symbol[operation] == '-':
            correct_result = number_a - number_b
        elif operation_symbol[operation] == '*':
            correct_result = number_a * number_b

        user_answer = prompt.integer('Your answer: ')
        if user_answer == correct_result:
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
    game_calc(max_raund)


if __name__ == "__main__":
    main()
