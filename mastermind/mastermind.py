def evaluate(secret, guess):
    correct_guessed_indices = find_matching_positions(secret, guess)
    filtered_secret = remove_indices(secret, correct_guessed_indices)
    filtered_guess = remove_indices(guess, correct_guessed_indices)
    misplaced_list = [value for value in filtered_guess if value in filtered_secret]
    return [len(correct_guessed_indices), len(misplaced_list)]


def find_matching_positions(list1, list2):
    return [i for i, (x, y) in enumerate(zip(list1, list2)) if x == y]


def remove_indices(original_list, indices_to_remove):
    return [item for i, item in enumerate(original_list) if i not in indices_to_remove]

