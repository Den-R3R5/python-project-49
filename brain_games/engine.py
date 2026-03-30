import prompt

def hello_user():
    print("Welcome to the Brain Games!")
    name = prompt.string('May I have your name? ')
    print(f"Hello, {name}!")
    return name
def question(game_input):
    print(f"Question: {game_input}")
def user_answer():
    user_input = prompt.string("Your answer: ")
    return user_input
def check_answer(user_input, game_answer, name):
    if user_input == game_answer:
        print("Correct!")
        return True
    else:
        print(f"'{user_input}' is wrong answer ;(. Correct answer was {game_answer}.\nLet's try again, {name}!")
        return False
def congratulations(name):
    print(f"Congratulations, {name}!")