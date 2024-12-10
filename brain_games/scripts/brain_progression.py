from brain_games.engine import run_game
from brain_games.games import progression


def main():
    """
    Точка входа для игры найди пропущенное число.
    """
    run_game(progression)


if __name__ == '__main__':
    main()
