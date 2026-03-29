import random
import prompt

def hello_user():
    print("Welcome to the Brain Games!")
    name = prompt.string('May I have your name? ')
    print(f"Hello, {name}!")
    return name
def even_game(name):
    print('Answer "yes" if the number is even, otherwise answer "no".')
    for i in range(3):
        random_number = random.randint(1, 30)
        is_random_number_eval = random_number % 2 == 0 and 'yes' or 'no'
        print(f"Question: {random_number}")
        answer = prompt.string("Your answer: ")
        if answer == is_random_number_eval:
            print("Correct!")
        else:
            print(f"'{answer}' is wrong answer ;(. Correct answer was {is_random_number_eval}.\nLet's try again, {name}!")
            return
    print(f"Congratulations, {name}!")
