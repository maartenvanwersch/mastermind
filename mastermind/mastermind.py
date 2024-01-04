def evaluate(secret, guess):
    if len(secret) != len(guess):
        raise ValueError("Guess and secret lists length are not equal")
    correct_guessed_indices = find_matching_positions(secret, guess)
    misplaced = find_overlap_after_removing_indices(correct_guessed_indices, guess, secret)
    return [len(correct_guessed_indices), len(misplaced)]


def find_overlap_after_removing_indices(indices_to_remove, guess, secret):
    filtered_secret = remove_indices(secret, indices_to_remove)
    filtered_guess = remove_indices(guess, indices_to_remove)
    return find_overlap(filtered_secret, filtered_guess)


def find_matching_positions(list1, list2):
    return [i for i, (x, y) in enumerate(zip(list1, list2)) if x == y]


def remove_indices(original_list, indices_to_remove):
    return [item for i, item in enumerate(original_list) if i not in indices_to_remove]


def find_overlap(list1, list2):
    return [value for value in list1 if value in list2]

