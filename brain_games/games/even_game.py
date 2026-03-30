import random


def even_game_rules():
    print('Answer "yes" if the number is even, otherwise answer "no".')


def even_game():
    random_number = random.randint(1, 30)
    is_random_number_eval = random_number % 2 == 0 and "yes" or "no"
    return random_number, is_random_number_eval
