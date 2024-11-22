from brain_games.cli import welcome_user as main_user_name
from random import randint
import prompt


def game_parity_check():
    user_name = main_user_name()
    print('Answer "yes" if the number is even, otherwise answer "no".')
    correct_answer = 0
    while correct_answer != 3:
        ask_user_number_text = 'Question:'
        number = randint(1, 100)
        print(f'{ask_user_number_text} {number}')
        user_answer = prompt.string('Your answer: ')
        if number % 2 == 0 and user_answer == 'yes':
            print("Correct!")
            correct_answer += 1
        elif number % 2 == 1 and user_answer == 'no':
            print("Correct!")
            correct_answer += 1
        elif user_answer == 'yes' or user_answer == 'no':
            if user_answer == 'yes':
                print(f"'{user_answer}' is wrong answer ;(. Correct answer was 'no'."
                      f"Let's try again, {user_name}!")
            elif user_answer == 'no':
                print(f"'{user_answer}' is wrong answer ;(. Correct answer was 'yes'."
                      f"Let's try again, {user_name}!")
            break
        else:
            print('Incorrect answer')
            break
        if correct_answer == 3:
            print(f'Congratulations, {user_name}!')


def main():
    game_parity_check()


if __name__ == "__main__":
    main()
