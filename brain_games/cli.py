import prompt

def welcome_user():
        ask_text = 'May I have your name? '
        name = prompt.string(ask_text)
        print(f'Hello, {name}!')



