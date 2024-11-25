import prompt


def welcome_user():
    print("Welcome to the Brain Games!")
    ask_text = 'May I have your name? '
    name = prompt.string(ask_text)
    print(f'Hello, {name}!')
    return name
