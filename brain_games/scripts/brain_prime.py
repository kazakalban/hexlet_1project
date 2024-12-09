from brain_games.engine import run_game
from brain_games.games import prime


def main():
    """
    Дверь для игры Проверка на простоту.
    """
    run_game(prime)


if __name__ == '__main__':
    main()
