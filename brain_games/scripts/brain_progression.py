from random import randint

def find_progression(game_raund = 3):
    print('What number is missing in the progression?')
    number_start = randint(1, 10)  # старт 
    progress_list = []  # массив чисел
    number_progress = randint(2, 5)  # прогресс
    list_len = randint(5, 10)  # длина массива

    while len(progress_list) != list_len:  # создаем массив с рандомными числами
        number_start += number_progress
        progress_list.append(number_start)

    secret_position = randint(0, list_len-1)  # определим позицию для скрытия
    secret_number = progress_list[secret_position]  # сохраняем правильный число
    progress_list[secret_position] = '..'
    print(*progress_list)
    #while 
find_progression() 