import random


def gcd_game_rules():
    print("Find the greatest common divisor of given numbers.")


def gcd_game():
    multiplier = random.randint(2, 10)
    first_number = random.randint(1, 20) * multiplier
    second_number = random.randint(1, 20) * multiplier
    random_numbers = f"{first_number} {second_number}"
    # gcd
    a, b = first_number, second_number
    while b != 0:
        a, b = b, a % b
    gcd = str(a)
    return random_numbers, gcd
