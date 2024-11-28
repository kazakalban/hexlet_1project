from brain_games.cli import welcome_user as main_user_name
from brain_games.scripts.brain_games import max_raund_game as max_raund  # Импорт количества раунда
from random import randint
import prompt


def is_even(number:int) -> bool:
    return True if number % 2 == 0 else False

def game_parity_check(max_raund):
    user_name = main_user_name()
    print('Answer "yes" if the number is even, otherwise answer "no".')
    correct_answer = 0
    while correct_answer != max_raund:
        number = randint(1, 100)
        print(f'Question: {number}')
        user_answer = prompt.string('Your answer: ')
        user_answer = True if user_answer == 'yes' else user_answer = False
        if is_even(number) and user_answer:
            print("Correct!")
            correct_answer += 1
        elif is_even(number) and user_answer:
            print("Correct!")
            correct_answer += 1
        elif user_answer == True or user_answer == False:
            print(f"'{user_answer}' is wrong answer ;(. Correct answer was 'no'.\n"
                      f"Let's try again, {user_name}!") if user_answer == True else print(f"'{user_answer}' is wrong answer ;(. Correct answer was 'yes'.\n"
                      f"Let's try again, {user_name}!")
            break
        else:
            print(f"Incorrect answer. Let's try again, {user_name}!")
            break
        if correct_answer == 3:
            print(f'Congratulations, {user_name}!')


def main():
    game_parity_check(max_raund)


if __name__ == "__main__":
    main()
