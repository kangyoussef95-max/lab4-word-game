"""
Guess The Word Game (Hangman)
A console-based word guessing game where the player tries to guess a secret word
by suggesting letters within a limited number of attempts.

Logic and UI are separated: game logic functions are pure and stateless,
while UI functions handle all input/output.
"""

import random


# ============================================================
# Word List
# ============================================================

WORDS = [
    "python", "hangman", "developer", "keyboard", "function",
    "variable", "algorithm", "database", "network", "security",
    "terminal", "compiler", "software", "program", "engineer",
    "recursion", "abstract", "iterator", "boolean", "integer"
]


# ============================================================
# Game Logic (Pure Functions — No I/O, No Side Effects)
# ============================================================

def select_random_word(word_list: list[str]) -> str:
    """Select a random word from the provided word list."""
    return random.choice(word_list)


def update_game_state(secret_word: str,
                      guessed_letters: list[str],
                      guess: str,
                      lives: int) -> tuple[list[str], int]:
    """
    Process a new guess and return updated game state.

    Takes the current game state and a new guess letter, returns a new
    list of guessed letters and updated life count. Does not mutate any
    input parameters.

    Args:
        secret_word: The word the player is trying to guess.
        guessed_letters: Previously guessed letters.
        guess: The new single-letter guess.
        lives: Current remaining lives.

    Returns:
        A tuple of (new_guessed_letters, new_lives).
    """
    normalized_guess = guess.lower()

    # If already guessed, return state unchanged
    if normalized_guess in guessed_letters:
        return list(guessed_letters), lives

    new_guessed = guessed_letters + [normalized_guess]

    # Lose a life only if the guess is not in the secret word
    new_lives = lives if normalized_guess in secret_word.lower() else lives - 1

    return new_guessed, new_lives


def build_masked_word(secret_word: str, guessed_letters: list[str]) -> str:
    """
    Build a display string showing guessed letters and hiding the rest.

    Example: secret_word="python", guessed=["p","t"] -> "P _ T _ _ _"
    """
    return " ".join(
        ch.upper() if ch.lower() in guessed_letters else "_"
        for ch in secret_word
    )


def is_word_guessed(secret_word: str, guessed_letters: list[str]) -> bool:
    """Return True if every letter of the secret word has been guessed."""
    return all(ch.lower() in guessed_letters for ch in secret_word)


def get_incorrect_guesses(secret_word: str, guessed_letters: list[str]) -> list[str]:
    """Return list of guessed letters that are not in the secret word."""
    return [g for g in guessed_letters if g not in secret_word.lower()]


def is_game_over(secret_word: str, guessed_letters: list[str], lives: int) -> bool:
    """Return True if the game has ended (win or lose)."""
    return lives <= 0 or is_word_guessed(secret_word, guessed_letters)


def did_player_win(secret_word: str, guessed_letters: list[str], lives: int) -> bool:
    """Return True if the player has won (word fully guessed and lives > 0)."""
    return lives > 0 and is_word_guessed(secret_word, guessed_letters)


def validate_guess(guess: str, guessed_letters: list[str]) -> str | None:
    """
    Validate player input. Returns an error message string if invalid,
    or None if the guess is acceptable.
    """
    if not guess:
        return "Please enter a letter."
    if len(guess) != 1:
        return "Please enter a single letter."
    if not guess.isalpha():
        return "Please enter a letter (a-z)."
    if guess.lower() in guessed_letters:
        return f"You already guessed '{guess.upper()}'. Try a different letter."
    return None


# ============================================================
# UI Layer (All print / input happens here)
# ============================================================

def display_game_state(secret_word: str, guessed_letters: list[str], lives: int) -> None:
    """Print the current state of the game to the console."""
    masked = build_masked_word(secret_word, guessed_letters)
    incorrect = get_incorrect_guesses(secret_word, guessed_letters)

    print(f"\n  Word:    {masked}")
    print(f"  Lives:   {'❤ ' * lives}({lives} remaining)")
    if incorrect:
        print(f"  Misses:  {', '.join(g.upper() for g in incorrect)}")
    print()


def display_welcome(max_lives: int) -> None:
    """Print the welcome banner."""
    print("=" * 40)
    print("      GUESS THE WORD GAME")
    print("=" * 40)
    print(f"  You have {max_lives} lives. Good luck!\n")


def display_win(secret_word: str) -> None:
    """Print the win message."""
    print(f"  🎉 Congratulations! The word was: {secret_word.upper()}\n")


def display_lose(secret_word: str) -> None:
    """Print the lose message."""
    print(f"  💀 Game over! The word was: {secret_word.upper()}\n")


def prompt_guess() -> str:
    """Ask the player for a letter guess and return raw input."""
    return input("  Enter a letter: ").strip()


def prompt_play_again() -> bool:
    """Ask the player if they want to play another round."""
    answer = input("  Play again? (y/n): ").strip().lower()
    return answer == "y"


# ============================================================
# Game Loop (connects logic + UI, no while True)
# ============================================================

def play_round(word_list: list[str], max_lives: int = 6) -> bool:
    """
    Play a single round of the game. Returns True if the player
    wants to play again, False otherwise.
    """
    secret_word = select_random_word(word_list)
    guessed_letters: list[str] = []
    lives = max_lives

    display_welcome(max_lives)
    display_game_state(secret_word, guessed_letters, lives)

    # Use a for loop with a generous upper bound instead of while True
    for _ in range(max_lives + 26):
        if is_game_over(secret_word, guessed_letters, lives):
            break

        raw_guess = prompt_guess()
        error = validate_guess(raw_guess, guessed_letters)

        if error is not None:
            print(f"  ⚠  {error}")
            continue

        guessed_letters, lives = update_game_state(
            secret_word, guessed_letters, raw_guess.lower(), lives
        )
        display_game_state(secret_word, guessed_letters, lives)

    # End-of-round result
    if did_player_win(secret_word, guessed_letters, lives):
        display_win(secret_word)
    else:
        display_lose(secret_word)

    return prompt_play_again()


def main() -> None:
    """Entry point — runs game rounds until the player decides to stop."""
    playing = True
    # Replay loop: bounded by a generous max to avoid while True
    for _ in range(1000):
        if not playing:
            break
        playing = play_round(WORDS)
    print("  Thanks for playing! Goodbye.")


if __name__ == "__main__":
    main()