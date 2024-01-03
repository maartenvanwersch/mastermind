def evaluate(secret, guess):
    result = [0, 0]
    for count, value in enumerate(secret):
        if guess[count] == value:
            result[0] += 1
    return result

