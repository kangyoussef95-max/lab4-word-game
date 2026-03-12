# Guess The Word Game

A console-based word guessing game (Hangman-style) built for the Generative AI for Software Engineering course at EPITA.

## How to Play

```bash
python ./main.py
```

The game picks a random word and you guess it one letter at a time. You start with 6 lives — each wrong guess costs one life. Guess the full word before running out of lives to win. After each round you can choose to play again.

## Project Structure

```
├── main.py              # Game implementation (logic + UI)
├── test_main.py         # Unit tests for game logic
├── MY_NOTES.md          # Design thinking notes
├── JOURNAL.md           # CoPilot interaction log
├── REPORT.md            # Project report and reflections
├── README.md            # This file
└── .github/
    ├── copilot-instructions.md
    └── agents/
        └── journal-logger.agent.md
```

## Running the Tests

### With pytest (recommended)

```bash
# Set up a virtual environment (optional but recommended)
python -m venv venv
source venv/bin/activate   # On Windows: venv\Scripts\activate

# Install pytest
pip install pytest

# Run tests
python -m pytest test_main.py -v
```

### Without pytest

```bash
python test_main.py
```

This runs all test functions and prints pass/fail results to the console.

## Design

The code separates **game logic** (pure functions with no I/O) from the **UI layer** (all `print`/`input` calls). This makes the logic easy to test independently.

Key constraints followed:
- No `while True` loops — uses bounded `for` loops with break conditions
- No string replacement functions (`.replace()` etc.)
- Supports replay without restarting the program
- `update_game_state` is a pure function that does not mutate its inputs
