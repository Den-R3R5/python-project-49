import math
import random


def prime_game_rules():
    print('Answer "yes" if given number is prime. Otherwise answer "no".')


def is_prime(n):
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False

    for i in range(5, int(math.sqrt(n)) + 1, 6):
        if n % i == 0 or n % (i + 2) == 0:
            return False
    return True


def prime_game():
    random_number = random.randint(2, 100)
    is_random_number_prime = is_prime(random_number)

    return random_number, is_random_number_prime and "yes" or "no"
