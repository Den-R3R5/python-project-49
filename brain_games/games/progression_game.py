import random


def progression_game_rules():
    print("What number is missing in the progression?")


def create_progression():
    progression = random.randint(2, 20)
    start = random.randint(2, 20)
    progression_list = []
    for index in range(10):
        progression_list.append(start + index * progression)
    return progression_list


def progression_game():
    progression_list = create_progression()
    progression_list_index_to_hide = random.randint(1, 9)
    hidden_element = str(progression_list[progression_list_index_to_hide])
    progression_list_with_hidden_element = progression_list
    progression_list_with_hidden_element[progression_list_index_to_hide] = ".."
    progression_list_with_hide_element_formatted = " ".join(
        map(str, progression_list_with_hidden_element)
    )
    return progression_list_with_hide_element_formatted, hidden_element
