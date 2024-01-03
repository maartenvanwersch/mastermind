def evaluate(secret, guess):
    correct_guessed_indices = []
    filtered_guess_list = guess.copy()
    filtered_secret_list = secret.copy()
    for count, value in enumerate(secret):
        if len(guess) > count and guess[count] == value:
            correct_guessed_indices.append(count)
            filtered_guess_list.remove(value)
            filtered_secret_list.remove(value)
    misplaced_list = [value for value in filtered_guess_list if value in filtered_secret_list]
    return [len(correct_guessed_indices), len(misplaced_list)]

