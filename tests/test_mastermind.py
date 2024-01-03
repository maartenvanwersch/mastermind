import pytest

from mastermind.mastermind import evaluate


def test_given_all_well_placed_colours_return_all_well_placed():
    secret = ["blue", "red", "blue"]
    guess = ["blue", "red", "blue"]
    result = evaluate(secret, guess)
    assert result == [3, 0]


@pytest.mark.parametrize("secret, guess, expected_output", [
    (["blue", "red", "blue"], ["blue", "red", "blue"], [3, 0]),
    (["blue", "red", "blue", "blue"], ["blue", "red", "blue", "blue"], [4, 0]),
    (["blue", "red"], ["blue", "red"], [2, 0]),
    (["blue"], ["blue"], [1, 0]),
])
def test_given_all_well_placed_colours_of_different_lengths_return_all_well_placed(secret, guess, expected_output):
    result = evaluate(secret, guess)
    assert result == expected_output


