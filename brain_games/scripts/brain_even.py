from brain_games import (
    check_answer,
    congratulations,
    even_game,
    even_game_rules,
    hello_user,
    question,
    user_answer,
)


def main():
    name = hello_user()
    even_game_rules()
    for i in range(3):
        game_input, game_answer = even_game()
        question(game_input)
        user_input = user_answer()
        is_user_right = check_answer(user_input, game_answer, name)
        if not is_user_right:
            return
    congratulations(name)


if __name__ == "__main__":
    main()
