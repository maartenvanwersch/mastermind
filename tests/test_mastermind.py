from mastermind.mastermind import evaluate


def test_given_all_well_placed_colours_return_all_well_placed():
    secret = ["blue", "red", "blue"]
    guess = ["blue", "red", "blue"]
    result = evaluate(secret, guess)
    assert result == [3, 0]