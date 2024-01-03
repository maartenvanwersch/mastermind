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


def test_given_all_wrong_placed_colours_return_all_wrong_placed():
    secret = ["red", "blue", "red"]
    guess = ["blue", "red", "blue"]
    result = evaluate(secret, guess)
    assert result == [0, 3]


@pytest.mark.parametrize("secret, guess, expected_output", [
    (["green", "red", "blue"], ["blue", "blue", "green"], [0, 3]),
    (["green", "red", "blue", "yellow"], ["blue", "blue", "green", "white"], [0, 4]),
    (["blue", "red"], ["yellow", "white"], [0, 2]),
    (["blue"], ["red"], [0, 1]),
])
def test_given_all_wrong_placed_colours_of_different_lengths_return_all_wrong_placed(secret, guess, expected_output):
    result = evaluate(secret, guess)
    assert result == expected_output
