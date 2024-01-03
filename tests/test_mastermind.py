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


def test_given_all_wrong_colours_return_no_well_placed_and_no_misplaced():
    secret = ["red", "blue", "red"]
    guess = ["green", "yellow", "white"]
    result = evaluate(secret, guess)
    assert result == [0, 0]


def test_given_empty_guess_return_no_right_placed_and_no_misplaced():
    secret = ["red", "blue"]
    guess = []
    assert evaluate(secret, guess) == [0, 0]

