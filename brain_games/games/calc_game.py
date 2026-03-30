import random


def calc_game_rules():
    print('What is the result of the expression?')
def calc_game():
    first_number = random.randint(1, 30)
    second_number = random.randint(1, 30)
    sign = '+-*'[random.randint(0, 2)]
    mathematical_expression = f'{first_number} {sign} {second_number}'
    solution = str(eval(mathematical_expression))
    return mathematical_expression, solution