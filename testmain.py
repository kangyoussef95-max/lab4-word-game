"""
Tests for the Guess The Word game logic functions.

Run with: python -m pytest test_main.py -v
Or simply: python test_main.py
"""

from main import (
    update_game_state,
    build_masked_word,
    is_word_guessed,
    get_incorrect_guesses,
    is_game_over,
    did_player_win,
    validate_guess,
    select_random_word,
)


# ---- update_game_state tests ----

def test_correct_guess_no_life_lost():
    """A correct guess should not decrease lives."""
    new_guessed, new_lives = update_game_state("python", [], "p", 6)
    assert "p" in new_guessed
    assert new_lives == 6


def test_incorrect_guess_loses_life():
    """An incorrect guess should decrease lives by 1."""
    new_guessed, new_lives = update_game_state("python", [], "z", 6)
    assert "z" in new_guessed
    assert new_lives == 5


def test_duplicate_guess_unchanged():
    """Guessing an already-guessed letter should not change state."""
    new_guessed, new_lives = update_game_state("python", ["p"], "p", 6)
    assert new_guessed == ["p"]
    assert new_lives == 6


def test_update_does_not_mutate_input():
    """update_game_state must not mutate the original guessed_letters list."""
    original = ["a", "b"]
    original_copy = list(original)
    update_game_state("python", original, "p", 6)
    assert original == original_copy, "Original list was mutated!"


def test_case_insensitive_guess():
    """Uppercase guess should match lowercase secret word."""
    new_guessed, new_lives = update_game_state("python", [], "P", 6)
    assert "p" in new_guessed
    assert new_lives == 6


# ---- build_masked_word tests ----

def test_masked_word_no_guesses():
    """With no guesses, all letters should be hidden."""
    result = build_masked_word("python", [])
    assert result == "_ _ _ _ _ _"


def test_masked_word_partial_guess():
    """Only guessed letters should be revealed."""
    result = build_masked_word("python", ["p", "t"])
    assert result == "P _ T _ _ _"


def test_masked_word_full_guess():
    """When all letters are guessed, the full word should show."""
    result = build_masked_word("hi", ["h", "i"])
    assert result == "H I"


# ---- is_word_guessed tests ----

def test_word_not_guessed():
    assert is_word_guessed("python", ["p", "y"]) is False


def test_word_fully_guessed():
    assert is_word_guessed("python", ["p", "y", "t", "h", "o", "n"]) is True


def test_word_guessed_with_extras():
    """Extra wrong guesses shouldn't prevent a win."""
    assert is_word_guessed("hi", ["h", "i", "z", "x"]) is True


# ---- get_incorrect_guesses tests ----

def test_no_incorrect_guesses():
    result = get_incorrect_guesses("python", ["p", "y"])
    assert result == []


def test_some_incorrect_guesses():
    result = get_incorrect_guesses("python", ["p", "z", "x"])
    assert result == ["z", "x"]


# ---- is_game_over tests ----

def test_game_not_over():
    assert is_game_over("python", ["p"], 5) is False


def test_game_over_no_lives():
    assert is_game_over("python", ["z"], 0) is True


def test_game_over_word_guessed():
    assert is_game_over("hi", ["h", "i"], 4) is True


# ---- did_player_win tests ----

def test_player_wins():
    assert did_player_win("hi", ["h", "i"], 3) is True


def test_player_loses():
    assert did_player_win("python", ["z", "x"], 0) is False


# ---- validate_guess tests ----

def test_validate_empty_input():
    assert validate_guess("", []) is not None


def test_validate_multiple_chars():
    assert validate_guess("ab", []) is not None


def test_validate_number():
    assert validate_guess("3", []) is not None


def test_validate_already_guessed():
    assert validate_guess("a", ["a"]) is not None


def test_validate_good_guess():
    assert validate_guess("a", []) is None


# ---- select_random_word tests ----

def test_random_word_from_list():
    words = ["alpha", "beta", "gamma"]
    result = select_random_word(words)
    assert result in words


# ---- Run tests manually if not using pytest ----

if __name__ == "__main__":
    test_funcs = [v for k, v in globals().items() if k.startswith("test_") and callable(v)]
    passed = 0
    failed = 0
    for fn in test_funcs:
        try:
            fn()
            passed += 1
            print(f"  ✅ {fn.__name__}")
        except AssertionError as e:
            failed += 1
            print(f"  ❌ {fn.__name__}: {e}")
    print(f"\nResults: {passed} passed, {failed} failed out of {passed + failed} tests.")